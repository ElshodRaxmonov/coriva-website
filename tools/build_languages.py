#!/usr/bin/env python3
"""Build the Uzbek pages (uz/) from the English pages and i18n/uz.json.

Usage (from the repository root, Python 3.9+, standard library only):
    python3 tools/build_languages.py            # rebuild uz/ and the language links
    python3 tools/build_languages.py --review   # also rewrite TRANSLATIONS_REVIEW.md (resets its tick boxes)

What it does
- English pages at the root are the source. i18n/uz.json maps English text to Uzbek. It is the only place
  translations live: edit it, never the generated uz/ pages.
- Text nodes and the alt, aria-label, placeholder and title attributes are translated exactly as the old
  client-side toggle (i18n.js) did: whole text node, whitespace collapsed, HTML entities decoded.
- Anything without a translation stays in English and is listed in i18n/missing-uz.txt. Nothing is guessed.
- Every page gets its own <html lang>, title, description, canonical URL and Open Graph tags.
- Language links (every <a lang="..">) point to the same page in the other language.

Publishing
- PUBLISH = False while the Uzbek text is a draft: uz/ pages are noindex, stay out of sitemap.xml, and no
  hreflang links are written. Set PUBLISH = True only after the native and clinical review is done.
"""
import html, json, os, re, sys

PUBLISH = False
SITE = 'https://coriva.uz'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANG, LOCALE, LANG_NAME = 'uz', 'uz_UZ', 'O‘zbekcha'
ATTRS = ('alt', 'aria-label', 'placeholder', 'title')
# Text that scripts write at run time (live.js, r7.js). The Uzbek pages carry these in window.__CORIVA_T.
SCRIPT_STRINGS = ('Play video', 'Pause video', 'Previous moment', 'Next moment', 'Every heartbeat matters.')

def read(p): return open(os.path.join(ROOT, p), encoding='utf-8').read()
def write(p, t):
    p = os.path.join(ROOT, p); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(t)

UZ = json.loads(read('i18n/uz.json'))
norm = lambda s: re.sub(r'\s+', ' ', html.unescape(s)).strip()
PAGES = sorted(f[:-5] for f in os.listdir(ROOT) if f.endswith('.html'))
url = lambda lang, page: SITE + ('/' if lang == 'en' else f'/{lang}/') + ('' if page == 'index' else page)
missing = {}   # page -> ordered set of English strings without a translation
SKIP = {'English', LANG_NAME}   # language names, and Uzbek text written by split_headlines()
used = {}      # English string -> (Uzbek, first page)

def tr(s, page, kind='text'):
    key = norm(s)
    if key in UZ:
        used.setdefault(key, (UZ[key], page)); return UZ[key]
    if re.search(r'[A-Za-z]{2}', key) and key not in ('Coriva', 'Coriva.') and key not in SKIP and '@' not in key:
        missing.setdefault(page, {}).setdefault(f'[{kind}] {key}', None)
    return None

def protect(t):
    """Hide script, style and svg blocks so only page text is touched."""
    keep = []
    def put(m): keep.append(m.group(0)); return f'\x00{len(keep) - 1}\x00'
    return re.sub(r'<(script|style|svg)\b.*?</\1>', put, t, flags=re.S), keep
def restore(t, keep): return re.sub(r'\x00(\d+)\x00', lambda m: keep[int(m.group(1))], t)

def lang_links(t, page, to):
    """Point every <a lang=".."> at the same page in language `to`."""
    if to == 'uz': href, name = ('uz/' if page == 'index' else f'uz/{page}.html'), LANG_NAME
    else: href, name = ('../' if page == 'index' else f'../{page}.html'), 'English'
    def fix(m):
        attrs = re.sub(r'\s(?:href|lang|hreflang|role)="[^"]*"', '', m.group(1))
        return f'<a{attrs} href="{href}" lang="{to}" hreflang="{to}">{name}</a>'
    return re.sub(r'<a((?:\s[^>]*)?\slang="[a-z]{2}"[^>]*)>[^<]*</a>', fix, t)

