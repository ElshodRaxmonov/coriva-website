# Translation review

Russian: **draft, needs native and clinical review.** The ru/ pages stay `noindex` until every box is ticked
and the owner confirms; then set `PUBLISH['ru'] = True` in tools/build_languages.py and re-run it.

Fix a translation in `i18n/ru.json`, never in ru/. Strings marked ⚕ make a clinical or safety statement: they need a clinician as well as a native reader.

Untranslated strings: see `i18n/missing-ru.txt`.

## Search terms (proposal, for the reviewer to accept or reject)

Use these only where the page already says the same thing in English. No new claims.

- [ ] Home title uses «Кардиореабилитация». Keep it (the term people search for), or prefer «реабилитация сердца»?
- [ ] Where the English says "cardiac rehabilitation", use «кардиореабилитация» consistently across pages.

## 404.html

| ✓ | English | Russian |
|---|---|---|
| ☐ | Page not found | Страница не найдена |
| ☐ | Skip to main content | Перейти к основному содержанию |
| ☐ | Primary | Основное меню |
| ☐ | Platform | Платформа |
| ☐ | Doctors | Врачи |
| ☐ | Clinics | Клиники |
| ☐ | Patients | Пациенты |
| ☐ | Partners | Партнёры |
| ☐ | Join the pilot waitlist | Записаться в лист ожидания пилота |
| ☐ | Join waitlist | Записаться |
| ☐ | Menu | Меню |
| ☐ | English | English |
| ☐ | Error 404 | Ошибка 404 |
| ☐ | This page doesn't exist. | Такой страницы нет. |
| ☐ | The link may be old or mistyped. | Возможно, ссылка устарела или в ней опечатка. |
| ☐ | Go to the home page | Перейти на главную страницу |
| ☐ | How Coriva works | Как работает Coriva |
| ☐ | Company | Компания |
| ☐ | Partners and investors | Партнёры и инвесторы |
| ☐ | Contact | Контакты |
| ☐ | Legal | Правовая информация |
| ☐ | Privacy notice | Политика конфиденциальности |
| ☐ ⚕ | Medical disclaimer | Медицинское предупреждение |
| ☐ ⚕ | Coriva is not an emergency service. If you feel unwell, call your local emergency number. | Coriva — не служба экстренной помощи. Если вы плохо себя чувствуете, позвоните в скорую помощь (103). |

## clinics.html

| ✓ | English | Russian |
|---|---|---|
| ☐ | For clinics | Для клиник |
| ☐ | Coriva is being built with clinics for the pilot: your doctors, their patients and care handover in one place, with clear roles and your data kept apart from other clinics. | Coriva создаётся вместе с клиниками для пилотного проекта: ваши врачи, их пациенты и передача пациентов — в одном месте, с чёткими ролями, а данные вашей клиники хранятся отдельно от других клиник. |
| ☐ | Coordinate rehabilitation across your team. | Координируйте реабилитацию всей командой. |
| ☐ | Join as a clinic | Записаться как клиника |
| ☐ | Coordination | Координация |
| ☐ | What your clinic will use, and its status today. | Чем будет пользоваться ваша клиника и каков статус на сегодня. |
| ☐ | Your team in one view | Ваша команда — на одном экране |
| ☐ | Who each doctor is caring for, inside the doctor’s dashboard. | Кого ведёт каждый врач — внутри панели врача. |
| ☐ | Pilot | Пилот |
| ☐ | clinic screens | экраны для клиник |
| ☐ | Care handover | Передача пациента |
| ☐ ⚕ | When a doctor is away, a colleague takes over, and the handover is recorded. | Когда врача нет на месте, ведение его пациентов берёт на себя коллега, и передача фиксируется. |
| ☐ | In development | В разработке |
| ☐ | backend built | серверная часть готова |
| ☐ | Activation in your clinic | Активация в вашей клинике |
| ☐ | Patients activate the app at your clinic, with staff present, using a single-use code. | Пациенты активируют приложение в вашей клинике, в присутствии персонала, с помощью одноразового кода. |
| ☐ | Who can do what | Кто что может делать |
| ☐ | Roles are enforced by the system, not only hidden in the screens. | Роли обеспечиваются самой системой, а не только скрытием элементов на экранах. |
| ☐ | Clinic leader | Руководитель клиники |
| ☐ | Can | Может |
| ☐ | Manages members and roles. Reassigns care inside the clinic. | Управляет участниками и ролями. Перераспределяет ведение пациентов внутри клиники. |
| ☐ | Cannot | Не может |
| ☐ ⚕ | Does not see patients' clinical records. | Не видит медицинскую документацию пациентов. |
| ☐ | Doctor | Врач |
| ☐ ⚕ | Cares for their own patients: approves programs and reviews reports. | Ведёт своих пациентов: утверждает программы и просматривает отчёты. |
| ☐ | Does not see patients outside their care. | Не видит пациентов, которых не ведёт. |
| ☐ | Patient | Пациент |
| ☐ ⚕ | Follows the plan their doctor approved and reports progress. | Следует плану, утверждённому врачом, и сообщает о своём прогрессе. |
| ☐ ⚕ | Cannot change their plan or medication. | Не может менять свой план или лекарства. |
| ☐ | Oversight and data | Контроль и данные |
| ☐ ⚕ | Clinical decisions stay with each patient's doctor. | Клинические решения остаются за врачом каждого пациента. |
| ☐ | Handovers and other sensitive actions are recorded. | Передачи пациентов и другие важные действия фиксируются. |
| ☐ ⚕ | AI drafts go only to doctors, never to patients directly. | Черновики ИИ попадают только к врачам и никогда не отправляются пациентам напрямую. |
| ☐ | Each clinic's data is kept apart, enforced in the database. | Данные каждой клиники хранятся отдельно — это обеспечивается на уровне базы данных. |
| ☐ | foundation built | основа готова |
| ☐ | Where data is stored: to be confirmed before the pilot. | Где хранятся данные: будет определено до пилотного проекта. |
| ☐ | Development uses synthetic data only. | При разработке используются только синтетические данные. |
| ☐ | Questions from clinics | Вопросы клиник |
| ☐ | Can our clinic join the pilot? | Может ли наша клиника участвовать в пилотном проекте? |
| ☐ | Register your interest on the waitlist with the role "Clinic". The pilot is in preparation with selected doctors and clinics; we contact you about it. | Оставьте заявку в листе ожидания, выбрав роль «Клиника». Пилотный проект готовится с отобранными врачами и клиниками; мы свяжемся с вами по этому поводу. |
| ☐ | Can clinic leaders see patients' records? | Видят ли руководители клиник медицинскую документацию пациентов? |
| ☐ ⚕ | No. Clinic leaders manage the team and care assignments. Clinical records stay with each patient's doctor. | Нет. Руководители клиник управляют командой и распределением пациентов. Медицинская документация остаётся у врача каждого пациента. |
| ☐ | Where is our data stored? | Где хранятся наши данные? |
| ☐ | To be confirmed before the pilot. We will state it on this page and in the privacy notice. | Будет определено до пилотного проекта. Мы укажем это на этой странице и в политике конфиденциальности. |
| ☐ | What happens when a doctor is away? | Что происходит, когда врача нет на месте? |
| ☐ | Care can pass to a colleague in the same clinic. The handover is recorded. | Ведение пациента можно передать коллеге в той же клинике. Передача фиксируется. |
| ☐ | How do patients join? | Как подключаются пациенты? |
| ☐ | Through their doctor. The doctor invites the patient; during the pilot, the app is activated at the clinic with staff present. There is no self sign-up. | Через своего врача. Врач приглашает пациента; во время пилотного проекта приложение активируется в клинике, в присутствии персонала. Самостоятельной регистрации нет. |
| ☐ | Bring your team to the pilot. | Подключите свою команду к пилотному проекту. |
| ☐ | Join the waitlist as a clinic. We'll contact you about the pilot. | Запишитесь в лист ожидания как клиника. Мы свяжемся с вами по поводу пилотного проекта. |
| ☐ | Photograph: Jacek Halicki (CC BY-SA 4.0), via Wikimedia Commons. | Фото: Jacek Halicki (CC BY-SA 4.0), через Wikimedia Commons. |

