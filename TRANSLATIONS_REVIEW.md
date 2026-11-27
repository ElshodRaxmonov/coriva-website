# Translation review

Uzbek (Latin): **draft, needs native and clinical review.** The uz/ pages stay `noindex` until every box is ticked
and the owner confirms; then set `PUBLISH = True` in tools/build_languages.py and re-run it.

Fix a translation in `i18n/uz.json`, never in uz/. Strings marked ⚕ make a clinical or safety statement: they need a clinician as well as a native reader.

Untranslated strings: see `i18n/missing-uz.txt`.

## Search terms (proposal, for the reviewer to accept or reject)

Use these only where the page already says the same thing in English. No new claims.

- [ ] Home title is "Coriva · Yurak reabilitatsiyasi uyda davom etadi". Keep "yurak reabilitatsiyasi", or prefer "kardioreabilitatsiya"?
- [ ] Home description: add "kardioreabilitatsiya" if it reads naturally, e.g. in the sentence that already says "platforma".
- [ ] Partners heading "Yurak reabilitatsiyasi uchun yagona tizim." uses the same term: keep both pages consistent.

## 404.html

| ✓ | English | Uzbek |
|---|---|---|
| ☐ ⚕ | Skip to main content | Asosiy mazmunga o‘tish |
| ☐ | Primary | Asosiy |
| ☐ | Platform | Platforma |
| ☐ ⚕ | Doctors | Shifokorlar |
| ☐ ⚕ | Clinics | Klinikalar |
| ☐ ⚕ | Patients | Bemorlar |
| ☐ | Partners | Hamkorlar |
| ☐ ⚕ | Join the pilot waitlist | Kutish ro‘yxatiga qo‘shilish |
| ☐ ⚕ | Join waitlist | Qo‘shilish |
| ☐ | Menu | Menyu |
| ☐ | Error 404 | 404 xatosi |
| ☐ | This page doesn't exist. | Bunday sahifa yo‘q. |
| ☐ | The link may be old or mistyped. | Havola eskirgan yoki noto‘g‘ri yozilgan bo‘lishi mumkin. |
| ☐ | Go to the home page | Bosh sahifaga o‘tish |
| ☐ | How Coriva works | Coriva qanday ishlaydi |
| ☐ | Company | Kompaniya |
| ☐ | Partners and investors | Hamkorlar va investorlar |
| ☐ | Contact | Aloqa |
| ☐ | Legal | Huquqiy ma’lumot |
| ☐ | Privacy notice | Maxfiylik bildirishnomasi |
| ☐ ⚕ | Medical disclaimer | Tibbiy ogohlantirish |
| ☐ ⚕ | Coriva is not an emergency service. If you feel unwell, call your local emergency number. | Coriva tez yordam xizmati emas. O‘zingizni yomon his qilsangiz, tez yordam raqamiga qo‘ng‘iroq qiling. |

## clinics.html

| ✓ | English | Uzbek |
|---|---|---|
| ☐ ⚕ | For clinics | Klinikalar uchun |
| ☐ ⚕ | Coriva is being built with clinics for the pilot: your doctors, their patients and care handover in one place, with clear roles and your data kept apart from other clinics. | Coriva pilot loyiha uchun klinikalar bilan birga yaratilmoqda: shifokorlaringiz, ularning bemorlari va bemorni topshirish bir joyda, rollar aniq, ma’lumotlaringiz esa boshqa klinikalardan alohida saqlanadi. |
| ☐ ⚕ | Coordinate rehabilitation across your team. | Reabilitatsiyani butun jamoangiz bilan muvofiqlashtiring. |
| ☐ ⚕ | Join as a clinic | Klinika sifatida qo‘shilish |
| ☐ | Coordination | Muvofiqlashtirish |
| ☐ ⚕ | What your clinic will use, and its status today. | Klinikangiz nimalardan foydalanadi va ularning bugungi holati. |
| ☐ | Your team in one view | Jamoangiz — bir ko‘rinishda |
| ☐ ⚕ | Who each doctor is caring for, inside the doctor’s dashboard. | Har bir shifokor kimlarga qarayotgani — shifokor panelining ichida. |
| ☐ | Pilot | Pilot |
| ☐ ⚕ | clinic screens | klinika ekranlari |
| ☐ | Care handover | Bemorni topshirish |
| ☐ ⚕ | When a doctor is away, a colleague takes over, and the handover is recorded. | Shifokor ishda bo‘lmasa, bemorni hamkasbi qabul qilib oladi va topshirish qayd etiladi. |
| ☐ | In development | Ishlab chiqilmoqda |
| ☐ | backend built | tizim tayyor |
| ☐ ⚕ | Activation in your clinic | Klinikangizda faollashtirish |
| ☐ ⚕ | Patients activate the app at your clinic, with staff present, using a single-use code. | Bemorlar ilovani klinikangizda, xodimlar ishtirokida, bir martalik kod bilan faollashtiradi. |
| ☐ | Who can do what | Kim nima qila oladi |
| ☐ | Roles are enforced by the system, not only hidden in the screens. | Rollar tizimning o‘zida ta’minlanadi, shunchaki ekranda yashirib qo‘yilmaydi. |
| ☐ ⚕ | Clinic leader | Klinika rahbari |
| ☐ | Can | Qila oladi |
| ☐ ⚕ | Manages members and roles. Reassigns care inside the clinic. | A’zolar va rollarni boshqaradi. Klinika ichida bemorlarni qayta biriktiradi. |
| ☐ | Cannot | Qila olmaydi |
| ☐ ⚕ | Does not see patients' clinical records. | Bemorlarning klinik yozuvlarini ko‘rmaydi. |
| ☐ ⚕ | Doctor | Shifokor |
| ☐ ⚕ | Cares for their own patients: approves programs and reviews reports. | O‘z bemorlariga qaraydi: dasturlarni tasdiqlaydi va hisobotlarni ko‘rib chiqadi. |
| ☐ ⚕ | Does not see patients outside their care. | O‘z qaramog‘idan tashqaridagi bemorlarni ko‘rmaydi. |
| ☐ ⚕ | Patient | Bemor |
| ☐ ⚕ | Follows the plan their doctor approved and reports progress. | Shifokori tasdiqlagan rejaga amal qiladi va natijalar haqida xabar beradi. |
| ☐ ⚕ | Cannot change their plan or medication. | Rejasini yoki dorilarini o‘zgartira olmaydi. |
| ☐ | Oversight and data | Nazorat va ma’lumotlar |
| ☐ ⚕ | Clinical decisions stay with each patient's doctor. | Klinik qarorlar har bir bemorning shifokorida qoladi. |
| ☐ | Handovers and other sensitive actions are recorded. | Topshirishlar va boshqa muhim amallar qayd etiladi. |
| ☐ ⚕ | AI drafts go only to doctors, never to patients directly. | Sun’iy intellekt qoralamalari faqat shifokorlarga boradi, bemorlarga to‘g‘ridan-to‘g‘ri hech qachon yuborilmaydi. |
| ☐ ⚕ | Each clinic's data is kept apart, enforced in the database. | Har bir klinikaning ma’lumotlari alohida saqlanadi — bu ma’lumotlar bazasi darajasida ta’minlangan. |
| ☐ | foundation built | asos tayyor |
| ☐ | Where data is stored: to be confirmed before the pilot. | Ma’lumotlar qayerda saqlanishi pilot loyihadan oldin aniqlanadi. |
| ☐ | Development uses synthetic data only. | Ishlab chiqishda faqat sun’iy (namunaviy) ma’lumotlar ishlatiladi. |
| ☐ ⚕ | Questions from clinics | Klinikalarning savollari |
| ☐ ⚕ | Can our clinic join the pilot? | Klinikamiz pilot loyihaga qo‘shila oladimi? |
| ☐ ⚕ | Register your interest on the waitlist with the role "Clinic". The pilot is in preparation with selected doctors and clinics; we contact you about it. | Kutish ro‘yxatida “Klinika” rolini tanlab, qiziqishingizni bildiring. Pilot loyiha tanlangan shifokorlar va klinikalar bilan tayyorlanmoqda; bu bo‘yicha siz bilan bog‘lanamiz. |
| ☐ ⚕ | Can clinic leaders see patients' records? | Klinika rahbarlari bemorlarning yozuvlarini ko‘ra oladimi? |
| ☐ ⚕ | No. Clinic leaders manage the team and care assignments. Clinical records stay with each patient's doctor. | Yo‘q. Klinika rahbarlari jamoani va bemorlarning biriktirilishini boshqaradi. Klinik yozuvlar har bir bemorning shifokorida qoladi. |
| ☐ | Where is our data stored? | Ma’lumotlarimiz qayerda saqlanadi? |
| ☐ | To be confirmed before the pilot. We will state it on this page and in the privacy notice. | Pilot loyihadan oldin aniqlanadi. Buni shu sahifada va maxfiylik bildirishnomasida ko‘rsatamiz. |
| ☐ ⚕ | What happens when a doctor is away? | Shifokor ishda bo‘lmasa, nima bo‘ladi? |
| ☐ ⚕ | Care can pass to a colleague in the same clinic. The handover is recorded. | Bemorni shu klinikadagi hamkasbga topshirish mumkin. Topshirish qayd etiladi. |
| ☐ ⚕ | How do patients join? | Bemorlar qanday qo‘shiladi? |
| ☐ ⚕ | Through their doctor. The doctor invites the patient; during the pilot, the app is activated at the clinic with staff present. There is no self sign-up. | Shifokori orqali. Bemorni shifokor taklif qiladi; pilot loyiha davomida ilova klinikada, xodimlar ishtirokida faollashtiriladi. O‘zi ro‘yxatdan o‘tish yo‘q. |
| ☐ | Bring your team to the pilot. | Jamoangizni pilot loyihaga olib keling. |
| ☐ ⚕ | Join the waitlist as a clinic. We'll contact you about the pilot. | Klinika sifatida kutish ro‘yxatiga qo‘shiling. Pilot loyiha bo‘yicha siz bilan bog‘lanamiz. |
| ☐ | Photograph: Jacek Halicki (CC BY-SA 4.0), via Wikimedia Commons. | Surat: Jacek Halicki (CC BY-SA 4.0), Wikimedia Commons orqali. |