def split_headlines(t, page):
    """Home headlines are pre-split into animated word spans: rebuild them from the translated name."""
    def fix(m):
        tag, attrs, inner = m.group(1), m.group(2), m.group(3)
        label = re.search(r'aria-label="([^"]*)"', attrs)
        u = tr(label.group(1), page, 'headline') if label else None
        if not u: return m.group(0)
        SKIP.add(u); SKIP.update(u.split())
        mark = re.search(r'<span class="s1-mark"[^>]*>.*?</span>', inner, re.S)
        spans = [f'<span class="w" aria-hidden="true"><span style="--i:{i}">{html.escape(w, quote=False)}</span></span>' for i, w in enumerate(u.split())]
        if mark: spans.insert(min(2, len(spans)), mark.group(0))
        attrs = attrs.replace(label.group(0), f'aria-label="{html.escape(u)}"')
        return f'<{tag}{attrs}>' + ' '.join(spans) + f'</{tag}>'
    return re.sub(r'<(h[12])(\s[^>]*class="[^"]*\bs[12]-title\b[^"]*"[^>]*)>(.*?)</\1>', fix, t, flags=re.S)

def presplit_h1(t):
    """Inner pages: r8.js splits the main headline into animated words after the first paint, and longer Uzbek
    words then re-wrap the line (layout shift). Write it pre-split, exactly as r8.js would; r8.js skips it."""
    if 'r8.js' not in t: return t
    def fix(m):
        attrs, text = m.group(1), html.unescape(m.group(2)).strip()
        if 'aria-label=' in attrs: return m.group(0)
        words = ' '.join(f'<span class="w" aria-hidden="true"><span style="--i:{i}">{html.escape(w, quote=False)}</span></span>' for i, w in enumerate(text.split()))
        return (f'<h1{attrs} aria-label="{html.escape(text)}">' + words
                + '<span class="r8-mark" aria-hidden="true"><img src="/blob/00ef871558ec9b9f54c10a145d26dde5.png" alt=""></span></h1>')
    i = t.index('<main'); return t[:i] + re.sub(r'<h1(\s[^>]*)?>([^<]*)</h1>', fix, t[i:], count=1)

def translate_body(t, page):
    t, keep = protect(t)
    out = []
    for tok in re.split(r'(<[^>]+>)', t):
        if tok.startswith('<'):
            def attr(m):
                u = tr(m.group(3), page, m.group(2)); return m.group(0) if u is None else f'{m.group(1)}{m.group(2)}="{html.escape(u)}"'
            if not re.match(r'<a\s[^>]*\slang="', tok) and not tok.startswith(('<meta', '<link', '<html')):
                tok = re.sub(r'(\s)(' + '|'.join(ATTRS) + r')="([^"]*)"', attr, tok)
            out.append(tok)
        elif tok.strip() and '\x00' not in tok:
            u = tr(tok, page)
            out.append(tok if u is None else re.match(r'\s*', tok).group(0) + html.escape(u, quote=False) + re.search(r'\s*$', tok).group(0))
        else:
            out.append(tok)
    return restore(''.join(out), keep)

def rebase_assets(t):
    """uz/ pages live one folder down: assets move to ../, links between pages stay inside uz/."""
    def one(v):
        if v.startswith(('http:', 'https:', '//', '/', '#', 'mailto:', 'tel:', 'data:', '../')): return v
        if v == './' or re.match(r'[\w-]+\.html(?:#.*)?$', v): return v
        return '../' + v
    t = re.sub(r'(\s(?:src|href|poster))="([^"]*)"', lambda m: f'{m.group(1)}="{one(m.group(2))}"', t)
    return re.sub(r'(\ssrcset)="([^"]*)"', lambda m: m.group(1) + '="' + ', '.join(' '.join([one(p.split()[0])] + p.split()[1:]) for p in m.group(2).split(',')) + '"', t)