## contact.html

| ✓ | English | Russian |
|---|---|---|
| ☐ | Contact the team. | Свяжитесь с командой. |
| ☐ | For partnerships, investment and other questions about Coriva. | По вопросам партнёрства, инвестиций и другим вопросам о Coriva. |
| ☐ | Write to us | Напишите нам |
| ☐ | Use the form, or write to | Воспользуйтесь формой или напишите на |
| ☐ | Are you a patient? | Вы пациент? |
| ☐ ⚕ | Please talk to your doctor about your care. Do not send health information here. If you feel unwell, call your local emergency number. | Пожалуйста, обсуждайте своё лечение с врачом. Не отправляйте сюда сведения о здоровье. Если вы плохо себя чувствуете, позвоните в скорую помощь (103). |
| ☐ | Pilot waitlist | Лист ожидания пилотного проекта |
| ☐ | The contact form opens soon. | Форма обратной связи скоро откроется. |
| ☐ | Until then, write to us: | А пока напишите нам: |
| ☐ | All fields are required unless marked optional. | Все поля обязательны, если не отмечены как необязательные. |
| ☐ | I am | Я — |
| ☐ | Cardiologist | Кардиолог |
| ☐ | Clinic or department | Клиника или отделение |
| ☐ | Partner or investor | Партнёр или инвестор |
| ☐ | Other | Другое |
| ☐ | Full name | Имя и фамилия |
| ☐ | Work email | Рабочая электронная почта |
| ☐ | We send one email to confirm it. | Мы отправим одно письмо, чтобы подтвердить адрес. |
| ☐ | Organisation | Организация |
| ☐ | (optional for Other) | (необязательно для варианта «Другое») |
| ☐ | Country | Страна |
| ☐ | Choose a country | Выберите страну |
| ☐ | Uzbekistan | Узбекистан |
| ☐ | Kazakhstan | Казахстан |
| ☐ | Kyrgyzstan | Кыргызстан |
| ☐ | Tajikistan | Таджикистан |
| ☐ | Turkmenistan | Туркменистан |
| ☐ | Russia | Россия |
| ☐ | Germany | Германия |
| ☐ | United Kingdom | Великобритания |
| ☐ | United States | США |
| ☐ | Message | Сообщение |
| ☐ | (optional) | (необязательно) |
| ☐ | Do not include health information about yourself or anyone else. Up to 1,000 characters. | Не указывайте сведения о здоровье — своём или чужом. До 1 000 символов. |
| ☐ | I have read the | Я прочитал(а) |
| ☐ | privacy notice | политику конфиденциальности |
| ☐ | and agree that Coriva uses these details to contact me about my message. | и согласен(-на) с тем, что Coriva использует эти данные, чтобы связаться со мной по поводу моего сообщения. |
| ☐ | Website | Веб-сайт |
| ☐ | Send message | Отправить сообщение |
| ☐ | The form is a design: it is not connected and sends nothing. | Эта форма — макет: она не подключена и ничего не отправляет. |

## doctors.html

