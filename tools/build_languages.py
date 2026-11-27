#!/usr/bin/env python3
"""Build the translated pages (uz/, ru/) from the English pages and i18n/<lang>.json.

Usage (from the repository root, Python 3.9+, standard library only):
    python3 tools/build_languages.py            # rebuild uz/, ru/ and the language links
    python3 tools/build_languages.py --review   # also rewrite the review lists (resets their tick boxes):
                                                # TRANSLATIONS_REVIEW.md (uz), TRANSLATIONS_REVIEW_RU.md,
                                                # CLINICAL_REVIEW_UZ.md, CLINICAL_REVIEW_RU.md

What it does
- English pages at the root are the source. i18n/<lang>.json maps English text to that language. It is the only
  place translations live: edit it, never the generated pages.
- Text nodes and the alt, aria-label, placeholder and title attributes are translated as whole text nodes,
  whitespace collapsed, HTML entities decoded.
- Anything without a translation stays in English and is listed in i18n/missing-<lang>.txt. Nothing is guessed.
- Every page gets its own <html lang>, title, description, canonical URL and Open Graph tags.
- Each language link becomes a set (EN, UZ, RU) pointing to the same page in every language, the current one
  marked aria-current. The header shows short codes; the menu and footer show the names.

Publishing
- PUBLISH[lang] = False while a language is a draft: its pages are noindex, stay out of sitemap.xml, and no
  hreflang links point to it. Set it True only after that language's native and clinical review.
"""
import html, json, os, re, sys

# Per language: True only after its native and clinical review. Unpublished pages are noindex, stay out of
# sitemap.xml and get no hreflang.
PUBLISH = {'uz': False, 'ru': False}
SITE = 'https://coriva.uz'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# code: (Open Graph locale, name in its own language, short code shown in the header)
LANGS = {'en': ('en_US', 'English', 'EN'), 'uz': ('uz_UZ', 'O‘zbekcha', 'UZ'), 'ru': ('ru_RU', 'Русский', 'RU')}
TRANSLATED = ('uz', 'ru')
LANG = 'uz'   # the language being built; set by build()
ATTRS = ('alt', 'aria-label', 'placeholder', 'title')
# Text that scripts write at run time (live.js, r7.js). Translated pages carry these in window.__CORIVA_T.
SCRIPT_STRINGS = ('Play video', 'Pause video', 'Previous moment', 'Next moment', 'Every heartbeat matters.', 'Close menu')

def read(p): return open(os.path.join(ROOT, p), encoding='utf-8').read()
def write(p, t):
    p = os.path.join(ROOT, p); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(t)

DICTS = {l: json.loads(read(f'i18n/{l}.json')) for l in TRANSLATED}
UZ = DICTS['uz']   # the dictionary of the language being built; set by build()
norm = lambda s: re.sub(r'\s+', ' ', html.unescape(s)).strip()
PAGES = sorted(f[:-5] for f in os.listdir(ROOT) if f.endswith('.html'))
url = lambda lang, page: SITE + ('/' if lang == 'en' else f'/{lang}/') + ('' if page == 'index' else page)
MISSING = {l: {} for l in TRANSLATED}   # per language: page -> ordered set of English strings without a translation
USED = {l: {} for l in TRANSLATED}      # per language: English string -> (translation, first page)
missing, used = MISSING['uz'], USED['uz']
SKIP = {v[1] for v in LANGS.values()} | {v[2] for v in LANGS.values()}   # language names, and headline words written by split_headlines()
published = lambda lang: lang == 'en' or PUBLISH.get(lang, False)

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