## contact.html

| ✓ | English | Uzbek |
|---|---|---|
| ☐ | Contact the team. | Jamoa bilan bog‘laning. |
| ☐ | For partnerships, investment and other questions about Coriva. | Hamkorlik, investitsiya va Coriva haqidagi boshqa savollar uchun. |
| ☐ | Write to us | Bizga yozing |
| ☐ | Use the form, or write to | Shakldan foydalaning yoki shu manzilga yozing: |
| ☐ ⚕ | Are you a patient? | Siz bemormisiz? |
| ☐ ⚕ | Please talk to your doctor about your care. Do not send health information here. If you feel unwell, call your local emergency number. | Davolanishingiz haqida shifokoringiz bilan gaplashing. Bu yerga sog‘liqqa oid ma’lumot yubormang. O‘zingizni yomon his qilsangiz, tez yordam raqamiga qo‘ng‘iroq qiling. |
| ☐ ⚕ | Pilot waitlist | Pilot loyihaning kutish ro‘yxati |
| ☐ | The contact form opens soon. | Aloqa shakli tez orada ochiladi. |
| ☐ | Until then, write to us: | Ungacha bizga yozing: |
| ☐ | All fields are required unless marked optional. | Ixtiyoriy deb belgilanmagan barcha maydonlar to‘ldirilishi shart. |
| ☐ | I am | Men — |
| ☐ ⚕ | Cardiologist | Kardiolog |
| ☐ ⚕ | Clinic or department | Klinika yoki bo‘lim |
| ☐ | Partner or investor | Hamkor yoki investor |
| ☐ | Other | Boshqa |
| ☐ | Full name | Ism-familiya |
| ☐ ⚕ | Work email | Ish elektron pochtasi |
| ☐ ⚕ | We send one email to confirm it. | Tasdiqlash uchun bitta xat yuboramiz. |
| ☐ | Organisation | Tashkilot |
| ☐ | (optional for Other) | (“Boshqa” uchun ixtiyoriy) |
| ☐ | Country | Mamlakat |
| ☐ | Choose a country | Mamlakatni tanlang |
| ☐ | Uzbekistan | O‘zbekiston |
| ☐ | Kazakhstan | Qozog‘iston |
| ☐ | Kyrgyzstan | Qirg‘iziston |
| ☐ | Tajikistan | Tojikiston |
| ☐ | Turkmenistan | Turkmaniston |
| ☐ | Russia | Rossiya |
| ☐ | Germany | Germaniya |
| ☐ | United Kingdom | Buyuk Britaniya |
| ☐ | United States | AQSH |
| ☐ | Message | Xabar |
| ☐ | (optional) | (ixtiyoriy) |
| ☐ | Do not include health information about yourself or anyone else. Up to 1,000 characters. | O‘zingiz yoki boshqa birov haqida sog‘liqqa oid ma’lumot yozmang. 1 000 belgigacha. |
| ☐ | I have read the | Men |
| ☐ | privacy notice | maxfiylik bildirishnomasi |
| ☐ ⚕ | and agree that Coriva uses these details to contact me about my message. | bilan tanishdim hamda Coriva ushbu ma’lumotlardan xabarim bo‘yicha men bilan bog‘lanish uchun foydalanishiga roziman. |
| ☐ | Website | Veb-sayt |
| ☐ | Send message | Xabar yuborish |
| ☐ | The form is a design: it is not connected and sends nothing. | Bu shakl — dizayn namunasi: u ulanmagan va hech narsa yubormaydi. |

## doctors.html