| ✓ | English | Russian |
|---|---|---|
| ☐ | For cardiologists | Для кардиологов |
| ☐ | Supervise rehabilitation beyond discharge. | Контролируйте реабилитацию и после выписки. |
| ☐ ⚕ | Coriva is being built so your patients can continue cardiac rehabilitation at home, on the plan you approve. You decide. AI helps you prepare. | Coriva создаётся, чтобы ваши пациенты могли продолжать кардиореабилитацию дома по плану, который утверждаете вы. Решаете вы. ИИ помогает с подготовкой. |
| ☐ | Pilot in preparation | Пилотный проект в подготовке |
| ☐ | Join as a cardiologist | Записаться как кардиолог |
| ☐ | What you would do | Что вы будете делать |
| ☐ | Your part | Ваша часть работы |
| ☐ | Three things you do in Coriva. Everything else supports them. | Три вещи, которые вы делаете в Coriva. Всё остальное их поддерживает. |
| ☐ | Invite | Пригласить |
| ☐ | You invite a patient. They activate the app in your clinic, with staff present, using a single-use code. | Вы приглашаете пациента. Он активирует приложение в вашей клинике, в присутствии персонала, с помощью одноразового кода. |
| ☐ | Plan and approve | Планирование и утверждение |
| ☐ ⚕ | Write a program, or start from an AI draft built from approved research. You edit it and approve it. Nothing reaches the patient before that. | Составьте программу сами или начните с черновика ИИ, созданного на основе утверждённых исследований. Вы редактируете и утверждаете её. До этого пациенту ничего не поступает. |
| ☐ | Review | Просмотр |
| ☐ ⚕ | See the patients who need a decision or sent a report. Reports wait for your review. | Смотрите, каким пациентам нужно решение и кто прислал отчёт. Отчёты ждут вашего просмотра. |
| ☐ | dashboard | панель |
| ☐ | reports | отчёты |
| ☐ | Your patients | Ваши пациенты |
| ☐ | In development · demo data | В разработке · демонстрационные данные |
| ☐ | 3 patients need you today | Сегодня вы нужны 3 пациентам |
| ☐ | Bekzod T. | Bekzod T. |
| ☐ ⚕ | Program draft waits for your approval | Черновик программы ждёт вашего утверждения |
| ☐ ⚕ | AI suggestion, not reviewed | Предложение ИИ, не проверено |
| ☐ ⚕ | Walking, 5 days a week | Ходьба, 5 дней в неделю |
| ☐ ⚕ | Edited by you · source: approved paper, section 4 | Отредактировано вами · источник: утверждённая статья, раздел 4 |
| ☐ | Approve | Утвердить |
| ☐ | Reject | Отклонить |
| ☐ | Lola M. | Lola M. |
| ☐ | New report | Новый отчёт |
| ☐ | Patient-reported | Со слов пациента |
| ☐ | Dilnoza R. | Dilnoza R. |
| ☐ | Follow-up this week | Повторный приём на этой неделе |
| ☐ | Scheduled by you | Назначено вами |
| ☐ ⚕ | Example of the doctor's dashboard with demo data: three patients need you today; a program draft waits for your approval (step 2), marked as an AI suggestion; a new patient-reported report (step 3); a follow-up this week. | Пример панели врача на демонстрационных данных: сегодня вы нужны трём пациентам; черновик программы ждёт вашего утверждения (шаг 2) и помечен как предложение ИИ; новый отчёт со слов пациента (шаг 3); повторный приём на этой неделе. |
| ☐ ⚕ | What the AI does, and never does | Что ИИ делает и чего никогда не делает |
| ☐ ⚕ | Rehabilitation intelligence is in research for the pilot. | ИИ для реабилитации сейчас исследуется для пилотного проекта. |
| ☐ | research in progress | идёт исследование |
| ☐ | It does | Что делает |
| ☐ ⚕ | Drafts rehabilitation guidance from research papers the team has approved | Готовит черновики рекомендаций по реабилитации на основе научных статей, утверждённых командой |
| ☐ ⚕ | Shows the source of every point: paper, page or section | Показывает источник каждого пункта: статью, страницу или раздел |
| ☐ ⚕ | Says so when the papers don't cover a question | Сообщает, если статьи не отвечают на вопрос |
| ☐ ⚕ | Marks every draft as a suggestion, kept apart from approved care | Помечает каждый черновик как предложение и хранит его отдельно от утверждённого лечения |
| ☐ | It never | Никогда |
| ☐ ⚕ | Diagnoses | не ставит диагнозы |
| ☐ ⚕ | Prescribes or changes medication | не назначает и не меняет лекарства |
| ☐ | Approves a program | не утверждает программы |
| ☐ | Sends anything to a patient without you | ничего не отправляет пациенту без вас |
| ☐ | Workload, responsibility and data | Нагрузка, ответственность и данные |
| ☐ | Your workload | Ваша нагрузка |
| ☐ ⚕ | Coriva is being built to show only what needs you: patients who need a decision or sent a report. We won't promise time saved. That is one of the questions the pilot will answer. | Coriva создаётся, чтобы показывать только то, что требует вашего участия: пациентов, которым нужно решение или которые прислали отчёт. Мы не обещаем экономию времени. Это один из вопросов, на которые ответит пилотный проект. |
| ☐ | Responsibility | Ответственность |
| ☐ ⚕ | Clinical decisions stay yours, as today. Coriva will keep a record of what you approve and when, and patient reports will be marked as patient-reported, not clinical records. The pilot terms will be reviewed by lawyers before the pilot starts. | Клинические решения остаются за вами, как и сейчас. Coriva будет фиксировать, что и когда вы утвердили, и отчёты пациентов будут помечены как «со слов пациента», а не как клинические записи. Условия пилотного проекта проверят юристы до его начала. |
| ☐ | Your patients’ data | Данные ваших пациентов |
| ☐ | Each clinic's data is kept apart, access is by role, and development uses synthetic data only. An independent security review comes before the pilot. | Данные каждой клиники хранятся отдельно, доступ предоставляется по ролям, а при разработке используются только синтетические данные. Перед пилотным проектом пройдёт независимая проверка безопасности. |
| ☐ | How Coriva works: every part and its status | Как работает Coriva: каждая часть и её статус |
| ☐ | Questions from cardiologists | Вопросы кардиологов |
| ☐ | Is Coriva available now? | Coriva уже доступна? |
| ☐ | Not yet. Coriva is in development, and a pilot with selected doctors and clinics is in preparation. | Пока нет. Coriva в разработке, готовится пилотный проект с отобранными врачами и клиниками. |
| ☐ ⚕ | Which research does the AI use? | Какие исследования использует ИИ? |
| ☐ ⚕ | Only research papers the team has approved. Every suggestion shows its source, and the AI says so when the papers don't cover a question. | Только научные статьи, утверждённые командой. Каждое предложение показывает свой источник, а если статьи не отвечают на вопрос, ИИ так и сообщает. |
| ☐ ⚕ | What happens if a patient feels unwell? | Что происходит, если пациент плохо себя чувствует? |
| ☐ ⚕ | Coriva is not an emergency service. Patients are told to call their local emergency number. Their reports wait for your next review. | Coriva — не служба экстренной помощи. Пациентам сообщают, что нужно позвонить в скорую помощь (103). Их отчёты ждут вашего следующего просмотра. |
| ☐ | How do my patients join? | Как подключаются мои пациенты? |
| ☐ | Through you. You invite the patient; during the pilot, the app is activated at the clinic with staff present. There is no self sign-up. | Через вас. Вы приглашаете пациента; во время пилотного проекта приложение активируется в клинике, в присутствии персонала. Самостоятельной регистрации нет. |
| ☐ | What does the waitlist keep about me? | Какие данные обо мне хранятся в листе ожидания? |
| ☐ | Your name, work email, role, organisation and country, used only to contact you about the pilot. The details are in the privacy notice. | Ваше имя, рабочая электронная почта, роль, организация и страна — используются только для связи с вами по поводу пилотного проекта. Подробности — в политике конфиденциальности. |
| ☐ | Help shape the pilot. | Помогите сформировать пилотный проект. |
| ☐ | Join the waitlist as a cardiologist. We'll contact you about the pilot. | Запишитесь в лист ожидания как кардиолог. Мы свяжемся с вами по поводу пилотного проекта. |
| ☐ | Photograph: Shixart1985 (CC BY 2.0), via Wikimedia Commons. Product screens show demo data. | Фото: Shixart1985 (CC BY 2.0), через Wikimedia Commons. На экранах продукта — демонстрационные данные. |

## index.html