def head(t, page, lang):
    """lang, canonical, Open Graph, robots and (once published) hreflang for one page."""
    t = re.sub(r'<html lang="[a-z]{2}"', f'<html lang="{lang}"', t, count=1)
    t = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url(lang, page)}">', t, count=1)
    t = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url(lang, page)}">', t, count=1)
    t = re.sub(r'\n<meta property="og:locale"[^>]*>', '', t)
    t = t.replace('<meta property="og:type"', f'<meta property="og:locale" content="{"en_US" if lang == "en" else LOCALE}">\n<meta property="og:type"', 1)
    t = re.sub(r'\n<link rel="alternate" hreflang="[^"]*" href="[^"]*">', '', t)
    if PUBLISH and page not in ('404',) and 'noindex' not in read(page + '.html'):
        alts = ''.join(f'\n<link rel="alternate" hreflang="{l}" href="{url(l, page)}">' for l in ('en', LANG)) + f'\n<link rel="alternate" hreflang="x-default" href="{url("en", page)}">'
        t = t.replace(f'<link rel="canonical" href="{url(lang, page)}">', f'<link rel="canonical" href="{url(lang, page)}">' + alts, 1)
    return t

def translate_head(t, page):
    m = re.search(r'<title>(.*?)</title>', t, re.S); title = html.unescape(m.group(1))
    if title.startswith('Coriva · '): parts = ('Coriva · ', title[9:], '')
    else: parts = ('', title[:-len(' · Coriva')], ' · Coriva')
    name, draft = parts[1], ''
    if name.endswith(' (draft)'): name, draft = name[:-8], ' (draft)'
    u = tr(name + '.', page, 'title') if norm(name) not in UZ and norm(name + '.') in UZ else tr(name, page, 'title')
    if u and parts[0]: u = u.rstrip('.')
    if draft: draft = ' (' + (tr('draft', page, 'title') or 'draft') + ')'
    new_title = parts[0] + (u or name) + draft + parts[2]
    t = t.replace(m.group(0), f'<title>{html.escape(new_title, quote=False)}</title>', 1)
    t = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{html.escape(new_title)}">', t, count=1)
    for prop in (r'<meta name="description" content="([^"]*)">', r'<meta property="og:description" content="([^"]*)">'):
        d = re.search(prop, t)
        if not d: continue
        en = html.unescape(d.group(1)); u = UZ.get(en)
        if u is None:   # descriptions are the page's lead paragraph, sometimes cut at a sentence end
            full = [k for k in UZ if k.startswith(en.rstrip('…'))]
            if len(full) == 1:
                u = UZ[full[0]]; used.setdefault(full[0], (u, page))
                if len(u) > 158: cut = u[:158]; u = cut[:cut.rindex('.') + 1] if '.' in cut[60:] else cut[:cut.rindex(' ')] + '…'
        if u is None: tr(en, page, 'description'); continue
        t = t.replace(d.group(0), d.group(0).replace(d.group(1), html.escape(u)), 1)
    return t