| ✓ | English | Uzbek |
|---|---|---|
| ☐ ⚕ | For cardiologists | Kardiologlar uchun |
| ☐ ⚕ | Supervise rehabilitation beyond discharge. | Reabilitatsiyani shifoxonadan keyin ham nazorat qiling. |
| ☐ ⚕ | Coriva is being built so your patients can continue cardiac rehabilitation at home, on the plan you approve. You decide. AI helps you prepare. | Coriva bemorlaringiz siz tasdiqlagan reja bo‘yicha yurak reabilitatsiyasini uyda davom ettira olishi uchun yaratilmoqda. Qarorni siz qabul qilasiz. Sun’iy intellekt tayyorlashga yordam beradi. |
| ☐ | Pilot in preparation | Pilot loyiha tayyorlanmoqda |
| ☐ ⚕ | Join as a cardiologist | Kardiolog sifatida qo‘shilish |
| ☐ | What you would do | Siz nima qilasiz |
| ☐ | Your part | Sizning vazifangiz |
| ☐ | Three things you do in Coriva. Everything else supports them. | Coriva’da siz uch ishni bajarasiz. Qolgan hammasi shularga xizmat qiladi. |
| ☐ | Invite | Taklif qilish |
| ☐ ⚕ | You invite a patient. They activate the app in your clinic, with staff present, using a single-use code. | Bemorni taklif qilasiz. U ilovani klinikangizda, xodimlar ishtirokida, bir martalik kod bilan faollashtiradi. |
| ☐ ⚕ | Plan and approve | Rejalashtirish va tasdiqlash |
| ☐ ⚕ | Write a program, or start from an AI draft built from approved research. You edit it and approve it. Nothing reaches the patient before that. | Dasturni o‘zingiz yozing yoki tasdiqlangan tadqiqotlar asosida tayyorlangan sun’iy intellekt qoralamasidan boshlang. Uni tahrirlaysiz va tasdiqlaysiz. Ungacha bemorga hech narsa yetib bormaydi. |
| ☐ | Review | Ko‘rib chiqish |
| ☐ ⚕ | See the patients who need a decision or sent a report. Reports wait for your review. | Qaror kutayotgan yoki hisobot yuborgan bemorlarni ko‘ring. Hisobotlar ko‘rib chiqishingizni kutadi. |
| ☐ | dashboard | panel |
| ☐ | reports | hisobotlar |
| ☐ ⚕ | Your patients | Bemorlaringiz |
| ☐ | In development · demo data | Ishlab chiqilmoqda · namunaviy ma’lumotlar |
| ☐ ⚕ | 3 patients need you today | Bugun 3 bemor sizni kutmoqda |
| ☐ | Bekzod T. | Bekzod T. |
| ☐ ⚕ | Program draft waits for your approval | Dastur qoralamasi tasdig‘ingizni kutmoqda |
| ☐ ⚕ | AI suggestion, not reviewed | Sun’iy intellekt taklifi, ko‘rib chiqilmagan |
| ☐ | Walking, 5 days a week | Sayr, haftasiga 5 kun |
| ☐ ⚕ | Edited by you · source: approved paper, section 4 | Siz tahrirlagansiz · manba: tasdiqlangan maqola, 4-bo‘lim |
| ☐ ⚕ | Approve | Tasdiqlash |
| ☐ | Reject | Rad etish |
| ☐ | Lola M. | Lola M. |
| ☐ | New report | Yangi hisobot |
| ☐ ⚕ | Patient-reported | Bemor yuborgan |
| ☐ | Dilnoza R. | Dilnoza R. |
| ☐ | Follow-up this week | Shu hafta navbatdagi ko‘rik |
| ☐ | Scheduled by you | Siz belgilagansiz |
| ☐ ⚕ | Example of the doctor's dashboard with demo data: three patients need you today; a program draft waits for your approval (step 2), marked as an AI suggestion; a new patient-reported report (step 3); a follow-up this week. | Namunaviy ma’lumotlar bilan shifokor paneli misoli: bugun uch bemor sizni kutmoqda; dastur qoralamasi tasdig‘ingizni kutmoqda (2-qadam), u sun’iy intellekt taklifi deb belgilangan; bemor yuborgan yangi hisobot (3-qadam); shu hafta navbatdagi ko‘rik. |
| ☐ ⚕ | What the AI does, and never does | Sun’iy intellekt nima qiladi va hech qachon nima qilmaydi |
| ☐ ⚕ | Rehabilitation intelligence is in research for the pilot. | Reabilitatsiya uchun sun’iy intellekt pilot loyihaga qadar tadqiq qilinmoqda. |
| ☐ | research in progress | tadqiqot bosqichida |
| ☐ | It does | Nima qiladi |
| ☐ ⚕ | Drafts rehabilitation guidance from research papers the team has approved | Jamoa tasdiqlagan ilmiy maqolalar asosida reabilitatsiya tavsiyalarini tayyorlaydi |
| ☐ | Shows the source of every point: paper, page or section | Har bir band manbasini ko‘rsatadi: maqola, sahifa yoki bo‘lim |
| ☐ | Says so when the papers don't cover a question | Maqolalarda javob bo‘lmasa, buni aytadi |
| ☐ ⚕ | Marks every draft as a suggestion, kept apart from approved care | Har bir qoralamani taklif deb belgilaydi va tasdiqlangan rejadan alohida saqlaydi |
| ☐ | It never | Hech qachon |
| ☐ ⚕ | Diagnoses | Tashxis qo‘yadi |
| ☐ ⚕ | Prescribes or changes medication | Dori yozadi yoki o‘zgartiradi |
| ☐ ⚕ | Approves a program | Dasturni tasdiqlaydi |
| ☐ ⚕ | Sends anything to a patient without you | Sizsiz bemorga biror narsa yuboradi |
| ☐ | Workload, responsibility and data | Ish hajmi, mas’uliyat va ma’lumotlar |
| ☐ | Your workload | Ish hajmingiz |
| ☐ ⚕ | Coriva is being built to show only what needs you: patients who need a decision or sent a report. We won't promise time saved. That is one of the questions the pilot will answer. | Coriva faqat sizning e’tiboringiz kerak bo‘lgan narsani ko‘rsatish uchun yaratilmoqda: qaror kutayotgan yoki hisobot yuborgan bemorlar. Vaqt tejalishini va’da qilmaymiz. Bu pilot loyiha javob beradigan savollardan biri. |
| ☐ | Responsibility | Mas’uliyat |
| ☐ ⚕ | Clinical decisions stay yours, as today. Coriva will keep a record of what you approve and when, and patient reports will be marked as patient-reported, not clinical records. The pilot terms will be reviewed by lawyers before the pilot starts. | Klinik qarorlar, hozirgidek, sizda qoladi. Coriva nimani va qachon tasdiqlaganingizni qayd etib boradi, bemor hisobotlari esa klinik yozuv emas, “bemor yuborgan” deb belgilanadi. Pilot loyiha shartlari boshlanishidan oldin yuristlar tomonidan ko‘rib chiqiladi. |
| ☐ ⚕ | Your patients’ data | Bemorlaringiz ma’lumotlari |
| ☐ ⚕ | Each clinic's data is kept apart, access is by role, and development uses synthetic data only. An independent security review comes before the pilot. | Har bir klinikaning ma’lumotlari alohida saqlanadi, kirish rol bo‘yicha beriladi, ishlab chiqishda esa faqat namunaviy ma’lumotlar ishlatiladi. Pilot loyihadan oldin mustaqil xavfsizlik tekshiruvi o‘tkaziladi. |
| ☐ | How Coriva works: every part and its status | Coriva qanday ishlaydi: har bir qism va uning holati |
| ☐ ⚕ | Questions from cardiologists | Kardiologlarning savollari |
| ☐ ⚕ | Is Coriva available now? | Coriva hozir ishlayaptimi? |
| ☐ ⚕ | Not yet. Coriva is in development, and a pilot with selected doctors and clinics is in preparation. | Hali yo‘q. Coriva ishlab chiqilmoqda, tanlangan shifokorlar va klinikalar bilan pilot loyiha tayyorlanmoqda. |
| ☐ ⚕ | Which research does the AI use? | Sun’iy intellekt qaysi tadqiqotlardan foydalanadi? |
| ☐ ⚕ | Only research papers the team has approved. Every suggestion shows its source, and the AI says so when the papers don't cover a question. | Faqat jamoa tasdiqlagan ilmiy maqolalar. Har bir taklif o‘z manbasini ko‘rsatadi, maqolalarda javob bo‘lmasa, sun’iy intellekt buni ochiq aytadi. |
| ☐ ⚕ | What happens if a patient feels unwell? | Bemor o‘zini yomon his qilsa, nima bo‘ladi? |
| ☐ ⚕ | Coriva is not an emergency service. Patients are told to call their local emergency number. Their reports wait for your next review. | Coriva tez yordam xizmati emas. Bemorlarga tez yordam raqamiga qo‘ng‘iroq qilish aytiladi. Ularning hisobotlari navbatdagi ko‘rib chiqishingizni kutadi. |
| ☐ ⚕ | How do my patients join? | Bemorlarim qanday qo‘shiladi? |
| ☐ ⚕ | Through you. You invite the patient; during the pilot, the app is activated at the clinic with staff present. There is no self sign-up. | Siz orqali. Bemorni siz taklif qilasiz; pilot loyiha davomida ilova klinikada, xodimlar ishtirokida faollashtiriladi. O‘zi ro‘yxatdan o‘tish yo‘q. |
| ☐ ⚕ | What does the waitlist keep about me? | Kutish ro‘yxati men haqimda nimalarni saqlaydi? |
| ☐ ⚕ | Your name, work email, role, organisation and country, used only to contact you about the pilot. The details are in the privacy notice. | Ismingiz, ish elektron pochtangiz, rolingiz, tashkilotingiz va mamlakatingiz — faqat pilot loyiha bo‘yicha siz bilan bog‘lanish uchun ishlatiladi. Batafsil ma’lumot maxfiylik bildirishnomasida. |
| ☐ | Help shape the pilot. | Pilot loyihani birga shakllantiring. |
| ☐ ⚕ | Join the waitlist as a cardiologist. We'll contact you about the pilot. | Kardiolog sifatida kutish ro‘yxatiga qo‘shiling. Pilot loyiha bo‘yicha siz bilan bog‘lanamiz. |
| ☐ | Photograph: Shixart1985 (CC BY 2.0), via Wikimedia Commons. Product screens show demo data. | Surat: Shixart1985 (CC BY 2.0), Wikimedia Commons orqali. Ekranlarda namunaviy ma’lumotlar ko‘rsatilgan. |

## index.html