| ✓ | English | Russian |
|---|---|---|
| ☐ | Cardiac rehabilitation, continued at home. | Кардиореабилитация продолжается дома. |
| ☐ ⚕ | A clinically supervised platform for cardiologists, clinics and their patients. The doctor approves every plan. AI helps prepare it and fit it to each patient. | Платформа под клиническим контролем для кардиологов, клиник и их пациентов. Каждый план утверждает врач. ИИ помогает подготовить его и адаптировать к каждому пациенту. |
| ☐ | A day in their shoes. | Один день на их месте. |
| ☐ ⚕ | An older couple walking hand in hand along a path, one with a walking cane | Пожилая пара идёт по дорожке, держась за руки; один из них — с тростью |
| ☐ | See how it works | Посмотреть, как это работает |
| ☐ | Choose who you are, and see what a day with Coriva will look like. Times are an example; the plan always comes from the patient's own doctor. | Выберите, кто вы, и посмотрите, как будет выглядеть день с Coriva. Время указано для примера; план всегда составляет собственный врач пациента. |
| ☐ | a cardiologist | кардиолог |
| ☐ | a clinic leader | руководитель клиники |
| ☐ | a patient or family member | пациент или член его семьи |
| ☐ | a partner or investor | партнёр или инвестор |
| ☐ | A doctor's day | День врача |
| ☐ | See who needs you | Посмотрите, кому вы нужны |
| ☐ ⚕ | Only the patients who need a decision or sent a report. | Только пациенты, которым нужно решение или которые прислали отчёт. |
| ☐ | A doctor at her desk on a phone call, taking notes beside a laptop | Врач за рабочим столом говорит по телефону и делает записи рядом с ноутбуком |
| ☐ | Three patients need you today | Сегодня вы нужны трём пациентам |
| ☐ | Approve a draft | Утвердить черновик |
| ☐ ⚕ | AI drafted it from approved research. You edit and approve. | ИИ подготовил его на основе утверждённых исследований. Вы редактируете и утверждаете. |
| ☐ ⚕ | Draft plan with sources | Черновик плана с источниками |
| ☐ | Invite a new patient | Пригласить нового пациента |
| ☐ | Activation happens in your clinic, with staff present. | Активация проходит в вашей клинике, в присутствии персонала. |
| ☐ | Invite a patient | Пригласить пациента |
| ☐ | In the clinic, with staff present | В клинике, в присутствии персонала |
| ☐ | A report arrives | Приходит отчёт |
| ☐ ⚕ | It waits for your next review. Coriva is not an emergency service. | Отчёт ждёт вашего следующего просмотра. Coriva — не служба экстренной помощи. |
| ☐ | New report from Lola M. | Новый отчёт от Lola M. |
| ☐ | A clinic leader's week | Неделя руководителя клиники |
| ☐ | Mon | Понедельник |
| ☐ | See your team's patients | Смотрите пациентов вашей команды |
| ☐ | Who each doctor is caring for, in one view. | Кого ведёт каждый врач — на одном экране. |
| ☐ | Cardiology team | Команда кардиологов |
| ☐ | Three doctors, demo data | Три врача, демонстрационные данные |
| ☐ | Wed | Среда |
| ☐ | Hand over care | Передать пациента |
| ☐ ⚕ | When a doctor is away, another can take over, and it is recorded. | Когда врача нет на месте, его может заменить другой врач, и это фиксируется. |
| ☐ | Dr. B. Demo to Dr. A. Demo | Д-р Б. Демо → д-р А. Демо |
| ☐ | Thu | Четверг |
| ☐ | Support activation | Помощь с активацией |
| ☐ | Your staff help patients activate the app, in person. | Ваш персонал лично помогает пациентам активировать приложение. |
| ☐ | Activation code created | Код активации создан |
| ☐ | With staff present | В присутствии персонала |
| ☐ | Fri | Пятница |
| ☐ | Look back on the week | Подвести итоги недели |
| ☐ | Reporting for clinics comes in a later phase. | Отчётность для клиник появится на более позднем этапе. |
| ☐ | Later | Позже |
| ☐ | Clinic reporting | Отчётность для клиник |
| ☐ | A patient's day | День пациента |
| ☐ ⚕ | Morning medication | Утренний приём лекарств |
| ☐ | As your doctor entered it. Coriva never changes it. | Так, как ввёл ваш врач. Coriva никогда это не меняет. |
| ☐ ⚕ | Morning medication, as entered | Утренний приём лекарств, как указано |
| ☐ | Mark as taken | Отметить как принятое |
| ☐ | A walk | Прогулка |
| ☐ ⚕ | As long as your plan says, at your own pace. | Столько, сколько указано в вашем плане, в удобном для вас темпе. |
| ☐ ⚕ | Walk, as set in your plan | Прогулка, как указано в вашем плане |
| ☐ | Lunch | Обед |
| ☐ | From your nutrition tasks. | Из ваших заданий по питанию. |
| ☐ | Tell your doctor | Сообщить врачу |
| ☐ ⚕ | How the day went, in a minute. If you feel unwell, call your local emergency number. | Как прошёл день — за минуту. Если вы плохо себя чувствуете, позвоните в скорую помощь (103). |
| ☐ | How did today go? | Как прошёл день? |
| ☐ | Send report | Отправить отчёт |
| ☐ | A partner's timeline | Хронология для партнёра |
| ☐ | Now | Сейчас |
| ☐ | The doctor's dashboard, the patient app and a secure backend. | Панель врача, приложение для пациента и защищённая серверная часть. |
| ☐ | Secure backend | Защищённая серверная часть |
| ☐ | Data separated per clinic | Данные разделены по клиникам |
| ☐ | Next | Далее |
| ☐ | The pilot | Пилотный проект |
| ☐ | Selected doctors and clinics, and what we learn with them. | Отобранные врачи и клиники — и то, что мы узнаем вместе с ними. |
| ☐ | A small group | Небольшая группа |
| ☐ | Phase 2 | Этап 2 |
| ☐ | A doctors' mobile app, wearable data, clinic reporting. | Мобильное приложение для врачей, данные умных часов и фитнес-браслетов, отчётность для клиник. |
| ☐ | Doctors' app | Приложение для врачей |
| ☐ | Further | В перспективе |
| ☐ | Phase 3 | Этап 3 |
| ☐ ⚕ | Validated risk intelligence and broader platform tools. | Валидированная оценка рисков и расширенные инструменты платформы. |
| ☐ | Risk intelligence | Оценка рисков |
| ☐ ⚕ | Validated before clinical use | Валидация до клинического применения |
| ☐ | A grandfather holding his young granddaughter outside a house in evening light | Дедушка держит на руках маленькую внучку у дома в вечернем свете |
| ☐ | Recovery happens on ordinary days. | Восстановление происходит в обычные дни. |
| ☐ ⚕ | Most of rehabilitation takes place at home. Coriva keeps those days connected to the doctor who planned them, and the patient always knows who decides. | Большая часть реабилитации проходит дома. Coriva сохраняет связь этих дней с врачом, который их запланировал, а пациент всегда знает, кто принимает решения. |
| ☐ | What Coriva will never do | Чего Coriva никогда не будет делать |
| ☐ ⚕ | A doctor stays responsible for every clinical decision. These lines don't move. | За каждое клиническое решение отвечает врач. Эти границы не меняются. |
| ☐ ⚕ | Diagnose. | Ставить диагнозы. |
| ☐ ⚕ | Change a medication on its own. | Самостоятельно менять лекарства. |
| ☐ ⚕ | Let AI approve a plan. | Позволять ИИ утверждать план. |
| ☐ ⚕ | Pretend to be an emergency service. | Выдавать себя за службу экстренной помощи. |
| ☐ | Show a number we can't stand behind. | Показывать число, за которое мы не можем поручиться. |
| ☐ ⚕ | If you feel unwell, call your local emergency number. | Если вы плохо себя чувствуете, позвоните в скорую помощь (103). |
| ☐ | Where Coriva is today | Где Coriva сейчас |
| ☐ | Demo | Демо |
| ☐ | Supervised activation, care relationships and clinic teams, the doctor's dashboard, the patient app's sign-in, data separated per clinic. | Активация под контролем, связи врач — пациент и команды клиник, панель врача, вход в приложение для пациента, разделение данных по клиникам. |
| ☐ ⚕ | Doctor-approved plans, medication schedules from the doctor, AI drafts for review, daily patient reports. | Планы, утверждённые врачом, графики приёма лекарств от врача, черновики ИИ на проверку, ежедневные отчёты пациентов. |
| ☐ ⚕ | Risk intelligence (validated first), wearable data, a doctors' mobile app, clinic reporting. | Оценка рисков (сначала — валидация), данные умных часов и фитнес-браслетов, мобильное приложение для врачей, отчётность для клиник. |
| ☐ | For partners and investors | Для партнёров и инвесторов |
| ☐ | Coriva is building one platform for supervised cardiac rehabilitation: a doctor's dashboard, a patient app and, later, tools for clinics, all on one secure backend. The aim is rehabilitation that continues after discharge, with the doctor in charge at every step. | Coriva создаёт единую платформу для контролируемой кардиореабилитации: панель врача, приложение для пациента, а позже — инструменты для клиник, всё на одной защищённой серверной части. Цель — реабилитация, которая продолжается после выписки, и врач руководит ею на каждом шаге. |
| ☐ | Contact the team | Связаться с командой |
| ☐ | Does it fit a cardiologist's day? | Вписывается ли это в рабочий день кардиолога? |
| ☐ | Is the plan easy to keep up at home? | Легко ли следовать плану дома? |
| ☐ | What should the doctor see first? | Что врач должен видеть в первую очередь? |
| ☐ | Help us answer these in the pilot | Помогите нам ответить на эти вопросы в пилотном проекте |
| ☐ | For cardiologists and clinics who want to supervise rehabilitation beyond discharge. No account and no commitment; we'll contact you about the pilot. Partners and investors can contact the team directly. | Для кардиологов и клиник, которые хотят контролировать реабилитацию и после выписки. Без учётной записи и без обязательств; мы свяжемся с вами по поводу пилотного проекта. Партнёры и инвесторы могут связаться с командой напрямую. |
| ☐ | Questions | Вопросы |
| ☐ ⚕ | Does AI make clinical decisions? | Принимает ли ИИ клинические решения? |
| ☐ ⚕ | No. AI may draft suggestions from research the clinical team has approved, and shows its sources. A doctor reviews and approves every patient's plan. | Нет. ИИ может готовить предложения на основе исследований, утверждённых клинической командой, и показывает свои источники. Каждый план пациента проверяет и утверждает врач. |
| ☐ ⚕ | Is Coriva an emergency service? | Coriva — служба экстренной помощи? |
| ☐ ⚕ | No. If you feel unwell, call your local emergency number. | Нет. Если вы плохо себя чувствуете, позвоните в скорую помощь (103). |
| ☐ | Photographs: bluesbby, Shixart1985 (CC BY 2.0), via Wikimedia Commons | Фото: bluesbby, Shixart1985 (CC BY 2.0), через Wikimedia Commons |