def build():
    for page in PAGES:
        en = read(page + '.html')
        en = re.sub(r'\n?<script src="i18n\.js[^"]*"[^>]*></script>', '', en)   # static pages replace the toggle
        en = lang_links(en, page, 'uz')
        en = head(en, page, 'en')
        write(page + '.html', en)
        uz = en
        uz = re.sub(r'\n?<script type="application/ld\+json">.*?</script>', '', uz, flags=re.S)
        uz = translate_head(uz, page)
        uz = head(uz, page, LANG)
        table = {}
        for s in SCRIPT_STRINGS:
            u = tr(s, '(scripts, every page)', 'script')
            if u: table[s] = u
        uz = uz.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<script>window.__CORIVA_T = ' + json.dumps(table, ensure_ascii=False) + ';</script>', 1)
        if not PUBLISH: uz = re.sub(r'<meta name="robots" content="[^"]*">', '<meta name="robots" content="noindex, follow">', uz, count=1)
        i = uz.index('<body'); b = split_headlines(uz[i:], page); b = translate_body(b, page)
        uz = presplit_h1(uz[:i] + b)
        uz = rebase_assets(uz)
        uz = lang_links(uz, page, 'en')
        write(f'{LANG}/{page}.html', '<!-- Generated by tools/build_languages.py from ../' + page + '.html and i18n/uz.json. Do not edit. -->\n' + uz)
    sitemap()
    lines = [f'# English strings with no Uzbek translation (generated; {sum(len(v) for v in missing.values())} entries)', '# Add them to i18n/uz.json, then re-run tools/build_languages.py.', '']
    for page in PAGES:
        if page in missing: lines += [f'## {page}.html'] + [f'- {k}' for k in missing[page]] + ['']
    if '(scripts, every page)' in missing: lines += ['## live.js, r7.js (every page)'] + [f'- {k}' for k in missing['(scripts, every page)']] + ['']
    write('i18n/missing-uz.txt', '\n'.join(lines))
    if '--review' in sys.argv: review()
    print(f'{len(PAGES)} pages -> {LANG}/, {len(used)} strings translated, {sum(len(v) for v in missing.values())} missing (i18n/missing-uz.txt), PUBLISH={PUBLISH}')

def sitemap():
    sm = read('sitemap.xml'); locs = re.findall(r'<url><loc>([^<]+)</loc>', sm)
    lastmod = (re.search(r'<lastmod>([^<]+)</lastmod>', sm) or [None, ''])[1]
    pages = [p for p in PAGES if url('en', p) in locs]
    rows = []
    for p in pages:
        for lang in (('en', LANG) if PUBLISH else ('en',)):
            alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{url(l, p)}"/>' for l in ('en', LANG)) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{url("en", p)}"/>' if PUBLISH else ''
            rows.append(f'  <url><loc>{url(lang, p)}</loc>' + (f'<lastmod>{lastmod}</lastmod>' if lastmod else '') + alts + '</url>')
    ns = ' xmlns:xhtml="http://www.w3.org/1999/xhtml"' if PUBLISH else ''
    write('sitemap.xml', f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"{ns}>\n' + '\n'.join(rows) + '\n</urlset>\n')

def review():
    out = ['# Translation review', '', 'Uzbek (Latin): **draft, needs native and clinical review.** The uz/ pages stay `noindex` until every box is ticked',
           'and the owner confirms; then set `PUBLISH = True` in tools/build_languages.py and re-run it.', '',
           'Fix a translation in `i18n/uz.json`, never in uz/. Strings marked ⚕ make a clinical or safety statement: they need a clinician as well as a native reader.', '',
           f'Untranslated strings: see `i18n/missing-uz.txt`.', '']
    out += ['## Search terms (proposal, for the reviewer to accept or reject)', '',
            'Use these only where the page already says the same thing in English. No new claims.', '',
            '- [ ] Home title is "Coriva · Yurak reabilitatsiyasi uyda davom etadi". Keep "yurak reabilitatsiyasi", or prefer "kardioreabilitatsiya"?',
            '- [ ] Home description: add "kardioreabilitatsiya" if it reads naturally, e.g. in the sentence that already says "platforma".',
            '- [ ] Partners heading "Yurak reabilitatsiyasi uchun yagona tizim." uses the same term: keep both pages consistent.', '']
    CLIN = re.compile(r'(?i)emergency|doctor|clinic|diagnos|medic|AI|plan|rehab|heart|cardi|patient|approve|safety|unwell')
    by_page = {}
    for en, (u, page) in used.items(): by_page.setdefault(page, []).append((en, u))
    for page in PAGES:
        if page not in by_page: continue
        out += [f'## {page}.html', '', '| ✓ | English | Uzbek |', '|---|---|---|']
        out += [f'| ☐{" ⚕" if CLIN.search(en) else ""} | {en.replace("|", "\\|")} | {u.replace("|", "\\|")} |' for en, u in by_page[page]] + ['']
    write('TRANSLATIONS_REVIEW.md', '\n'.join(out))

if __name__ == '__main__':
    build()