| ✓ | English | Uzbek |
|---|---|---|
| ☐ ⚕ | Cardiac rehabilitation, continued at home. | Yurak reabilitatsiyasi uyda davom etadi. |
| ☐ ⚕ | A clinically supervised platform for cardiologists, clinics and their patients. The doctor approves every plan. AI helps prepare it and fit it to each patient. | Kardiologlar, klinikalar va ularning bemorlari uchun klinik nazorat ostidagi platforma. Har bir rejani shifokor tasdiqlaydi. Sun’iy intellekt uni tayyorlashga va har bir bemorga moslashga yordam beradi. |
| ☐ | A day in their shoes. | Ular o‘rnida bir kun. |
| ☐ | An older couple walking hand in hand along a path, one with a walking cane | Yo‘lakda qo‘l ushlashib ketayotgan keksa juftlik, biri hassa bilan |
| ☐ | See how it works | Qanday ishlashini ko‘rish |
| ☐ ⚕ | Choose who you are, and see what a day with Coriva will look like. Times are an example; the plan always comes from the patient's own doctor. | Kim ekaningizni tanlang va Coriva bilan bir kun qanday o‘tishini ko‘ring. Vaqtlar misol tariqasida; reja har doim bemorning o‘z shifokoridan keladi. |
| ☐ ⚕ | a cardiologist | kardiologman |
| ☐ ⚕ | a clinic leader | klinika rahbariman |
| ☐ ⚕ | a patient or family member | bemor yoki uning yaqiniman |
| ☐ | a partner or investor | hamkor yoki investorman |
| ☐ ⚕ | A doctor's day | Shifokorning kuni |
| ☐ | See who needs you | Sizni kim kutayotganini ko‘ring |
| ☐ ⚕ | Only the patients who need a decision or sent a report. | Faqat qaror kutayotgan yoki hisobot yuborgan bemorlar. |
| ☐ ⚕ | A doctor at her desk on a phone call, taking notes beside a laptop | Ish stolida telefonda gaplashayotgan va noutbuk yonida qayd yozayotgan shifokor |
| ☐ ⚕ | Three patients need you today | Bugun uch bemor sizni kutmoqda |
| ☐ ⚕ | Approve a draft | Qoralamani tasdiqlash |
| ☐ ⚕ | AI drafted it from approved research. You edit and approve. | Sun’iy intellekt uni tasdiqlangan tadqiqotlar asosida tayyorladi. Siz tahrirlaysiz va tasdiqlaysiz. |
| ☐ ⚕ | Draft plan with sources | Manbalari ko‘rsatilgan reja qoralamasi |
| ☐ ⚕ | Invite a new patient | Yangi bemorni taklif qilish |
| ☐ ⚕ | Activation happens in your clinic, with staff present. | Faollashtirish klinikangizda, xodimlar ishtirokida amalga oshadi. |
| ☐ ⚕ | Invite a patient | Bemorni taklif qilish |
| ☐ ⚕ | In the clinic, with staff present | Klinikada, xodimlar ishtirokida |
| ☐ | A report arrives | Hisobot keladi |
| ☐ ⚕ | It waits for your next review. Coriva is not an emergency service. | U navbatdagi ko‘rib chiqishingizni kutadi. Coriva tez yordam xizmati emas. |
| ☐ | New report from Lola M. | Lola M.dan yangi hisobot |
| ☐ ⚕ | A clinic leader's week | Klinika rahbarining haftasi |
| ☐ | Mon | Dushanba |
| ☐ ⚕ | See your team's patients | Jamoangiz bemorlarini ko‘ring |
| ☐ ⚕ | Who each doctor is caring for, in one view. | Har bir shifokor kimlarga qarayotgani — bir ko‘rinishda. |
| ☐ ⚕ | Cardiology team | Kardiologiya jamoasi |
| ☐ ⚕ | Three doctors, demo data | Uch shifokor, namunaviy ma’lumotlar |
| ☐ | Wed | Chorshanba |
| ☐ | Hand over care | Bemorni topshirish |
| ☐ ⚕ | When a doctor is away, another can take over, and it is recorded. | Shifokor ishda bo‘lmasa, bemorni boshqa shifokor qabul qilib oladi va bu qayd etiladi. |
| ☐ | Dr. B. Demo to Dr. A. Demo | Dr. B. Namuna → Dr. A. Namuna |
| ☐ | Thu | Payshanba |
| ☐ | Support activation | Faollashtirishda yordam |
| ☐ ⚕ | Your staff help patients activate the app, in person. | Xodimlaringiz bemorlarga ilovani faollashtirishda shaxsan yordam beradi. |
| ☐ | Activation code created | Faollashtirish kodi yaratildi |
| ☐ | With staff present | Xodimlar ishtirokida |
| ☐ | Fri | Juma |
| ☐ | Look back on the week | Haftaga nazar tashlash |
| ☐ ⚕ | Reporting for clinics comes in a later phase. | Klinikalar uchun hisobotlar keyingi bosqichda paydo bo‘ladi. |
| ☐ | Later | Keyinroq |
| ☐ ⚕ | Clinic reporting | Klinika hisobotlari |
| ☐ ⚕ | A patient's day | Bemorning kuni |
| ☐ ⚕ | Morning medication | Ertalabki dori |
| ☐ ⚕ | As your doctor entered it. Coriva never changes it. | Shifokoringiz kiritganidek. Coriva uni hech qachon o‘zgartirmaydi. |
| ☐ ⚕ | Morning medication, as entered | Ertalabki dori, shifokor kiritganidek |
| ☐ | Mark as taken | Qabul qilindi deb belgilash |
| ☐ | A walk | Sayr |
| ☐ ⚕ | As long as your plan says, at your own pace. | Rejangizda belgilangancha, o‘zingizga qulay sur’atda. |
| ☐ ⚕ | Walk, as set in your plan | Sayr, rejangizda belgilanganidek |
| ☐ | Lunch | Tushlik |
| ☐ | From your nutrition tasks. | Ovqatlanish bo‘yicha vazifalaringizdan. |
| ☐ ⚕ | Tell your doctor | Shifokoringizga xabar bering |
| ☐ ⚕ | How the day went, in a minute. If you feel unwell, call your local emergency number. | Kun qanday o‘tgani haqida — bir daqiqada. O‘zingizni yomon his qilsangiz, tez yordam raqamiga qo‘ng‘iroq qiling. |
| ☐ | How did today go? | Bugun kun qanday o‘tdi? |
| ☐ | Send report | Hisobot yuborish |
| ☐ | A partner's timeline | Hamkorning yo‘l xaritasi |
| ☐ | Now | Hozir |
| ☐ ⚕ | The doctor's dashboard, the patient app and a secure backend. | Shifokor paneli, bemor ilovasi va xavfsiz tizim. |
| ☐ | Secure backend | Xavfsiz tizim |
| ☐ ⚕ | Data separated per clinic | Ma’lumotlar klinikalar bo‘yicha ajratilgan |
| ☐ | Next | Keyingi |
| ☐ | The pilot | Pilot loyiha |
| ☐ ⚕ | Selected doctors and clinics, and what we learn with them. | Tanlangan shifokorlar va klinikalar hamda ular bilan birga o‘rgangan narsalarimiz. |
| ☐ | A small group | Kichik guruh |
| ☐ | Phase 2 | 2-bosqich |
| ☐ ⚕ | A doctors' mobile app, wearable data, clinic reporting. | Shifokorlar uchun mobil ilova, aqlli soat va fitnes-bilaguzuklar ma’lumotlari, klinika hisobotlari. |
| ☐ ⚕ | Doctors' app | Shifokorlar ilovasi |
| ☐ | Further | Kelajakda |
| ☐ | Phase 3 | 3-bosqich |
| ☐ | Validated risk intelligence and broader platform tools. | Tasdiqlangan xavfni baholash va kengroq platforma vositalari. |
| ☐ | Risk intelligence | Xavfni baholash |
| ☐ ⚕ | Validated before clinical use | Klinik qo‘llashdan oldin tasdiqlanadi |
| ☐ | A grandfather holding his young granddaughter outside a house in evening light | Kechki yorug‘likda uy oldida nabirasini ko‘tarib turgan bobo |
| ☐ | Recovery happens on ordinary days. | Sog‘ayish oddiy kunlarda kechadi. |
| ☐ ⚕ | Most of rehabilitation takes place at home. Coriva keeps those days connected to the doctor who planned them, and the patient always knows who decides. | Reabilitatsiyaning katta qismi uyda o‘tadi. Coriva shu kunlarni ularni rejalashtirgan shifokor bilan bog‘lab turadi, bemor esa qarorni kim qabul qilishini doim biladi. |
| ☐ | What Coriva will never do | Coriva hech qachon qilmaydigan ishlar |
| ☐ ⚕ | A doctor stays responsible for every clinical decision. These lines don't move. | Har bir klinik qaror uchun shifokor javobgar bo‘lib qoladi. Bu qoidalar o‘zgarmaydi. |
| ☐ ⚕ | Diagnose. | Tashxis qo‘ymaydi. |
| ☐ ⚕ | Change a medication on its own. | Dorini o‘zicha o‘zgartirmaydi. |
| ☐ ⚕ | Let AI approve a plan. | Rejani sun’iy intellekt tasdiqlashiga yo‘l qo‘ymaydi. |
| ☐ ⚕ | Pretend to be an emergency service. | O‘zini tez yordam xizmati qilib ko‘rsatmaydi. |
| ☐ | Show a number we can't stand behind. | Kafolatlay olmaydigan raqamni ko‘rsatmaydi. |
| ☐ ⚕ | If you feel unwell, call your local emergency number. | O‘zingizni yomon his qilsangiz, tez yordam raqamiga qo‘ng‘iroq qiling. |
| ☐ | Where Coriva is today | Coriva bugun qay bosqichda |
| ☐ | Demo | Namuna |
| ☐ ⚕ | Supervised activation, care relationships and clinic teams, the doctor's dashboard, the patient app's sign-in, data separated per clinic. | Nazorat ostida faollashtirish, shifokor–bemor aloqalari va klinika jamoalari, shifokor paneli, bemor ilovasiga kirish, klinikalar bo‘yicha ajratilgan ma’lumotlar. |
| ☐ ⚕ | Doctor-approved plans, medication schedules from the doctor, AI drafts for review, daily patient reports. | Shifokor tasdiqlagan rejalar, shifokor kiritgan dori jadvallari, ko‘rib chiqish uchun sun’iy intellekt qoralamalari, bemorlarning kundalik hisobotlari. |
| ☐ ⚕ | Risk intelligence (validated first), wearable data, a doctors' mobile app, clinic reporting. | Xavfni baholash (avval tasdiqlanadi), aqlli soat va fitnes-bilaguzuklar ma’lumotlari, shifokorlar uchun mobil ilova, klinika hisobotlari. |
| ☐ | For partners and investors | Hamkorlar va investorlar uchun |
| ☐ ⚕ | Coriva is building one platform for supervised cardiac rehabilitation: a doctor's dashboard, a patient app and, later, tools for clinics, all on one secure backend. The aim is rehabilitation that continues after discharge, with the doctor in charge at every step. | Coriva nazorat ostidagi yurak reabilitatsiyasi uchun yagona platforma yaratmoqda: shifokor paneli, bemor ilovasi va keyinchalik klinikalar uchun vositalar — barchasi bitta xavfsiz tizimda. Maqsad — reabilitatsiya shifoxonadan chiqqandan keyin ham davom etishi va har bir qadamda shifokor boshqarishi. |
| ☐ | Contact the team | Jamoa bilan bog‘lanish |
| ☐ ⚕ | Does it fit a cardiologist's day? | Kardiologning ish kuniga mos keladimi? |
| ☐ ⚕ | Is the plan easy to keep up at home? | Rejaga uyda amal qilish osonmi? |
| ☐ ⚕ | What should the doctor see first? | Shifokor birinchi navbatda nimani ko‘rishi kerak? |
| ☐ | Help us answer these in the pilot | Bu savollarga pilot loyihada birga javob topaylik |
| ☐ ⚕ | For cardiologists and clinics who want to supervise rehabilitation beyond discharge. No account and no commitment; we'll contact you about the pilot. Partners and investors can contact the team directly. | Reabilitatsiyani shifoxonadan keyin ham nazorat qilishni istagan kardiologlar va klinikalar uchun. Hisob ochish ham, majburiyat ham yo‘q; pilot loyiha bo‘yicha siz bilan bog‘lanamiz. Hamkorlar va investorlar jamoa bilan to‘g‘ridan-to‘g‘ri bog‘lanishi mumkin. |
| ☐ | Questions | Savollar |
| ☐ ⚕ | Does AI make clinical decisions? | Klinik qarorlarni sun’iy intellekt qabul qiladimi? |
| ☐ ⚕ | No. AI may draft suggestions from research the clinical team has approved, and shows its sources. A doctor reviews and approves every patient's plan. | Yo‘q. Sun’iy intellekt klinik jamoa tasdiqlagan tadqiqotlar asosida takliflar tayyorlashi mumkin va manbalarini ko‘rsatadi. Har bir bemorning rejasini shifokor ko‘rib chiqadi va tasdiqlaydi. |
| ☐ ⚕ | Is Coriva an emergency service? | Coriva tez yordam xizmatimi? |
| ☐ ⚕ | No. If you feel unwell, call your local emergency number. | Yo‘q. O‘zingizni yomon his qilsangiz, tez yordam raqamiga qo‘ng‘iroq qiling. |
| ☐ | Photographs: bluesbby, Shixart1985 (CC BY 2.0), via Wikimedia Commons | Suratlar: bluesbby, Shixart1985 (CC BY 2.0), Wikimedia Commons orqali |