## medical-disclaimer.html

| ✓ | English | Russian |
|---|---|---|
| ☐ | Draft, pending legal review. | Черновик, ожидает юридической проверки. |
| ☐ | Legal pages | Правовые страницы |
| ☐ | On this page | На этой странице |
| ☐ | Legal pages: draft, pending legal review. | Правовые страницы: черновик, ожидает юридической проверки. |

## partners.html

| ✓ | English | Russian |
|---|---|---|
| ☐ ⚕ | Coriva is a clinically supervised cardiac rehabilitation platform where doctors retain clinical authority and AI supports decision-making, monitoring, and personalization. | Coriva — платформа кардиореабилитации под клиническим контролем: клинические полномочия остаются за врачами, а ИИ помогает в принятии решений, мониторинге и персонализации. |
| ☐ | One system for cardiac rehabilitation. | Единая система для кардиореабилитации. |
| ☐ | Six surfaces, one core | Шесть частей, одно ядро |
| ☐ | It connects cardiologists, clinics and patients in one system, so rehabilitation can continue after discharge under the doctor's supervision. | Платформа объединяет кардиологов, клиники и пациентов в одной системе, чтобы реабилитация могла продолжаться после выписки под наблюдением врача. |
| ☐ | Coriva core | Ядро Coriva |
| ☐ | One backend, one data model and one set of access rules for every surface. | Одна серверная часть, одна модель данных и один набор правил доступа для всех частей платформы. |
| ☐ | built | готово |
| ☐ | Surfaces | Части платформы |
| ☐ | Patient app | Приложение для пациента |
| ☐ | Android. The patient's daily plan, reminders and reports. | Android. Ежедневный план пациента, напоминания и отчёты. |
| ☐ | Doctor's web dashboard | Веб-панель врача |
| ☐ ⚕ | Patients who need a decision, approvals and follow-ups. | Пациенты, которым нужно решение, утверждения и повторные приёмы. |
| ☐ | Clinic section | Раздел клиники |
| ☐ | A clinic's team, roles and handover, inside the doctor's dashboard. | Команда клиники, роли и передача пациентов — внутри панели врача. |
| ☐ | Doctors' mobile app | Мобильное приложение для врачей |
| ☐ | Android, for doctors away from the desk. | Android — для врачей вдали от рабочего стола. |
| ☐ | Platform administration | Администрирование платформы |
| ☐ | Internal oversight and configuration. | Внутренний контроль и настройка. |
| ☐ | Public website | Публичный сайт |
| ☐ | This site. | Этот сайт. |
| ☐ | You are here | Вы здесь |
| ☐ | Technology | Технологии |
| ☐ | One backend for everything | Одна серверная часть для всего |
| ☐ | A modular Go service with shared API contracts. Every surface follows the same rules for access and data. | Модульный сервис на Go с общими контрактами API. Все части платформы следуют одним правилам доступа и работы с данными. |
| ☐ | Data kept apart per clinic | Данные каждой клиники хранятся отдельно |
| ☐ | PostgreSQL with row-level security, access by role, and a record of sensitive actions. | PostgreSQL с защитой на уровне строк, доступ по ролям и журнал важных действий. |
| ☐ ⚕ | AI that Coriva runs itself | ИИ, который Coriva запускает самостоятельно |
| ☐ ⚕ | Open models hosted by Coriva, answering only from approved research papers, with sources. No third-party AI service. | Открытые модели, размещённые Coriva, отвечают только на основе утверждённых научных статей, с указанием источников. Без сторонних ИИ-сервисов. |
| ☐ | Native and web apps | Нативные и веб-приложения |
| ☐ | Android (Kotlin) for patients; a web dashboard (Next.js) for doctors and clinics. | Android (Kotlin) для пациентов; веб-панель (Next.js) для врачей и клиник. |
| ☐ | Roadmap | План развития |
| ☐ | No dates yet. Each stage starts only after the one before it is validated. | Дат пока нет. Каждый этап начинается только после того, как предыдущий прошёл проверку. |
| ☐ | Being built now. | Создаётся сейчас. |
| ☐ | Secure backend and data separation | Защищённая серверная часть и разделение данных |
| ☐ | Patient app: sign-in, onboarding, home | Приложение для пациента: вход, первичная настройка, главный экран |
| ☐ | Supervised patient activation | Активация пациента под контролем |
| ☐ | Planned for the controlled pilot. | Запланировано для контролируемого пилотного проекта. |
| ☐ | A controlled pilot with selected doctors and clinics | Контролируемый пилотный проект с отобранными врачами и клиниками |
| ☐ | Doctor-approved rehabilitation programs | Программы реабилитации, утверждённые врачом |
| ☐ ⚕ | Medication schedule and reminders | График приёма лекарств и напоминания |
| ☐ | Progress reports | Отчёты о прогрессе |
| ☐ | Clinic teams | Команды клиник |
| ☐ ⚕ | Rehabilitation intelligence (research in progress) | ИИ для реабилитации (идёт исследование) |
| ☐ | Planned for a later phase. | Запланировано на более поздний этап. |
| ☐ | Phase 2: doctors' mobile app, wearable and phone data, clinic reporting | Этап 2: мобильное приложение для врачей, данные умных часов, фитнес-браслетов и телефона, отчётность для клиник |
| ☐ ⚕ | Phase 3: risk intelligence, validated before any clinical use; platform administration | Этап 3: оценка рисков — с валидацией до любого клинического применения; администрирование платформы |
| ☐ | Talk to the team. | Поговорите с командой. |
| ☐ | For partnerships and investment, contact the Coriva team. | По вопросам партнёрства и инвестиций свяжитесь с командой Coriva. |
| ☐ | Team | Команда |
| ☐ | We'll introduce the team here soon. | Скоро мы представим здесь команду. |

