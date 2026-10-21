# Polityka prywatności AllPass Training w trzech językach.
# {company}, {address}, {nip}, {email} są uzupełniane w build.py.
# Każda sekcja: (nagłówek, [akapity lub listy w HTML]).

PL = dict(
    title="Polityka prywatności",
    meta_desc="Jak AllPass Training przetwarza dane osobowe osób, które odwiedzają stronę i wysyłają zapytania o kursy.",
    updated="Obowiązuje od: {date}",
    intro="Tu opisujemy, jakie dane zbieramy przez stronę allpass.pl, w jakim celu, komu je przekazujemy i jakie masz prawa. Stosujemy rozporządzenie RODO (UE 2016/679).",
    sections=[
        ("Administrator danych", [
            "Administratorem Twoich danych osobowych jest {company}, {address}, NIP {nip} (dalej: „AllPass”, „my”).",
            "We wszystkich sprawach dotyczących danych osobowych napisz do nas: <a href=\"mailto:{email}\">{email}</a>. Nie powołaliśmy inspektora ochrony danych.",
        ]),
        ("Jakie dane zbieramy", [
            "<strong>Dane z formularza:</strong> imię i nazwisko, telefon lub e-mail, wybrany kurs, liczba osób, język i miejsce szkolenia oraz treść wiadomości. Podanie danych jest dobrowolne, ale bez imienia i telefonu albo e-maila nie odpowiemy na zapytanie.",
            "<strong>Korespondencja:</strong> dane, które podasz, pisząc do nas e-mailem lub dzwoniąc.",
            "<strong>Dane techniczne:</strong> przy każdym wejściu na stronę serwer hostingu zapisuje w logach m.in. adres IP, datę i godzinę oraz informacje o przeglądarce. Służą one bezpieczeństwu i działaniu serwisu.",
            "Dane potrzebne do zapisu na egzamin UDT (np. PESEL, data i miejsce urodzenia) zbieramy dopiero przy zapisie na kurs, nie przez stronę.",
        ]),
        ("Cele i podstawy prawne", [
            "<ul><li>Odpowiedź na zapytanie i przygotowanie oferty, na Twoje żądanie, przed zawarciem umowy: art. 6 ust. 1 lit. b RODO.</li>"
            "<li>Odpowiedź na zapytanie złożone w imieniu firmy i dalszy kontakt z jej przedstawicielem: nasz prawnie uzasadniony interes, czyli prowadzenie korespondencji, art. 6 ust. 1 lit. f RODO.</li>"
            "<li>Realizacja umowy szkolenia i zgłoszenie na egzamin, jeśli zapiszesz się na kurs: art. 6 ust. 1 lit. b RODO.</li>"
            "<li>Wypełnienie obowiązków prawnych, np. księgowych i podatkowych: art. 6 ust. 1 lit. c RODO.</li>"
            "<li>Ustalenie, dochodzenie lub obrona roszczeń oraz zapewnienie bezpieczeństwa strony: nasz prawnie uzasadniony interes, art. 6 ust. 1 lit. f RODO.</li></ul>",
            "Nie wysyłamy newslettera ani informacji handlowych bez Twojej osobnej zgody. Nie profilujemy i nie podejmujemy decyzji w sposób zautomatyzowany.",
        ]),
        ("Komu przekazujemy dane", [
            "Korzystamy z usług zaufanych dostawców, którzy przetwarzają dane w naszym imieniu na podstawie umów powierzenia:",
            "<ul><li><strong>GitHub, Inc.</strong> (USA): hosting strony, w tym logi serwera.</li>"
            "<li><strong>Formspree, Inc.</strong> (USA): przekazanie wiadomości z formularza na naszą skrzynkę e-mail.</li>"
            "<li><strong>BunnyWay d.o.o.</strong> (Słowenia, UE): dostarczanie czcionek strony (bunny.net). Usługa nie zapisuje adresów IP odwiedzających.</li>"
            "<li><strong>Dostawca poczty e-mail</strong>, na którym działa skrzynka {email}.</li>"
            "<li>Przy zapisie na kurs: <strong>Urząd Dozoru Technicznego</strong>, który przeprowadza egzamin, oraz, jeśli o to poprosisz, współpracujący z nami tłumacz.</li>"
            "<li>Biuro rachunkowe i podmioty uprawnione z mocy prawa.</li></ul>",
        ]),
        ("Przekazywanie danych poza Europejski Obszar Gospodarczy", [
            "GitHub i Formspree mają siedzibę w USA, więc część danych może trafić poza EOG. Przekazanie odbywa się na podstawie decyzji Komisji Europejskiej w sprawie EU-US Data Privacy Framework (jeśli dostawca jest w nim certyfikowany) albo standardowych klauzul umownych zatwierdzonych przez Komisję. Kopię zabezpieczeń możesz otrzymać, pisząc na {email}.",
        ]),
        ("Jak długo przechowujemy dane", [
            "<ul><li>Zapytania, które nie zakończyły się zapisem na kurs: do 12 miesięcy od ostatniego kontaktu.</li>"
            "<li>Dane uczestników kursów: przez czas trwania umowy, a potem do upływu terminów przedawnienia roszczeń.</li>"
            "<li>Dokumenty księgowe: 5 lat od końca roku, w którym minął termin płatności podatku.</li>"
            "<li>Logi serwera: zgodnie z polityką GitHub, zwykle przez krótki okres potrzebny do zapewnienia bezpieczeństwa.</li></ul>",
        ]),
        ("Twoje prawa", [
            "Masz prawo do dostępu do swoich danych, ich sprostowania, usunięcia lub ograniczenia przetwarzania, przeniesienia danych oraz wniesienia sprzeciwu wobec przetwarzania opartego na naszym prawnie uzasadnionym interesie. Aby skorzystać z tych praw, napisz na {email}.",
            "Masz też prawo wnieść skargę do Prezesa Urzędu Ochrony Danych Osobowych, ul. Stawki 2, 00-193 Warszawa (uodo.gov.pl).",
        ]),
        ("Pliki cookies", [
            "Strona nie używa plików cookies ani podobnych technologii zapisujących informacje na Twoim urządzeniu. Nie korzystamy z narzędzi analitycznych ani reklamowych. Dlatego nie wyświetlamy baneru zgody na cookies.",
            "Jeśli w przyszłości dodamy takie narzędzia, najpierw poprosimy Cię o zgodę i zaktualizujemy tę politykę.",
        ]),
        ("Zmiany polityki", [
            "Możemy aktualizować tę politykę, np. gdy zmienimy dostawców usług. Aktualna wersja jest zawsze dostępna na tej stronie, z datą obowiązywania na górze.",
        ]),
    ],
)