## medical-disclaimer.html

| ✓ | English | Uzbek |
|---|---|---|
| ☐ | Draft, pending legal review. | Qoralama, yuridik ko‘rikdan o‘tmagan. |
| ☐ | Legal pages | Huquqiy sahifalar |
| ☐ | On this page | Ushbu sahifada |
| ☐ | Legal pages: draft, pending legal review. | Huquqiy sahifalar: qoralama, yuridik ko‘rikdan o‘tmagan. |

## partners.html

| ✓ | English | Uzbek |
|---|---|---|
| ☐ ⚕ | Coriva is a clinically supervised cardiac rehabilitation platform where doctors retain clinical authority and AI supports decision-making, monitoring, and personalization. | Coriva — klinik nazorat ostidagi yurak reabilitatsiyasi platformasi: klinik vakolat shifokorlarda qoladi, sun’iy intellekt esa qaror qabul qilish, kuzatuv va moslashtirishda yordam beradi. |
| ☐ ⚕ | One system for cardiac rehabilitation. | Yurak reabilitatsiyasi uchun yagona tizim. |
| ☐ | Six surfaces, one core | Olti qism, bitta yadro |
| ☐ ⚕ | It connects cardiologists, clinics and patients in one system, so rehabilitation can continue after discharge under the doctor's supervision. | U kardiologlar, klinikalar va bemorlarni bitta tizimda bog‘laydi — reabilitatsiya shifoxonadan chiqqandan keyin ham shifokor nazoratida davom etishi uchun. |
| ☐ | Coriva core | Coriva yadrosi |
| ☐ | One backend, one data model and one set of access rules for every surface. | Barcha qismlar uchun bitta tizim, bitta ma’lumotlar modeli va bitta kirish qoidalari to‘plami. |
| ☐ | built | tayyor |
| ☐ | Surfaces | Qismlar |
| ☐ ⚕ | Patient app | Bemor ilovasi |
| ☐ ⚕ | Android. The patient's daily plan, reminders and reports. | Android. Bemorning kundalik rejasi, eslatmalari va hisobotlari. |
| ☐ ⚕ | Doctor's web dashboard | Shifokorning veb-paneli |
| ☐ ⚕ | Patients who need a decision, approvals and follow-ups. | Qaror kutayotgan bemorlar, tasdiqlashlar va navbatdagi ko‘riklar. |
| ☐ ⚕ | Clinic section | Klinika bo‘limi |
| ☐ ⚕ | A clinic's team, roles and handover, inside the doctor's dashboard. | Klinika jamoasi, rollar va bemorni topshirish — shifokor panelining ichida. |
| ☐ ⚕ | Doctors' mobile app | Shifokorlar uchun mobil ilova |
| ☐ ⚕ | Android, for doctors away from the desk. | Android, yo‘lda yoki bo‘limda yurgan shifokorlar uchun. |
| ☐ | Platform administration | Platformani boshqarish |
| ☐ | Internal oversight and configuration. | Ichki nazorat va sozlamalar. |
| ☐ | Public website | Veb-sayt |
| ☐ | This site. | Ushbu sayt. |
| ☐ | You are here | Siz shu yerdasiz |
| ☐ | Technology | Texnologiya |
| ☐ | One backend for everything | Hammasi uchun yagona tizim |
| ☐ | A modular Go service with shared API contracts. Every surface follows the same rules for access and data. | Umumiy API shartnomalariga ega modulli Go xizmati. Har bir qism kirish va ma’lumotlar bo‘yicha bir xil qoidalarga amal qiladi. |
| ☐ ⚕ | Data kept apart per clinic | Ma’lumotlar har bir klinika uchun alohida saqlanadi |
| ☐ | PostgreSQL with row-level security, access by role, and a record of sensitive actions. | Qator darajasidagi himoyaga ega PostgreSQL, rol bo‘yicha kirish va muhim amallar qaydnomasi. |
| ☐ ⚕ | AI that Coriva runs itself | Coriva o‘zi ishlatadigan sun’iy intellekt |
| ☐ ⚕ | Open models hosted by Coriva, answering only from approved research papers, with sources. No third-party AI service. | Coriva o‘zi joylashtirgan ochiq modellar faqat tasdiqlangan ilmiy maqolalar asosida, manbalari bilan javob beradi. Uchinchi tomon sun’iy intellekt xizmati yo‘q. |
| ☐ | Native and web apps | Mobil va veb-ilovalar |
| ☐ ⚕ | Android (Kotlin) for patients; a web dashboard (Next.js) for doctors and clinics. | Bemorlar uchun Android (Kotlin); shifokorlar va klinikalar uchun veb-panel (Next.js). |
| ☐ | Roadmap | Yo‘l xaritasi |
| ☐ | No dates yet. Each stage starts only after the one before it is validated. | Hozircha sanalar yo‘q. Har bir bosqich oldingisi tasdiqlangandan keyingina boshlanadi. |
| ☐ | Being built now. | Hozir ishlab chiqilmoqda. |
| ☐ | Secure backend and data separation | Xavfsiz tizim va ma’lumotlarni ajratish |
| ☐ ⚕ | Patient app: sign-in, onboarding, home | Bemor ilovasi: kirish, dastlabki sozlash, bosh sahifa |
| ☐ ⚕ | Supervised patient activation | Bemorni nazorat ostida faollashtirish |
| ☐ ⚕ | Planned for the controlled pilot. | Nazorat ostidagi pilot loyihaga rejalashtirilgan. |
| ☐ ⚕ | A controlled pilot with selected doctors and clinics | Tanlangan shifokorlar va klinikalar bilan nazorat ostidagi pilot loyiha |
| ☐ ⚕ | Doctor-approved rehabilitation programs | Shifokor tasdiqlagan reabilitatsiya dasturlari |
| ☐ ⚕ | Medication schedule and reminders | Dori jadvali va eslatmalar |
| ☐ | Progress reports | Natijalar haqida hisobotlar |
| ☐ ⚕ | Clinic teams | Klinika jamoalari |
| ☐ ⚕ | Rehabilitation intelligence (research in progress) | Reabilitatsiya uchun sun’iy intellekt (tadqiqot bosqichida) |
| ☐ ⚕ | Planned for a later phase. | Keyingi bosqichga rejalashtirilgan. |
| ☐ ⚕ | Phase 2: doctors' mobile app, wearable and phone data, clinic reporting | 2-bosqich: shifokorlar uchun mobil ilova, aqlli soat, fitnes-bilaguzuk va telefon ma’lumotlari, klinika hisobotlari |
| ☐ ⚕ | Phase 3: risk intelligence, validated before any clinical use; platform administration | 3-bosqich: xavfni baholash — klinik qo‘llashdan oldin tasdiqlanadi; platformani boshqarish |
| ☐ | Talk to the team. | Jamoa bilan gaplashing. |
| ☐ | For partnerships and investment, contact the Coriva team. | Hamkorlik va investitsiya bo‘yicha Coriva jamoasi bilan bog‘laning. |
| ☐ | Team | Jamoa |
| ☐ | We'll introduce the team here soon. | Tez orada jamoani shu yerda tanishtiramiz. |