## patients.html

| ✓ | English | Russian |
|---|---|---|
| ☐ | For patients and families | Для пациентов и их семей |
| ☐ | Your doctor's plan, at home. | План вашего врача — у вас дома. |
| ☐ | Coriva is being built to help you follow the rehabilitation plan your doctor makes for you, day by day. It is not available yet. | Coriva создаётся, чтобы помогать вам день за днём следовать плану реабилитации, который составит для вас врач. Пока Coriva недоступна. |
| ☐ | What Coriva will help with | В чём поможет Coriva |
| ☐ | Your plan for each day | Ваш план на каждый день |
| ☐ ⚕ | Walks, exercise and meals, as your doctor planned them. | Прогулки, упражнения и питание — так, как запланировал ваш врач. |
| ☐ ⚕ | Medicine reminders | Напоминания о лекарствах |
| ☐ ⚕ | At the times your doctor entered. Coriva never changes your medicine. | В то время, которое указал ваш врач. Coriva никогда не меняет ваши лекарства. |
| ☐ | Telling your doctor how you are | Как сообщить врачу о своём самочувствии |
| ☐ | A short report that your doctor reads at their next review. | Короткий отчёт, который ваш врач читает при следующем просмотре отчётов. |
| ☐ | Your progress | Ваш прогресс |
| ☐ | What you have done so far, from your own reports. | Что вы уже сделали — по вашим собственным отчётам. |
| ☐ | How you join | Как вы подключаетесь |
| ☐ | Your doctor invites you | Ваш врач приглашает вас |
| ☐ | If Coriva is right for you, your doctor will offer it. | Если Coriva вам подходит, ваш врач предложит её. |
| ☐ | You start at the clinic | Вы начинаете в клинике |
| ☐ | Staff help you set up the app with a one-time code. | Персонал помогает вам настроить приложение с помощью одноразового кода. |
| ☐ | You follow your doctor’s plan | Вы следуете плану своего врача |
| ☐ ⚕ | Day by day, at home, at your own pace. | День за днём, дома, в своём темпе. |
| ☐ | You cannot sign up on this website. | На этом сайте нельзя зарегистрироваться. |
| ☐ ⚕ | Coriva is not an emergency service. | Coriva — не служба экстренной помощи. |
| ☐ ⚕ | Coriva does not watch you all the time. Your doctor reads your reports at their next review. | Coriva не следит за вами постоянно. Ваш врач читает ваши отчёты при следующем просмотре. |
| ☐ | Your information | Ваши данные |
| ☐ | Your doctor sees what you share. | Ваш врач видит то, чем вы делитесь. |
| ☐ ⚕ | If your doctor is away, a colleague at the same clinic may look after you. This change is recorded. | Если вашего врача нет на месте, вас может вести его коллега из той же клиники. Это изменение фиксируется. |
| ☐ ⚕ | Your reports are your own words, not a medical record. | Ваши отчёты — это ваши собственные слова, а не медицинская документация. |
| ☐ | Your clinic's information is kept apart from other clinics. | Данные вашей клиники хранятся отдельно от других клиник. |
| ☐ | Questions from patients and families | Вопросы пациентов и их семей |
| ☐ | Can I sign up myself? | Можно ли зарегистрироваться самостоятельно? |
| ☐ | No. Your doctor invites you. This keeps your care in your doctor’s hands. | Нет. Вас приглашает ваш врач. Так ваше лечение остаётся в руках вашего врача. |
| ☐ ⚕ | Will Coriva change my medicine? | Будет ли Coriva менять мои лекарства? |
| ☐ ⚕ | No. Only your doctor decides about your medicine. Coriva reminds you of what your doctor entered. | Нет. Решения о ваших лекарствах принимает только ваш врач. Coriva напоминает о том, что ввёл ваш врач. |
| ☐ ⚕ | Does a computer decide my treatment? | Решает ли компьютер, как меня лечить? |
| ☐ ⚕ | No. Your doctor decides. Coriva may help your doctor prepare a plan, but your doctor checks and approves it. | Нет. Решает ваш врач. Coriva может помочь вашему врачу подготовить план, но ваш врач проверяет и утверждает его. |
| ☐ | What if I miss a day? | Что, если я пропущу день? |
| ☐ ⚕ | That is all right. Tell your doctor in your report. Your doctor decides if anything should change. | Ничего страшного. Расскажите об этом врачу в отчёте. Нужно ли что-то менять, решает ваш врач. |
| ☐ | Which phones will it work on? | На каких телефонах будет работать приложение? |
| ☐ | At first, Android phones. | Сначала — телефоны на Android. |
| ☐ | Questions about your care? | Есть вопросы о лечении? |
| ☐ | Ask your doctor. They know your plan. | Спросите своего врача. Он знает ваш план. |
| ☐ ⚕ | Read the medical disclaimer | Прочитать медицинское предупреждение |
| ☐ | Photograph: Shixart1985 (CC BY 2.0), via Wikimedia Commons. People shown are not Coriva patients. | Фото: Shixart1985 (CC BY 2.0), через Wikimedia Commons. Люди на фото не являются пациентами Coriva. |