EN = dict(
    title="Privacy policy",
    meta_desc="How AllPass Training processes the personal data of website visitors and people who send course enquiries.",
    updated="Effective from: {date}",
    intro="This policy explains what data we collect through allpass.pl, why, who we share it with and what rights you have. We apply the General Data Protection Regulation (EU 2016/679, GDPR). The Polish version of this policy prevails.",
    sections=[
        ("Data controller", [
            "The controller of your personal data is {company}, {address}, NIP (tax ID) {nip} (“AllPass”, “we”).",
            "For any matter concerning personal data, write to <a href=\"mailto:{email}\">{email}</a>. We have not appointed a data protection officer.",
        ]),
        ("What data we collect", [
            "<strong>Form data:</strong> name, phone or email, chosen course, number of people, language and location of training, and your message. Providing data is voluntary, but without a name and a phone number or email we cannot reply.",
            "<strong>Correspondence:</strong> data you give us when you email or call us.",
            "<strong>Technical data:</strong> on every visit the hosting server logs your IP address, date and time and browser information. These logs keep the site secure and working.",
            "Data needed to register you for the UDT exam (e.g. PESEL number, date and place of birth) is collected only when you sign up for a course, not through this website.",
        ]),
        ("Purposes and legal bases", [
            "<ul><li>Replying to your enquiry and preparing an offer at your request before a contract: Art. 6(1)(b) GDPR.</li>"
            "<li>Replying to an enquiry made on behalf of a company and keeping in touch with its representative: our legitimate interest in handling correspondence, Art. 6(1)(f) GDPR.</li>"
            "<li>Performing the training contract and registering you for the exam if you sign up: Art. 6(1)(b) GDPR.</li>"
            "<li>Meeting legal obligations such as accounting and tax: Art. 6(1)(c) GDPR.</li>"
            "<li>Establishing, pursuing or defending claims and keeping the site secure: our legitimate interest, Art. 6(1)(f) GDPR.</li></ul>",
            "We do not send newsletters or marketing without your separate consent. We do not profile you or make automated decisions.",
        ]),
        ("Who we share data with", [
            "We use trusted providers that process data on our behalf under data processing agreements:",
            "<ul><li><strong>GitHub, Inc.</strong> (USA): website hosting, including server logs.</li>"
            "<li><strong>Formspree, Inc.</strong> (USA): delivering form messages to our mailbox.</li>"
            "<li><strong>BunnyWay d.o.o.</strong> (Slovenia, EU): serving the website fonts (bunny.net). The service does not log visitors' IP addresses.</li>"
            "<li><strong>Our email provider</strong> hosting the {email} mailbox.</li>"
            "<li>When you sign up for a course: the <strong>Office of Technical Inspection (UDT)</strong>, which runs the exam, and, if you ask for one, an interpreter we work with.</li>"
            "<li>Our accountants and authorities entitled by law.</li></ul>",
        ]),
        ("Transfers outside the European Economic Area", [
            "GitHub and Formspree are based in the USA, so some data may leave the EEA. Transfers rely on the European Commission's adequacy decision on the EU-US Data Privacy Framework (where the provider is certified) or on the Commission's standard contractual clauses. You can request a copy of the safeguards at {email}.",
        ]),
        ("How long we keep data", [
            "<ul><li>Enquiries that did not lead to a course: up to 12 months after the last contact.</li>"
            "<li>Course participants' data: for the duration of the contract and then until claims become time-barred.</li>"
            "<li>Accounting records: 5 years from the end of the year in which the tax payment deadline passed.</li>"
            "<li>Server logs: according to GitHub's policy, usually for a short period needed for security.</li></ul>",
        ]),
        ("Your rights", [
            "You have the right to access your data, to rectify, erase or restrict it, to data portability and to object to processing based on our legitimate interest. To use these rights, write to {email}.",
            "You may also lodge a complaint with the Polish supervisory authority: President of the Personal Data Protection Office (UODO), ul. Stawki 2, 00-193 Warsaw (uodo.gov.pl).",
        ]),
        ("Cookies", [
            "This website does not use cookies or similar technologies that store information on your device. We use no analytics or advertising tools, so there is no cookie consent banner.",
            "If we add such tools in the future, we will ask for your consent first and update this policy.",
        ]),
        ("Changes to this policy", [
            "We may update this policy, for example when we change service providers. The current version is always on this page, with its effective date at the top.",
        ]),
    ],
)