## patients.html

| ✓ | English | Uzbek |
|---|---|---|
| ☐ ⚕ | For patients and families | Bemorlar va ularning yaqinlari uchun |
| ☐ ⚕ | Your doctor's plan, at home. | Shifokoringiz rejasi — uyingizda. |
| ☐ ⚕ | Coriva is being built to help you follow the rehabilitation plan your doctor makes for you, day by day. It is not available yet. | Coriva shifokoringiz siz uchun tuzgan reabilitatsiya rejasiga kunma-kun amal qilishingizga yordam berish uchun yaratilmoqda. U hali ishga tushmagan. |
| ☐ | What Coriva will help with | Coriva nimada yordam beradi |
| ☐ ⚕ | Your plan for each day | Har kunlik rejangiz |
| ☐ ⚕ | Walks, exercise and meals, as your doctor planned them. | Sayr, mashqlar va ovqatlanish — shifokoringiz rejalashtirganidek. |
| ☐ ⚕ | Medicine reminders | Dori eslatmalari |
| ☐ ⚕ | At the times your doctor entered. Coriva never changes your medicine. | Shifokoringiz kiritgan vaqtlarda. Coriva dorilaringizni hech qachon o‘zgartirmaydi. |
| ☐ ⚕ | Telling your doctor how you are | Ahvolingizni shifokoringizga aytish |
| ☐ ⚕ | A short report that your doctor reads at their next review. | Shifokoringiz navbatdagi ko‘rib chiqishda o‘qiydigan qisqa hisobot. |
| ☐ | Your progress | Natijalaringiz |
| ☐ | What you have done so far, from your own reports. | Shu paytgacha bajarganlaringiz — o‘z hisobotlaringiz asosida. |
| ☐ | How you join | Qanday qo‘shilasiz |
| ☐ ⚕ | Your doctor invites you | Shifokoringiz sizni taklif qiladi |
| ☐ ⚕ | If Coriva is right for you, your doctor will offer it. | Coriva sizga mos kelsa, shifokoringiz uni o‘zi taklif qiladi. |
| ☐ ⚕ | You start at the clinic | Klinikada boshlaysiz |
| ☐ | Staff help you set up the app with a one-time code. | Xodimlar bir martalik kod bilan ilovani sozlashingizga yordam beradi. |
| ☐ ⚕ | You follow your doctor’s plan | Shifokoringiz rejasiga amal qilasiz |
| ☐ | Day by day, at home, at your own pace. | Kunma-kun, uyda, o‘zingizga qulay sur’atda. |
| ☐ | You cannot sign up on this website. | Bu veb-saytda ro‘yxatdan o‘tib bo‘lmaydi. |
| ☐ ⚕ | Coriva is not an emergency service. | Coriva tez yordam xizmati emas. |
| ☐ ⚕ | Coriva does not watch you all the time. Your doctor reads your reports at their next review. | Coriva sizni doim kuzatib turmaydi. Hisobotlaringizni shifokoringiz navbatdagi ko‘rib chiqishda o‘qiydi. |
| ☐ | Your information | Ma’lumotlaringiz |
| ☐ ⚕ | Your doctor sees what you share. | Ulashgan ma’lumotlaringizni shifokoringiz ko‘radi. |
| ☐ ⚕ | If your doctor is away, a colleague at the same clinic may look after you. This change is recorded. | Shifokoringiz ishda bo‘lmasa, sizga shu klinikadagi hamkasbi qarashi mumkin. Bu o‘zgarish qayd etiladi. |
| ☐ ⚕ | Your reports are your own words, not a medical record. | Hisobotlaringiz — o‘z so‘zlaringiz, tibbiy yozuv emas. |
| ☐ ⚕ | Your clinic's information is kept apart from other clinics. | Klinikangiz ma’lumotlari boshqa klinikalardan alohida saqlanadi. |
| ☐ ⚕ | Questions from patients and families | Bemorlar va ularning yaqinlari savollari |
| ☐ | Can I sign up myself? | O‘zim ro‘yxatdan o‘ta olamanmi? |
| ☐ ⚕ | No. Your doctor invites you. This keeps your care in your doctor’s hands. | Yo‘q. Sizni shifokoringiz taklif qiladi. Shunda davolanishingiz shifokoringiz qo‘lida qoladi. |
| ☐ ⚕ | Will Coriva change my medicine? | Coriva dorilarimni o‘zgartiradimi? |
| ☐ ⚕ | No. Only your doctor decides about your medicine. Coriva reminds you of what your doctor entered. | Yo‘q. Dorilaringiz haqida faqat shifokoringiz qaror qiladi. Coriva shifokoringiz kiritgan narsani eslatadi, xolos. |
| ☐ | Does a computer decide my treatment? | Davolanishimni kompyuter hal qiladimi? |
| ☐ ⚕ | No. Your doctor decides. Coriva may help your doctor prepare a plan, but your doctor checks and approves it. | Yo‘q. Qarorni shifokoringiz qabul qiladi. Coriva shifokoringizga reja tayyorlashda yordam berishi mumkin, lekin uni shifokoringiz tekshiradi va tasdiqlaydi. |
| ☐ | What if I miss a day? | Bir kunni o‘tkazib yuborsam-chi? |
| ☐ ⚕ | That is all right. Tell your doctor in your report. Your doctor decides if anything should change. | Hechqisi yo‘q. Hisobotingizda shifokoringizga ayting. Biror narsani o‘zgartirish kerakmi — shifokoringiz hal qiladi. |
| ☐ | Which phones will it work on? | Qaysi telefonlarda ishlaydi? |
| ☐ | At first, Android phones. | Dastlab Android telefonlarda. |
| ☐ | Questions about your care? | Davolanishingiz haqida savollaringiz bormi? |
| ☐ ⚕ | Ask your doctor. They know your plan. | Shifokoringizdan so‘rang. Rejangizni u biladi. |
| ☐ ⚕ | Read the medical disclaimer | Tibbiy ogohlantirishni o‘qish |
| ☐ ⚕ | Photograph: Shixart1985 (CC BY 2.0), via Wikimedia Commons. People shown are not Coriva patients. | Surat: Shixart1985 (CC BY 2.0), Wikimedia Commons orqali. Suratdagilar Coriva bemorlari emas. |