## platform.html

| ✓ | English | Russian |
|---|---|---|
| ☐ | How Coriva works. | Как работает Coriva. |
| ☐ ⚕ | Follow one rehabilitation program from research to a patient's day, and see where the doctor decides. Every step shows its status today. | Проследите путь одной программы реабилитации — от исследования до дня пациента — и посмотрите, где решение принимает врач. Для каждого шага указан его статус на сегодня. |
| ☐ ⚕ | From research to a patient's day | От исследования ко дню пациента |
| ☐ ⚕ | An example with demo data. The doctor decides at step 3, and again at every review. | Пример на демонстрационных данных. Врач принимает решение на шаге 3 и снова — при каждом просмотре отчётов. |
| ☐ | Status labels | Обозначения статусов |
| ☐ | Approved research | Утверждённые исследования |
| ☐ ⚕ | The team approves the research papers Coriva may use. Nothing else goes in. | Команда утверждает научные статьи, которые может использовать Coriva. Больше ничего не добавляется. |
| ☐ | Status | Статус |
| ☐ | Who decides | Кто решает |
| ☐ ⚕ | The Coriva team approves each paper. | Каждую статью утверждает команда Coriva. |
| ☐ | Approved paper | Утверждённая статья |
| ☐ | Cardiac rehabilitation · example | Кардиореабилитация · пример |
| ☐ | Section 4 | Раздел 4 |
| ☐ ⚕ | Used as a source | Использован как источник |
| ☐ | An AI draft | Черновик ИИ |
| ☐ ⚕ | AI drafts rehabilitation guidance for one patient from those papers, with the source of every point. If the papers don't support it, it says so. | ИИ составляет черновик рекомендаций по реабилитации для одного пациента на основе этих статей, с источником для каждого пункта. Если статьи этого не подтверждают, он так и говорит. |
| ☐ | No one yet. It is only a suggestion. | Пока никто. Это только предложение. |
| ☐ ⚕ | Walking plan · source: approved paper, section 4 | План ходьбы · источник: утверждённая статья, раздел 4 |
| ☐ | The doctor decides | Решает врач |
| ☐ ⚕ | The doctor reads the draft, edits it, and approves or rejects it. The program reaches the patient only after approval. | Врач читает черновик, редактирует его, а затем утверждает или отклоняет. Программа поступает пациенту только после утверждения. |
| ☐ | The patient's doctor. | Врач пациента. |
| ☐ | Program draft | Черновик программы |
| ☐ | Edited by you | Отредактировано вами |
| ☐ | The patient's day | День пациента |
| ☐ ⚕ | The patient sees the approved plan: activity, nutrition, and medication exactly as the doctor entered it. | Пациент видит утверждённый план: физическую активность, питание и лекарства — точно так, как их ввёл врач. |
| ☐ | plans | планы |
| ☐ | the app | приложение |
| ☐ ⚕ | The doctor's plan. Coriva never changes medication. | План врача. Coriva никогда не меняет лекарства. |
| ☐ ⚕ | Approved by your doctor | Утверждено вашим врачом |
| ☐ | A report | Отчёт |
| ☐ ⚕ | The patient tells the doctor how the day went. If they feel unwell, they call their local emergency number. | Пациент сообщает врачу, как прошёл день. Если он плохо себя чувствует, он звонит в скорую помощь (103). |
| ☐ | The patient. | Пациент. |
| ☐ | The next review | Следующий просмотр отчётов |
| ☐ ⚕ | Reports wait for the doctor's next review. The doctor adjusts the program when needed. | Отчёты ждут следующего просмотра врачом. При необходимости врач корректирует программу. |
| ☐ | The doctor. | Врач. |
| ☐ | Patient-reported · demo data | Со слов пациента · демонстрационные данные |
| ☐ | Everything, with its status | Всё — с указанием статуса |
| ☐ | Each part, and what the doctor controls. | Каждая часть — и то, что контролирует врач. |
| ☐ | Supervised activation | Активация под контролем |
| ☐ ⚕ | Decides who is invited. Patients cannot sign up on their own. | Решает, кого пригласить. Пациенты не могут зарегистрироваться самостоятельно. |
| ☐ | Care relationships and handover | Связи врач — пациент и передача пациентов |
| ☐ | Sees only the patients in their care. | Видит только тех пациентов, которых ведёт. |
| ☐ | Doctor's dashboard | Панель врача |
| ☐ ⚕ | Decides every next step. | Определяет каждый следующий шаг. |
| ☐ | · membership and handover | · участники и передача пациентов |
| ☐ ⚕ | Clinic leaders manage the team. Clinical decisions stay with each patient's doctor. | Руководители клиник управляют командой. Клинические решения остаются за врачом каждого пациента. |
| ☐ | Patient app (Android) | Приложение для пациента (Android) |
| ☐ ⚕ | The app shows only what the doctor approved. | Приложение показывает только то, что утвердил врач. |
| ☐ | Privacy and security foundation | Основа конфиденциальности и безопасности |
| ☐ | Every sensitive action is recorded. | Каждое важное действие фиксируется. |
| ☐ | · clinic screens | · экраны для клиник |
| ☐ | Rehabilitation programs | Программы реабилитации |
| ☐ ⚕ | Creates, edits and approves every program. Nothing reaches the patient before approval. | Создаёт, редактирует и утверждает каждую программу. До утверждения пациенту ничего не поступает. |
| ☐ ⚕ | Enters the schedule. Coriva and its AI never change it. | Вводит график. Coriva и её ИИ никогда его не меняют. |
| ☐ ⚕ | Reviews reports at the next review. They are not watched in real time. | Читает отчёты при следующем просмотре. Они не отслеживаются в реальном времени. |
| ☐ | Rehabilitation intelligence | ИИ для реабилитации |
| ☐ ⚕ | Reviews, edits, approves or rejects every draft. | Проверяет, редактирует, утверждает или отклоняет каждый черновик. |
| ☐ | Not used in care before validation. | Не применяется в лечении до валидации. |
| ☐ | Wearable and phone data | Данные умных часов, фитнес-браслетов и телефона |
| ☐ | Not yet defined. | Пока не определено. |
| ☐ | Oversight, privacy and security | Контроль, конфиденциальность и безопасность |
| ☐ | Clinical oversight | Клинический контроль |
| ☐ ⚕ | Clinical rules are reviewed | Клинические правила проходят проверку |
| ☐ ⚕ | Any clinical rule or threshold is reviewed by a qualified cardiologist before it is used. | Любое клиническое правило или пороговое значение проверяет квалифицированный кардиолог до того, как оно начнёт применяться. |
| ☐ ⚕ | The other rules are in the steps above: the doctor approves every program (step 3), medication stays as entered (step 4), and reports wait for the doctor's review (step 6). Coriva is not an emergency service. | Остальные правила — в шагах выше: каждую программу утверждает врач (шаг 3), лекарства остаются такими, как их ввели (шаг 4), а отчёты ждут просмотра врачом (шаг 6). Coriva — не служба экстренной помощи. |
| ☐ | Built now | Создаётся сейчас |
| ☐ | Each clinic's data is kept apart, enforced in the database | Данные каждой клиники хранятся отдельно — это обеспечивается на уровне базы данных |
| ☐ | Access by role: doctor, clinic leader, patient | Доступ по ролям: врач, руководитель клиники, пациент |
| ☐ | Single-use activation codes, given in person | Одноразовые коды активации, выдаваемые лично |
| ☐ | A record of sensitive actions | Журнал важных действий |
| ☐ | Synthetic data only during development | Только синтетические данные во время разработки |
| ☐ | Before the pilot | До пилотного проекта |
| ☐ | An independent security review | Независимая проверка безопасности |
| ☐ ⚕ | AI on open models Coriva runs itself, not a third-party AI service | ИИ на открытых моделях, которые Coriva запускает самостоятельно, а не сторонний ИИ-сервис |
| ☐ | Privacy notice and terms, reviewed by lawyers | Политика конфиденциальности и условия, проверенные юристами |
| ☐ ⚕ | How the AI is being built | Как создаётся ИИ |
| ☐ ⚕ | Rehabilitation intelligence is in research for the pilot. It is built to six rules. | ИИ для реабилитации сейчас исследуется для пилотного проекта. Он строится по шести правилам. |
| ☐ | Approved research only | Только утверждённые исследования |
| ☐ ⚕ | The AI works only from research papers the team has approved, not from the open internet. | ИИ работает только с научными статьями, утверждёнными командой, а не с открытым интернетом. |
| ☐ | Always cited | Всегда с источником |
| ☐ ⚕ | Every point shows its source: the paper, page or section. | Для каждого пункта указан источник: статья, страница или раздел. |
| ☐ | Says when it doesn't know | Говорит, когда не знает |
| ☐ ⚕ | If the papers don't support an answer, it says so and stops. | Если статьи не подтверждают ответ, он сообщает об этом и останавливается. |
| ☐ | Labelled as a suggestion | Помечено как предложение |
| ☐ ⚕ | Drafts look different from approved care and are never shown to patients as instructions. | Черновики выглядят иначе, чем утверждённое лечение, и никогда не показываются пациентам как инструкции. |
| ☐ ⚕ | Nothing reaches a patient until the doctor approves it. | Пациент ничего не получит, пока врач это не утвердит. |
| ☐ ⚕ | Never diagnoses | Никогда не ставит диагнозы |
| ☐ ⚕ | It does not diagnose, prescribe, or change medication. | ИИ не ставит диагнозы, не назначает лекарства и не меняет их. |
| ☐ | Cardiologists and clinics can join the waitlist. We'll contact you about the pilot. | Кардиологи и клиники могут записаться в лист ожидания. Мы свяжемся с вами по поводу пилотного проекта. |
| ☐ | Product screens show demo data. | На экранах продукта — демонстрационные данные. |