def lang_links(t, page, cur):
    """Replace each language link (a single <a lang=".."> in the English source, or a set written by an earlier
    run) with a set linking the same page in every language; the page's own language is marked aria-current.
    The header (class lang-inline) shows short codes with the full name as the accessible name."""
    def fix(m):
        first = re.search(r'<a((?:\s[^>]*)?)>', m.group(0)).group(1)
        attrs = re.sub(r'\s(?:href|lang|hreflang|role|aria-current|aria-label|title)="[^"]*"', '', first)
        short = 'lang-inline' in attrs
        out = []
        for l, (_, name, code) in LANGS.items():
            label = f' aria-label="{name}" title="{name}"' if short else ''
            mark = ' aria-current="true"' if l == cur else ''
            out.append(f'<a{attrs} href="{page_url(l, page)}" lang="{l}" hreflang="{l}"{label}{mark}>{code if short else name}</a>')
        return '<span class="lang-set">' + ''.join(out) + '</span>'
    return re.sub(r'<span class="lang-set">.*?</span>|<a(?:\s[^>]*)?\slang="[a-z]{2}"[^>]*>[^<]*</a>', fix, t, flags=re.S)

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

def page_url(lang, page):
    """Clean root-relative address of a page, as in sitemap.xml: / or /platform, /uz/ or /uz/platform."""
    return ('/' if lang == 'en' else f'/{lang}/') + ('' if page == 'index' else page)

def page_link(v):
    """(page, '#fragment') if v links to one of the site's pages, in any form the English pages use:
    ./  /  index.html  platform.html  /platform  (each with or without #fragment). Otherwise None."""
    m = re.fullmatch(r'(?:\./|/)(#.*)?', v)
    if m: return 'index', m.group(1) or ''
    m = re.fullmatch(r'(/)?([\w-]+)(\.html)?(#.*)?', v)
    if m and (m.group(1) or m.group(3)) and m.group(2) in PAGES: return m.group(2), m.group(4) or ''
    return None

def rebase_assets(t):
    """Translated pages live one folder down: assets move to ../, links between pages go to the same language."""
    def one(v):
        link = page_link(v)
        if link: return page_url(LANG, link[0]) + link[1]
        if v.startswith(('http:', 'https:', '//', '/', '#', 'mailto:', 'tel:', 'data:', '../')): return v
        return '../' + v
    t = re.sub(r'(\s(?:src|href|poster))="([^"]*)"', lambda m: f'{m.group(1)}="{one(m.group(2))}"', t)
    return re.sub(r'(\ssrcset)="([^"]*)"', lambda m: m.group(1) + '="' + ', '.join(' '.join([one(p.split()[0])] + p.split()[1:]) for p in m.group(2).split(',')) + '"', t)

def head(t, page, lang):
    """lang, canonical, Open Graph, robots and (once published) hreflang for one page."""
    t = re.sub(r'<html lang="[a-z]{2}"', f'<html lang="{lang}"', t, count=1)
    t = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url(lang, page)}">', t, count=1)
    t = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url(lang, page)}">', t, count=1)
    t = re.sub(r'\n<meta property="og:locale"[^>]*>', '', t)
    t = t.replace('<meta property="og:type"', f'<meta property="og:locale" content="{LANGS[lang][0]}">\n<meta property="og:type"', 1)
    t = re.sub(r'\n<link rel="alternate" hreflang="[^"]*" href="[^"]*">', '', t)
    live = [l for l in LANGS if published(l)]
    if len(live) > 1 and published(lang) and page not in ('404',) and 'noindex' not in read(page + '.html'):
        alts = ''.join(f'\n<link rel="alternate" hreflang="{l}" href="{url(l, page)}">' for l in live) + f'\n<link rel="alternate" hreflang="x-default" href="{url("en", page)}">'
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
    global LANG, UZ, missing, used
    english = {}
    for page in PAGES:
        en = read(page + '.html')
        en = re.sub(r'\n?<script src="i18n\.js[^"]*"[^>]*></script>', '', en)   # static pages replace the toggle
        en = lang_links(en, page, 'en')
        en = head(en, page, 'en')
        write(page + '.html', en); english[page] = en
    for LANG in TRANSLATED:
        UZ, missing, used = DICTS[LANG], MISSING[LANG], USED[LANG]
        build_language(english)
    sitemap()
    if '--review' in sys.argv:
        for LANG in TRANSLATED:
            UZ, missing, used = DICTS[LANG], MISSING[LANG], USED[LANG]
            review()
    for l in TRANSLATED:
        print(f'{len(PAGES)} pages -> {l}/, {len(USED[l])} strings translated, {sum(len(v) for v in MISSING[l].values())} missing (i18n/missing-{l}.txt), published={PUBLISH[l]}')