## platform.html

| ✓ | English | Uzbek |
|---|---|---|
| ☐ | How Coriva works. | Coriva qanday ishlaydi. |
| ☐ ⚕ | Follow one rehabilitation program from research to a patient's day, and see where the doctor decides. Every step shows its status today. | Bitta reabilitatsiya dasturining tadqiqotdan bemor kunigacha bo‘lgan yo‘lini kuzating va shifokor qayerda qaror qabul qilishini ko‘ring. Har bir qadamda bugungi holati ko‘rsatilgan. |
| ☐ ⚕ | From research to a patient's day | Tadqiqotdan bemorning kunigacha |
| ☐ ⚕ | An example with demo data. The doctor decides at step 3, and again at every review. | Namunaviy ma’lumotlar bilan misol. Shifokor 3-qadamda va har bir ko‘rib chiqishda yana qaror qabul qiladi. |
| ☐ | Status labels | Holat belgilari |
| ☐ ⚕ | Approved research | Tasdiqlangan tadqiqotlar |
| ☐ ⚕ | The team approves the research papers Coriva may use. Nothing else goes in. | Coriva foydalanishi mumkin bo‘lgan ilmiy maqolalarni jamoa tasdiqlaydi. Boshqa hech narsa kiritilmaydi. |
| ☐ | Status | Holati |
| ☐ | Who decides | Kim qaror qiladi |
| ☐ ⚕ | The Coriva team approves each paper. | Har bir maqolani Coriva jamoasi tasdiqlaydi. |
| ☐ ⚕ | Approved paper | Tasdiqlangan maqola |
| ☐ ⚕ | Cardiac rehabilitation · example | Yurak reabilitatsiyasi · misol |
| ☐ | Section 4 | 4-bo‘lim |
| ☐ | Used as a source | Manba sifatida ishlatilgan |
| ☐ ⚕ | An AI draft | Sun’iy intellekt qoralamasi |
| ☐ ⚕ | AI drafts rehabilitation guidance for one patient from those papers, with the source of every point. If the papers don't support it, it says so. | Sun’iy intellekt shu maqolalar asosida bitta bemor uchun reabilitatsiya tavsiyalarini tayyorlaydi va har bir band manbasini ko‘rsatadi. Maqolalarda asos bo‘lmasa, buni ochiq aytadi. |
| ☐ | No one yet. It is only a suggestion. | Hozircha hech kim. Bu faqat taklif. |
| ☐ ⚕ | Walking plan · source: approved paper, section 4 | Sayr rejasi · manba: tasdiqlangan maqola, 4-bo‘lim |
| ☐ ⚕ | The doctor decides | Shifokor qaror qiladi |
| ☐ ⚕ | The doctor reads the draft, edits it, and approves or rejects it. The program reaches the patient only after approval. | Shifokor qoralamani o‘qiydi, tahrirlaydi va tasdiqlaydi yoki rad etadi. Dastur bemorga faqat tasdiqlangandan keyin yetib boradi. |
| ☐ ⚕ | The patient's doctor. | Bemorning shifokori. |
| ☐ | Program draft | Dastur qoralamasi |
| ☐ | Edited by you | Siz tahrirlagansiz |
| ☐ ⚕ | The patient's day | Bemorning kuni |
| ☐ ⚕ | The patient sees the approved plan: activity, nutrition, and medication exactly as the doctor entered it. | Bemor tasdiqlangan rejani ko‘radi: jismoniy faollik, ovqatlanish va dorilar — aynan shifokor kiritganidek. |
| ☐ ⚕ | plans | rejalar |
| ☐ | the app | ilova |
| ☐ ⚕ | The doctor's plan. Coriva never changes medication. | Shifokorning rejasi. Coriva dorilarni hech qachon o‘zgartirmaydi. |
| ☐ ⚕ | Approved by your doctor | Shifokoringiz tasdiqlagan |
| ☐ | A report | Hisobot |
| ☐ ⚕ | The patient tells the doctor how the day went. If they feel unwell, they call their local emergency number. | Bemor kun qanday o‘tganini shifokorga aytadi. O‘zini yomon his qilsa, tez yordam raqamiga qo‘ng‘iroq qiladi. |
| ☐ ⚕ | The patient. | Bemor. |
| ☐ | The next review | Navbatdagi ko‘rib chiqish |
| ☐ ⚕ | Reports wait for the doctor's next review. The doctor adjusts the program when needed. | Hisobotlar shifokorning navbatdagi ko‘rib chiqishini kutadi. Zarur bo‘lsa, shifokor dasturni o‘zgartiradi. |
| ☐ ⚕ | The doctor. | Shifokor. |
| ☐ ⚕ | Patient-reported · demo data | Bemor yuborgan · namunaviy ma’lumotlar |
| ☐ | Everything, with its status | Hammasi — holati bilan |
| ☐ ⚕ | Each part, and what the doctor controls. | Har bir qism va shifokor nimani boshqarishi. |
| ☐ | Supervised activation | Nazorat ostida faollashtirish |
| ☐ ⚕ | Decides who is invited. Patients cannot sign up on their own. | Kim taklif qilinishini hal qiladi. Bemorlar o‘zlari ro‘yxatdan o‘ta olmaydi. |
| ☐ | Care relationships and handover | Shifokor–bemor aloqalari va topshirish |
| ☐ ⚕ | Sees only the patients in their care. | Faqat o‘z qaramog‘idagi bemorlarni ko‘radi. |
| ☐ ⚕ | Doctor's dashboard | Shifokor paneli |
| ☐ | Decides every next step. | Har bir keyingi qadamni hal qiladi. |
| ☐ | · membership and handover | · a’zolik va topshirish |
| ☐ ⚕ | Clinic leaders manage the team. Clinical decisions stay with each patient's doctor. | Klinika rahbarlari jamoani boshqaradi. Klinik qarorlar har bir bemorning shifokorida qoladi. |
| ☐ ⚕ | Patient app (Android) | Bemor ilovasi (Android) |
| ☐ ⚕ | The app shows only what the doctor approved. | Ilova faqat shifokor tasdiqlagan narsani ko‘rsatadi. |
| ☐ | Privacy and security foundation | Maxfiylik va xavfsizlik asosi |
| ☐ | Every sensitive action is recorded. | Har bir muhim amal qayd etiladi. |
| ☐ ⚕ | · clinic screens | · klinika ekranlari |
| ☐ ⚕ | Rehabilitation programs | Reabilitatsiya dasturlari |
| ☐ ⚕ | Creates, edits and approves every program. Nothing reaches the patient before approval. | Har bir dasturni yaratadi, tahrirlaydi va tasdiqlaydi. Tasdiqlanmaguncha bemorga hech narsa yetib bormaydi. |
| ☐ ⚕ | Enters the schedule. Coriva and its AI never change it. | Jadvalni kiritadi. Coriva ham, uning sun’iy intellekti ham uni hech qachon o‘zgartirmaydi. |
| ☐ | Reviews reports at the next review. They are not watched in real time. | Hisobotlarni navbatdagi ko‘rib chiqishda ko‘rib chiqadi. Ular real vaqtda kuzatilmaydi. |
| ☐ ⚕ | Rehabilitation intelligence | Reabilitatsiya uchun sun’iy intellekt |
| ☐ ⚕ | Reviews, edits, approves or rejects every draft. | Har bir qoralamani ko‘rib chiqadi, tahrirlaydi, tasdiqlaydi yoki rad etadi. |
| ☐ | Not used in care before validation. | Tasdiqlanmaguncha davolashda qo‘llanmaydi. |
| ☐ | Wearable and phone data | Aqlli soat, fitnes-bilaguzuk va telefon ma’lumotlari |
| ☐ | Not yet defined. | Hali belgilanmagan. |
| ☐ | Oversight, privacy and security | Nazorat, maxfiylik va xavfsizlik |
| ☐ ⚕ | Clinical oversight | Klinik nazorat |
| ☐ ⚕ | Clinical rules are reviewed | Klinik qoidalar ko‘rib chiqiladi |
| ☐ ⚕ | Any clinical rule or threshold is reviewed by a qualified cardiologist before it is used. | Har qanday klinik qoida yoki chegara qo‘llanishidan oldin malakali kardiolog tomonidan ko‘rib chiqiladi. |
| ☐ ⚕ | The other rules are in the steps above: the doctor approves every program (step 3), medication stays as entered (step 4), and reports wait for the doctor's review (step 6). Coriva is not an emergency service. | Qolgan qoidalar yuqoridagi qadamlarda: har bir dasturni shifokor tasdiqlaydi (3-qadam), dorilar kiritilganidek qoladi (4-qadam), hisobotlar shifokor ko‘rib chiqishini kutadi (6-qadam). Coriva tez yordam xizmati emas. |
| ☐ | Built now | Hozir yaratilmoqda |
| ☐ ⚕ | Each clinic's data is kept apart, enforced in the database | Har bir klinikaning ma’lumotlari alohida saqlanadi — bu ma’lumotlar bazasi darajasida ta’minlangan |
| ☐ ⚕ | Access by role: doctor, clinic leader, patient | Rol bo‘yicha kirish: shifokor, klinika rahbari, bemor |
| ☐ | Single-use activation codes, given in person | Shaxsan beriladigan bir martalik faollashtirish kodlari |
| ☐ | A record of sensitive actions | Muhim amallar qaydnomasi |
| ☐ | Synthetic data only during development | Ishlab chiqishda faqat namunaviy ma’lumotlar |
| ☐ | Before the pilot | Pilot loyihadan oldin |
| ☐ | An independent security review | Mustaqil xavfsizlik tekshiruvi |
| ☐ ⚕ | AI on open models Coriva runs itself, not a third-party AI service | Sun’iy intellekt Coriva o‘zi ishlatadigan ochiq modellarda ishlaydi, uchinchi tomon xizmatida emas |
| ☐ | Privacy notice and terms, reviewed by lawyers | Yuristlar ko‘rib chiqqan maxfiylik bildirishnomasi va shartlar |
| ☐ ⚕ | How the AI is being built | Sun’iy intellekt qanday yaratilmoqda |
| ☐ ⚕ | Rehabilitation intelligence is in research for the pilot. It is built to six rules. | Reabilitatsiya uchun sun’iy intellekt pilot loyihaga qadar tadqiq qilinmoqda. U oltita qoida asosida quriladi. |
| ☐ ⚕ | Approved research only | Faqat tasdiqlangan tadqiqotlar |
| ☐ ⚕ | The AI works only from research papers the team has approved, not from the open internet. | Sun’iy intellekt ochiq internetdan emas, faqat jamoa tasdiqlagan ilmiy maqolalar asosida ishlaydi. |
| ☐ | Always cited | Har doim manbasi bilan |
| ☐ | Every point shows its source: the paper, page or section. | Har bir band o‘z manbasini ko‘rsatadi: maqola, sahifa yoki bo‘lim. |
| ☐ | Says when it doesn't know | Bilmasa, bilmasligini aytadi |
| ☐ | If the papers don't support an answer, it says so and stops. | Maqolalarda javobga asos bo‘lmasa, buni aytadi va to‘xtaydi. |
| ☐ | Labelled as a suggestion | Taklif deb belgilangan |
| ☐ ⚕ | Drafts look different from approved care and are never shown to patients as instructions. | Qoralamalar tasdiqlangan rejadan farq qilib ko‘rinadi va bemorlarga hech qachon ko‘rsatma sifatida ko‘rsatilmaydi. |
| ☐ ⚕ | Nothing reaches a patient until the doctor approves it. | Shifokor tasdiqlamaguncha bemorga hech narsa yetib bormaydi. |
| ☐ ⚕ | Never diagnoses | Hech qachon tashxis qo‘ymaydi |
| ☐ ⚕ | It does not diagnose, prescribe, or change medication. | U tashxis qo‘ymaydi, dori yozmaydi va dorilarni o‘zgartirmaydi. |
| ☐ ⚕ | Cardiologists and clinics can join the waitlist. We'll contact you about the pilot. | Kardiologlar va klinikalar kutish ro‘yxatiga qo‘shilishi mumkin. Pilot loyiha bo‘yicha siz bilan bog‘lanamiz. |
| ☐ | Product screens show demo data. | Ekranlarda namunaviy ma’lumotlar ko‘rsatilgan. |