## privacy.html

| ✓ | English | Russian |
|---|---|---|
| ☐ | This page is not in force. The text will be written and reviewed by a lawyer before the website is published. | Эта страница не имеет силы. Текст будет написан и проверен юристом до публикации сайта. |
| ☐ | Who is responsible for your information | Кто отвечает за ваши данные |
| ☐ | What we collect | Что мы собираем |
| ☐ | Why we use it | Зачем мы их используем |
| ☐ | How long we keep it | Сколько мы храним данные |
| ☐ | Where it is stored | Где хранятся данные |
| ☐ | Your rights | Ваши права |

## waitlist.html

| ✓ | English | Russian |
|---|---|---|
| ☐ | Join the Coriva pilot waitlist. | Запишитесь в лист ожидания пилотного проекта Coriva. |
| ☐ | For cardiologists, clinics, partners and investors. | Для кардиологов, клиник, партнёров и инвесторов. |
| ☐ | What happens next | Что дальше |
| ☐ | You join | Вы записываетесь |
| ☐ | Choose your role and enter your work details. | Выберите роль и укажите рабочие данные. |
| ☐ | You confirm | Вы подтверждаете |
| ☐ | We send one email. Press Confirm in it to join the list. | Мы отправляем одно письмо. Нажмите в нём «Подтвердить», чтобы попасть в список. |
| ☐ | We contact you | Мы связываемся с вами |
| ☐ | When pilot places open, we contact confirmed participants by email. | Когда откроются места в пилотном проекте, мы свяжемся с подтвердившими участниками по электронной почте. |
| ☐ | The pilot waitlist opens soon. | Лист ожидания пилотного проекта скоро откроется. |
| ☐ | and agree that Coriva uses these details to contact me about the pilot. | и согласен(-на) с тем, что Coriva использует эти данные, чтобы связаться со мной по поводу пилотного проекта. |
| ☐ | Join the waitlist | Записаться в лист ожидания |
| ☐ | What we keep | Что мы храним |
| ☐ | Your role, name, work email, organisation and country, and your message if you write one. Used only to contact you about the pilot. No marketing email; withdraw at any time with the link in the email. Details in the | Ваша роль, имя, рабочая электронная почта, организация и страна, а также ваше сообщение, если вы его напишете. Используются только для связи с вами по поводу пилотного проекта. Никаких рекламных писем; выйти из списка можно в любое время по ссылке в письме. Подробнее см. |