def build_language(english):
    """One translated language (LANG, with UZ as its dictionary) for every page."""
    for page in PAGES:
        uz = english[page]
        uz = re.sub(r'\n?<script type="application/ld\+json">.*?</script>', '', uz, flags=re.S)
        uz = translate_head(uz, page)
        uz = head(uz, page, LANG)
        table = {}
        for s in SCRIPT_STRINGS:
            u = tr(s, '(scripts, every page)', 'script')
            if u: table[s] = u
        uz = uz.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<script>window.__CORIVA_T = ' + json.dumps(table, ensure_ascii=False) + ';</script>', 1)
        if not PUBLISH[LANG]: uz = re.sub(r'<meta name="robots" content="[^"]*">', '<meta name="robots" content="noindex, follow">', uz, count=1)
        i = uz.index('<body'); b = split_headlines(uz[i:], page); b = translate_body(b, page)
        uz = presplit_h1(uz[:i] + b)
        uz = rebase_assets(uz)
        uz = lang_links(uz, page, LANG)
        write(f'{LANG}/{page}.html', f'<!-- Generated by tools/build_languages.py from ../{page}.html and i18n/{LANG}.json. Do not edit. -->\n' + uz)
    lines = [f'# English strings with no {LANGS[LANG][1]} translation (generated; {sum(len(v) for v in missing.values())} entries)', f'# Add them to i18n/{LANG}.json, then re-run tools/build_languages.py.', '']
    for page in PAGES:
        if page in missing: lines += [f'## {page}.html'] + [f'- {k}' for k in missing[page]] + ['']
    if '(scripts, every page)' in missing: lines += ['## live.js, r7.js (every page)'] + [f'- {k}' for k in missing['(scripts, every page)']] + ['']
    write(f'i18n/missing-{LANG}.txt', '\n'.join(lines))