UK = dict(
    title="Політика конфіденційності",
    meta_desc="Як AllPass Training обробляє персональні дані відвідувачів сайту та осіб, які надсилають запити щодо курсів.",
    updated="Діє з: {date}",
    intro="Тут ми пояснюємо, які дані збираємо через сайт allpass.pl, з якою метою, кому їх передаємо і які у вас права. Ми застосовуємо Загальний регламент захисту даних (ЄС 2016/679, RODO/GDPR). Переважну силу має польська версія цієї політики.",
    sections=[
        ("Адміністратор даних", [
            "Адміністратором ваших персональних даних є {company}, {address}, NIP {nip} (далі «AllPass», «ми»).",
            "З усіх питань щодо персональних даних пишіть на <a href=\"mailto:{email}\">{email}</a>. Ми не призначали інспектора із захисту даних.",
        ]),
        ("Які дані ми збираємо", [
            "<strong>Дані з форми:</strong> ім’я та прізвище, телефон або e-mail, обраний курс, кількість осіб, мова й місце навчання та текст повідомлення. Надання даних добровільне, але без імені та телефону чи e-mail ми не зможемо відповісти.",
            "<strong>Листування:</strong> дані, які ви надаєте, коли пишете нам або телефонуєте.",
            "<strong>Технічні дані:</strong> під час кожного відвідування сервер хостингу записує в журнали IP-адресу, дату й час та відомості про браузер. Вони потрібні для безпеки та роботи сайту.",
            "Дані для реєстрації на іспит UDT (напр. номер PESEL, дата й місце народження) ми збираємо лише під час запису на курс, а не через сайт.",
        ]),
        ("Мета та правові підстави", [
            "<ul><li>Відповідь на запит і підготовка пропозиції на ваше прохання до укладення договору: ст. 6(1)(b) GDPR.</li>"
            "<li>Відповідь на запит від імені компанії та подальший контакт з її представником: наш законний інтерес у веденні листування, ст. 6(1)(f) GDPR.</li>"
            "<li>Виконання договору про навчання та реєстрація на іспит, якщо ви записалися на курс: ст. 6(1)(b) GDPR.</li>"
            "<li>Виконання юридичних обов’язків, напр. бухгалтерських і податкових: ст. 6(1)(c) GDPR.</li>"
            "<li>Встановлення, пред’явлення чи захист претензій і безпека сайту: наш законний інтерес, ст. 6(1)(f) GDPR.</li></ul>",
            "Ми не надсилаємо розсилок чи реклами без вашої окремої згоди. Ми не здійснюємо профілювання та автоматизованого ухвалення рішень.",
        ]),
        ("Кому ми передаємо дані", [
            "Ми користуємося послугами надійних постачальників, які обробляють дані від нашого імені на підставі договорів доручення:",
            "<ul><li><strong>GitHub, Inc.</strong> (США): хостинг сайту, зокрема журнали сервера.</li>"
            "<li><strong>Formspree, Inc.</strong> (США): доставка повідомлень із форми на нашу пошту.</li>"
            "<li><strong>BunnyWay d.o.o.</strong> (Словенія, ЄС): шрифти сайту (bunny.net). Сервіс не зберігає IP-адреси відвідувачів.</li>"
            "<li><strong>Постачальник електронної пошти</strong> скриньки {email}.</li>"
            "<li>Під час запису на курс: <strong>Управління технічного нагляду (UDT)</strong>, яке проводить іспит, а також, на ваше прохання, перекладач, з яким ми співпрацюємо.</li>"
            "<li>Бухгалтерія та органи, уповноважені законом.</li></ul>",
        ]),
        ("Передача даних за межі Європейської економічної зони", [
            "GitHub і Formspree розташовані в США, тому частина даних може залишати ЄЕЗ. Передача відбувається на підставі рішення Європейської комісії щодо EU-US Data Privacy Framework (якщо постачальник сертифікований) або стандартних договірних положень, затверджених Комісією. Копію гарантій можна отримати, написавши на {email}.",
        ]),
        ("Як довго ми зберігаємо дані", [
            "<ul><li>Запити, які не завершилися записом на курс: до 12 місяців від останнього контакту.</li>"
            "<li>Дані учасників курсів: протягом дії договору, а потім до спливу строків позовної давності.</li>"
            "<li>Бухгалтерські документи: 5 років від кінця року, в якому минув строк сплати податку.</li>"
            "<li>Журнали сервера: згідно з політикою GitHub, зазвичай короткий час, потрібний для безпеки.</li></ul>",
        ]),
        ("Ваші права", [
            "Ви маєте право на доступ до своїх даних, їх виправлення, видалення чи обмеження обробки, перенесення даних, а також право заперечити проти обробки на підставі нашого законного інтересу. Щоб скористатися цими правами, напишіть на {email}.",
            "Ви також можете подати скаргу до польського наглядового органу: Голова Управління з питань захисту персональних даних (UODO), ul. Stawki 2, 00-193 Варшава (uodo.gov.pl).",
        ]),
        ("Файли cookies", [
            "Сайт не використовує файли cookies чи подібні технології, що зберігають інформацію на вашому пристрої. Ми не використовуємо аналітичних чи рекламних інструментів, тому банера згоди на cookies немає.",
            "Якщо в майбутньому ми додамо такі інструменти, спершу попросимо вашої згоди й оновимо цю політику.",
        ]),
        ("Зміни політики", [
            "Ми можемо оновлювати цю політику, напр. коли змінюємо постачальників послуг. Чинна версія завжди доступна на цій сторінці з датою набрання чинності вгорі.",
        ]),
    ],
)