## privacy.html

| ✓ | English | Uzbek |
|---|---|---|
| ☐ | This page is not in force. The text will be written and reviewed by a lawyer before the website is published. | Bu sahifa hali kuchga kirmagan. Matn veb-sayt e’lon qilinishidan oldin yurist tomonidan yoziladi va ko‘rib chiqiladi. |
| ☐ | Who is responsible for your information | Ma’lumotlaringiz uchun kim javobgar |
| ☐ | What we collect | Qanday ma’lumot yig‘amiz |
| ☐ | Why we use it | Nima uchun foydalanamiz |
| ☐ | How long we keep it | Qancha vaqt saqlaymiz |
| ☐ | Where it is stored | Qayerda saqlanadi |
| ☐ | Your rights | Huquqlaringiz |

## waitlist.html

| ✓ | English | Uzbek |
|---|---|---|
| ☐ ⚕ | Join the Coriva pilot waitlist. | Coriva pilot loyihasining kutish ro‘yxatiga qo‘shiling. |
| ☐ ⚕ | For cardiologists, clinics, partners and investors. | Kardiologlar, klinikalar, hamkorlar va investorlar uchun. |
| ☐ | What happens next | Keyin nima bo‘ladi |
| ☐ | You join | Siz qo‘shilasiz |
| ☐ ⚕ | Choose your role and enter your work details. | Rolingizni tanlang va ish ma’lumotlaringizni kiriting. |
| ☐ | You confirm | Siz tasdiqlaysiz |
| ☐ ⚕ | We send one email. Press Confirm in it to join the list. | Bitta xat yuboramiz. Ro‘yxatga qo‘shilish uchun undagi “Tasdiqlash”ni bosing. |
| ☐ | We contact you | Biz siz bilan bog‘lanamiz |
| ☐ ⚕ | When pilot places open, we contact confirmed participants by email. | Pilot loyihada joylar ochilganda, tasdiqlagan ishtirokchilar bilan pochta orqali bog‘lanamiz. |
| ☐ ⚕ | The pilot waitlist opens soon. | Pilot loyihaning kutish ro‘yxati tez orada ochiladi. |
| ☐ ⚕ | and agree that Coriva uses these details to contact me about the pilot. | bilan tanishdim hamda Coriva ushbu ma’lumotlardan pilot loyiha bo‘yicha men bilan bog‘lanish uchun foydalanishiga roziman. |
| ☐ ⚕ | Join the waitlist | Kutish ro‘yxatiga qo‘shilish |
| ☐ | What we keep | Nimalarni saqlaymiz |
| ☐ ⚕ | Your role, name, work email, organisation and country, and your message if you write one. Used only to contact you about the pilot. No marketing email; withdraw at any time with the link in the email. Details in the | Rolingiz, ismingiz, ish elektron pochtangiz, tashkilotingiz va mamlakatingiz, shuningdek yozgan bo‘lsangiz — xabaringiz. Faqat pilot loyiha bo‘yicha siz bilan bog‘lanish uchun ishlatiladi. Reklama xatlari yo‘q; xatdagi havola orqali istalgan vaqtda ro‘yxatdan chiqish mumkin. Batafsil: |