def sitemap():
    sm = read('sitemap.xml'); locs = re.findall(r'<url><loc>([^<]+)</loc>', sm)
    lastmod = (re.search(r'<lastmod>([^<]+)</lastmod>', sm) or [None, ''])[1]
    pages = [p for loc in locs for p in PAGES if url('en', p) == loc]   # keep the existing order
    rows = []
    for p in pages:
        live = [l for l in LANGS if published(l)]
        for lang in live:
            alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{url(l, p)}"/>' for l in live) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{url("en", p)}"/>' if len(live) > 1 else ''
            rows.append(f'  <url><loc>{url(lang, p)}</loc>' + (f'<lastmod>{lastmod}</lastmod>' if lastmod else '') + alts + '</url>')
    ns = ' xmlns:xhtml="http://www.w3.org/1999/xhtml"' if len([l for l in LANGS if published(l)]) > 1 else ''
    write('sitemap.xml', f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"{ns}>\n' + '\n'.join(rows) + '\n</urlset>\n')

ENGLISH_NAME = {'uz': 'Uzbek (Latin)', 'ru': 'Russian'}
SEARCH_TERMS = {
    'uz': ['- [ ] Home title is "Coriva · Yurak reabilitatsiyasi uyda davom etadi". Keep "yurak reabilitatsiyasi", or prefer "kardioreabilitatsiya"?',
           '- [ ] Home description: add "kardioreabilitatsiya" if it reads naturally, e.g. in the sentence that already says "platforma".',
           '- [ ] Partners heading "Yurak reabilitatsiyasi uchun yagona tizim." uses the same term: keep both pages consistent.'],
    'ru': ['- [ ] Home title uses «Кардиореабилитация». Keep it (the term people search for), or prefer «реабилитация сердца»?',
           '- [ ] Where the English says "cardiac rehabilitation", use «кардиореабилитация» consistently across pages.'],
}

def review():
    """TRANSLATIONS_REVIEW[_RU].md (every string) and CLINICAL_REVIEW_<LANG>.md (the ⚕ lines) for LANG."""
    suffix = '' if LANG == 'uz' else '_' + LANG.upper()
    out = ['# Translation review', '', f'{ENGLISH_NAME[LANG]}: **draft, needs native and clinical review.** The {LANG}/ pages stay `noindex` until every box is ticked',
           f"and the owner confirms; then set `PUBLISH['{LANG}'] = True` in tools/build_languages.py and re-run it.", '',
           f'Fix a translation in `i18n/{LANG}.json`, never in {LANG}/. Strings marked ⚕ make a clinical or safety statement: they need a clinician as well as a native reader.', '',
           f'Untranslated strings: see `i18n/missing-{LANG}.txt`.', '']
    out += ['## Search terms (proposal, for the reviewer to accept or reject)', '',
            'Use these only where the page already says the same thing in English. No new claims.', ''] + SEARCH_TERMS[LANG] + ['']
    # ⚕ = a clinical or safety statement a cardiologist should read: medicine, emergencies, AI, approvals,
    # decisions, activity guidance, monitoring and handover. Labels like "Doctors" are not statements, so
    # most topics need four words or more; the strongest topics are flagged at any length.
    STRONG = re.compile(r'(?i)emergenc|unwell|diagnos|prescri|medic(?:ation|ine|al)|treatment|threshold')
    TOPIC = re.compile(r'(?i)approv|heart|safety|risk|clinical|decid|decision|\bAI\b|research|papers?\b|sources?\b|'
                       r'reports? wait|real time|watch|walk|exercise|activity|pace\b|days a week|look after|take[s]? over')
    clin = lambda en: bool(STRONG.search(en)) or (bool(TOPIC.search(en)) and len(en.split()) >= 4)
    by_page = {}
    for en, (u, page) in used.items(): by_page.setdefault(page, []).append((en, u))
    for page in PAGES:
        if page not in by_page: continue
        out += [f'## {page}.html', '', f'| ✓ | English | {ENGLISH_NAME[LANG]} |', '|---|---|---|']
        out += [f'| ☐{" ⚕" if clin(en) else ""} | {en.replace("|", "\\|")} | {u.replace("|", "\\|")} |' for en, u in by_page[page]] + ['']
    write(f'TRANSLATIONS_REVIEW{suffix}.md', '\n'.join(out))
    # The ⚕ lines alone, for the cardiologist: each once, grouped by the page where it first appears
    rows = [(page, en, u) for page in PAGES for en, u in by_page.get(page, []) if clin(en)]
    cl = [f'# Clinical review: {ENGLISH_NAME[LANG]} text on coriva.uz', '',
          f'{len(rows)} lines that make a clinical or safety statement. Please check that each {ENGLISH_NAME[LANG]} line says the same as',
          'the English, is medically correct and could not be misread by a patient. Tick the box, or write the',
          'correction in the last column. Lines that name 103 are a deliberate localisation (owner, 2026-11-27).', '',
          'Generated by tools/build_languages.py --review from i18n/uz.json. Do not edit the translations here.', '']
    for page in PAGES:
        mine = [(en, u) for pg, en, u in rows if pg == page]
        if not mine: continue
        cl += [f'## {page}', '', f'| ✓ | English | {ENGLISH_NAME[LANG]} | Correction |', '|---|---|---|---|']
        cl += [f'| ☐ | {en.replace("|", "\\|")} | {u.replace("|", "\\|")} | |' for en, u in mine] + ['']
    write(f'CLINICAL_REVIEW_{LANG.upper()}.md', '\n'.join(cl))

if __name__ == '__main__':
    build()
