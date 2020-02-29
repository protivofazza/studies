import pickle


print("Запущено на виконання програму 'Адресна книга'")


def create_contact():
    new_contact_def = [0,
                       'Прізвище', "Ім'я", 'По батькові',
                       'ПІБ',  # Внутрішньопрограмний рядок для організації зручного сортування
                       'Адреса',
                       ['E-Mail_1', 'E-Mail_2'],
                       ['333-33-33', '777-77-77'],
                       {'Viber': '333-33-33', 'Messenger': '777-77-77', 'Telegram': 'mavka-lisova'},
                       ]
    default_dict = {'Viber': '333-33-33', 'Messenger': '777-77-77', 'Telegram': 'mavka-lisova'}
    print('Розпочнемо з вводу ПІБ:\n')
    try:
        new_contact_def[0] = max(address_book_list)[0] + 1
    except ValueError:
        new_contact_def[0] = 1
    new_contact_def[1] = input('Введіть прізвище: ')
    new_contact_def[2] = input("Введіть ім'я: ")
    new_contact_def[3] = input('Введіть по-батькові (якщо немає - введіть пустий рядок, просто натиснувши Enter): ')
    new_contact_def[4] = new_contact_def[1] + ' ' + new_contact_def[2] + ' ' + new_contact_def[3]
    new_contact_def[5] = input(
        "\nВведіть поштову адресу у фоматі 'Країна', 'Місто', 'буд.', 'кв.', 'поштовий індекс': ")
    new_contact_def[6] = input_email()  # введення списку E-Mail
    new_contact_def[7] = input_phone_num()  # введення списку телефонних ноиерів
    new_contact_def[8] = input_messenger(default_dict)  # введення списку месенджерів
    return new_contact_def


def input_email():
    emails_list = []
    append_email = 'you@example.com'
    emails_list.append(input('\nВведіть основний E-Mail у вигляді you@example.com: '))
    print('Введіть додаткові E-Mail. Після того, як всі будуть записані - введіть пустий рядок: ')
    while append_email:
        append_email = input('e-mail: ')
        if not append_email == '':
            emails_list.append(append_email)
        else:
            print('Введення адреси електронної пошти завершено')
    return emails_list


def input_phone_num():
    phone_num_list = []
    append_phone = '+38067-777-88-99'
    print('\nВведіть телефонні номери у вигляді 777-88-99 по порядку. Після того, як всі будуть записані - '
          'введіть пустий рядок: ')
    while append_phone:
        append_phone = input('Телефонний номер: ')
        if not append_phone == '':
            phone_num_list.append(append_phone)
        else:
            print('Введення телефонних номерів завершено')
    return phone_num_list


def input_messenger(default_dict):
    print('\nМожна ввести аккаунти контакту для таких месенджерів:')
    for key in default_dict:
        print(key, ' ', sep='', end='')
    print('\nЯкщо дані акаунту відсутні - введіть Enter пустим рядком\n')
    for key in default_dict.copy():
        temp = input(f"- Введіть назву чи телефонний номер акаунта у {key}: ")
        if temp == '':
            default_dict.pop(key)
        else:
            default_dict[key] = temp
    print('Введення акаунтів для месенджерів закінчилось з таким їх переліком: ')
    print(default_dict.items())
    return default_dict


def print_list_of_contacts():
    len_list = []
    for i, attributes in enumerate(address_book_in_alphabet_order, 1):
        len_list.append(attributes[4])
    max_len = len(max(len_list, key=len))
    for i, attributes in enumerate(address_book_in_alphabet_order, 1):
        print(' ' * (3 - len(str(i))), i, ' | ', attributes[4], ' ' * (max_len - len(attributes[4])), ' | ', sep='')


def print_contact():
    check_listing = True
    while check_listing:
        check_listing = input("\n- Для виходу в основне меню натисніть Enter\n- Для перегляду повної інформації "
                              "по вибраному контакту, введіть його id (цифра, що вказана лівіше від ПІБ): ")
        if check_listing == '':
            break
        elif check_listing.isdigit():
            if 1 <= int(check_listing) <= max(address_book_list)[0]:
                print('\n№', check_listing, '|', address_book_list[int(check_listing) - 1][4], '|',
                      address_book_list[int(check_listing) - 1][5])
                print('_' * (8 + len(str(check_listing)) + len(str(address_book_list[int(check_listing) - 1][4])) +
                             len(str(address_book_list[int(check_listing) - 1][5]))))
                print('Список E-Mail:  ')
                for key in address_book_list[int(check_listing) - 1][6]:
                    print('                 |', key)
                print('Список телефонів:')
                for key in address_book_list[int(check_listing) - 1][7]:
                    print('                 |', key)
                print('Месенджери:')
                for key in address_book_list[int(check_listing) - 1][8].items():
                    print('                 |', key)

                check_listing = False
                tt = input('\nЩоб продовжити натисніть Enter:')
            else:
                print('____________________Ви ввели неіснуючий id. Спробуйте ще раз уважно виконати інструкції'
                      '____________________')
        else:
            print('____________________Ви ввели неіснуючий id. Спробуйте ще раз уважно виконати інструкції'
                  '____________________')


def change_contact(value):
    print('\n№', value, '|', address_book_list[int(value) - 1][4], '|')
    rb = input('- натисніть 1, якщо хочете переписати відомості про контакт повністю або\n'
               '- натисніть 2, якщо хочете змінити дані частково\n')

    if rb == '1':
        address_book_list[int(value) - 1] = create_contact()
    elif rb == '2':
        print('Якщо значення поля контакту необхідно залишити без змін - просто натискайте Enter без вводу даних.')

        temp_value = input(f"Змінити значення '{address_book_list[int(value) - 1][1]}' в полі /Прізвище/? Якщо так - "
                           f"введіть нове: ")
        if not temp_value == '':
            address_book_list[int(value) - 1][1] = temp_value
            address_book_list[int(value) - 1][4] = address_book_list[int(value) - 1][1] + ' ' \
                                                   + address_book_list[int(value) - 1][2] + ' ' \
                                                   + address_book_list[int(value) - 1][3]

        temp_value = input(f"Змінити значення '{address_book_list[int(value) - 1][2]}' в полі /Ім'я/? Якщо так - "
                           f"введіть нове: ")
        if not temp_value == '':
            address_book_list[int(value) - 1][2] = temp_value
            address_book_list[int(value) - 1][4] = address_book_list[int(value) - 1][1] + ' ' + \
                                                   address_book_list[int(value) - 1][2] + ' ' + \
                                                   address_book_list[int(value) - 1][3]

        if not address_book_list[int(value) - 1][3] == '':
            temp_value = input(f"Змінити значення '{address_book_list[int(value) - 1][3]}' в полі /по Батькові/? "
                               f"Якщо так - введіть нове: ")
            if not temp_value == '':
                address_book_list[int(value) - 1][3] = temp_value
                address_book_list[int(value) - 1][4] = address_book_list[int(value) - 1][1] + ' ' + \
                                                       address_book_list[int(value) - 1][2] + ' ' + \
                                                       address_book_list[int(value) - 1][3]

        temp_value = input(f"\nЗмінити значення '{address_book_list[int(value) - 1][5]}' в полі /Адреса/? "
                           f"Якщо так - введіть нове: ")
        if not temp_value == '':
            address_book_list[int(value) - 1][5] = temp_value

        print('\n')
        if not address_book_list[int(value) - 1][6][0] == '':
            for i in range(len(address_book_list[int(value) - 1][6].copy())):
                temp_value = input(f"Змінити значення '{address_book_list[int(value) - 1][6][i]}' в полі /E-Mails/? "
                                   f"Якщо так - введіть нове: ")
                if not temp_value == '':
                    address_book_list[int(value) - 1][6][i] = temp_value
        print('Якщо бажаєте, введіть додаткові E-Mail. Після того, як всі будуть записані - введіть пустий рядок: ')
        append_email = 'you@example.com'
        while append_email:
            append_email = input('e-mail: ')
            if not append_email == '':
                address_book_list[int(value) - 1][6].append(append_email)
            else:
                print('Введення додаткових адрес електронної пошти завершено\n')

        if not address_book_list[int(value) - 1][7][0] == '':
            for i in range(len(address_book_list[int(value) - 1][7].copy())):
                temp_value = input(f"Змінити значення '{address_book_list[int(value) - 1][7][i]}' "
                                   f"в полі /Телефонні номери/? Якщо так - введіть нове: ")
                if not temp_value == '':
                    address_book_list[int(value) - 1][7][i] = temp_value
        append_phone = '+38067-777-88-99'
        print('Якщо бажаєте, введіть додаткові телефонні номери. Після того, як всі будуть '
              'записані - введіть пустий рядок: ')
        while append_phone:
            append_phone = input('Телефонний номер: ')
            if not append_phone == '':
                address_book_list[int(value) - 1][7].append(append_phone)
            else:
                print('Введення додаткових телефонних номерів завершено\n')

        # if not address_book_list[int(value) - 1][8]['Viber'] == '':
        default_dict = {'Viber': '__', 'Messenger': '__', 'Telegram': '__'}
        for key in default_dict.copy():
            try:
                temp_value = input(f"Для месенджеру '{key}' зазначений аккаунт "
                                   f"'{address_book_list[int(value) - 1][8][key]}'. Введіть нове значення, або "
                                   f"скопіюйте попередне, \nа для видалення - натисніть Enter з пустим рядком:")
            except KeyError:
                temp_value = input(f"Для месенджеру '{key}' був відсуній аккаунт "
                                   f"'Введіть нове значення або залиште все, як є, \nнатиснув Enter з пустим рядком:")
            if temp_value == '':
                try:
                    address_book_list[int(value) - 1][8].pop(key)
                except KeyError:
                    pass
            else:
                address_book_list[int(value) - 1][8].update({key: temp_value})

    else:
        print('При необхідності ввести всього лише одну цифру "1" чи "2" у вас не вийшло це зробити правильно.\n'
              'Вам потрібен відпочинок!')

    address_book_in_alphabet_order.sort(key=lambda x: x[4])


def write_contacts_in_txt(address_book_for_txt):
    list_for_txt = []
    for i in range(len(address_book_for_txt)):
        for j in range(len(address_book_for_txt[i])):
            if type(address_book_for_txt[i][j]) == str:
                list_for_txt.append(address_book_for_txt[i][j])
            elif type(address_book_for_txt[i][j]) == int:
                list_for_txt.append(str(address_book_for_txt[i][j]))
            elif type(address_book_for_txt[i][j]) == list:
                list_for_txt.append('       '.join(address_book_for_txt[i][j]))
            elif type(address_book_for_txt[i][j]) == dict:
                temp = []
                for key in address_book_for_txt[i][j]:
                    temp.append(''.join(key + ':' + address_book_for_txt[i][j].get(key)))
                list_for_txt.append('       '.join(temp))
            else:
                print('Сталась невідома помилка з типом даних заповнення полів контакту адресної книги. \n'
                      'Зверніться до розробників.')
        list_for_txt.append('\n')

    string_for_write = '\n'.join(list_for_txt)

    file = open('address_book.txt', 'w')
    file.write(string_for_write)
    file.close()


def find_contact(string_to_find):
    print(f'Виконано пошук за запитом "{string_to_find}" серед даних контактів адресної книги')
    mark = False
    for i in range(len(address_book_in_alphabet_order)):
        temp_aggregator = []
        for j in range(len(address_book_in_alphabet_order[i])):
            if type(address_book_in_alphabet_order[i][j]) == str:
                temp_aggregator.append(address_book_in_alphabet_order[i][j])
            elif type(address_book_in_alphabet_order[i][j]) == list:
                temp_aggregator.extend(address_book_in_alphabet_order[i][j])
            elif type(address_book_in_alphabet_order[i][j]) == dict:
                temp_aggregator.extend(address_book_in_alphabet_order[i][j].values())
        if string_to_find in temp_aggregator:
            mark = True
            print("\nЗнайдено відповіність у контакті:", end='')
            print('\n№', address_book_list[i][0], '|', address_book_list[i][4], '|',
                  address_book_list[i][5])
            print('_' * (8 + len(str(address_book_in_alphabet_order[i][0])) + len(str(address_book_list[i][4])) +
                         len(str(address_book_list[i][5]))))
            print('Список E-Mail:  ')
            for key in address_book_list[i][6]:
                print('                 |', key)
            print('Список телефонів:')
            for key in address_book_list[i][7]:
                print('                 |', key)
            print('Месенджери:')
            for key in address_book_list[i][8].items():
                print('                 |', key)
    if not mark:
        print(f"\nЗбігів серед даних контактів абонентів адресної книги із пошуковим запитом '{string_to_find}' "
                  f"не знайдено..")
    ttt = input("Для продовження натисніть клавішу 'Enter'...")


# address_book_list = []
address_book_in_alphabet_order = []

try:
    with open('address_book_in_alphabet_order.pickle', 'rb') as f:
        address_book_list = pickle.load(f)
except FileNotFoundError:
    print("При спробі програми завантажити попередньо збережені на диску дані контактів адресної книги з файлу \n"
          "'address_book_in_alphabet_order.pickle' файл не було знайдено. Тому програма для коректного старту \n"
          "завантажить власні дефолтні дані, які потребуватимуть зміни або видалення користувачем. При першому \n"
          "збереженні введених даних відповідний файл з'явиться у папці, в якій запущений срипт. В подальшому \n"
          "стартові дані контактів, збережених при попередніх виконаннях програми, будуть завантажуватись при \n"
          "запуску програми вже з файлу 'address_book_in_alphabet_order.pickle'")

    address_book_list = [
        [1, 'Петренко', 'Олексій', 'Євгенович', 'Петренко' + ' ' + 'Олексій' + ' ' + 'Євгенович',
         'Адреса_1',
         ['E-Mail_1_1', 'E-Mail_2_1', 'E-Mail_3_1', 'E-Mail_4_1'],
         ['333-33-33', '333-33-44'],
         {'Viber': '333-33-33', 'Messenger': '333-33-44', 'Telegram': '@mavka-lisova'},
         ],
        [2, 'Семененко', 'Олександр', 'Полікарпович', 'Семененко' + ' ' + 'Олександр' + ' ' + 'Полікарпович',
         'Адреса_2',
         ['E-Mail_1_2', 'E-Mail_2_2', 'E-Mail_3_2', 'E-Mail_4_2'],
         ['444-44-44', '444-44-55'],
         {'Viber': '777-77-77', 'Messenger': '777-77-88', 'Telegram': '@student'},
         ],
        [3, 'Петренко-cfvcvxzx', 'Андрій', 'Семенович', 'Петренко-cfvcvxzx' + ' ' + 'Андрій' + ' ' + 'Семенович',
         'Адреса_3',
         ['E-Mail_1_3', 'E-Mail_2_3', 'E-Mail_3_3', 'E-Mail_4_3'],
         ['555-55-55', '555-55-66'],
         {'Viber': '888-88-88', 'Telegram': '@studentochka'},  # 'Messenger': '888-88-99',
         ],
    ]


address_book_in_alphabet_order = address_book_list
address_book_in_alphabet_order.sort(key=lambda x: x[4])

check_exit = True
while check_exit:
    radio_button = input("\nВиберіть подальший варіант дій:"
                         "\n                               - Створити новий контакт:____________ 1"
                         "\n                               - Вивести список контактів:__________ 2"
                         "\n                               - Змінити контакт:___________________ 3"
                         "\n                               - Видалити контакт:__________________ 4"
                         "\n                               - Записати список контактів на диск:_ 5"
                         "\n                               - Знайти контакт:____________________ 6"
                         "\n                               - Завершити роботу:__________________ 7"
                         "\n\nВведіть цифру для вашого варіанту дій: ")

    if radio_button == '1':
        print('\nВи вибрали пункт "Створити новий контакт"...')

        new_contact = create_contact()
        address_book_list.append(new_contact)

        address_book_in_alphabet_order = []  # Подвійне об'явлення списку виконане, щоб
        address_book_in_alphabet_order = address_book_list
        address_book_in_alphabet_order.sort(key=lambda x: x[4])

    elif radio_button == '2':
        print('\nВи вибрали пункт "Вивести список контактів"...\n')

        print_list_of_contacts()
        print_contact()

    elif radio_button == '3':
        print('\nВи вибрали пункт "Змінити контакт"...\n\nВиберіть номер контакту, який плануєте змінити:')
        print_list_of_contacts()

        change_contact(int(input('Введіть номер: ')))

    elif radio_button == '4':
        print('\nВи вибрали пункт "Видалити контакт"...\n\nВиберіть номер контакту, який плануєте видалити:')
        print_list_of_contacts()
        del_position = int(input('Введіть номер контакту для видалення: '))
        print(del_position, type(del_position))
        address_book_in_alphabet_order.pop(del_position - 1)

    elif radio_button == '5':
        print('\nВи вибрали пункт "Записати список контактів на диск"...\n')
        print(f"Всі дані контактів, актуальні на даний момент, збережені у файлі "
              f"'address_book_in_alphabet_order.pickle'\nА також список контактів виведений в текстовий файл"
              f" 'address_book.txt'.")

        with open('address_book_in_alphabet_order.pickle', 'wb') as f:
            pickle.dump(address_book_in_alphabet_order, f)
        write_contacts_in_txt(address_book_in_alphabet_order)

    elif radio_button == '6':
        print('\nВи вибрали пункт "Знайти контакт"...')
        find_contact(input("Введіть прізвище, або ім'я, або будь-який реквізит для пошуку: "))

    elif radio_button == '7':
        check_exit = False
        print("Робота програми завершується за вибором користувача.")
        r_button = True if input('Зберегти актуальну версію контактів адресної книги? (Y/y/Т/т): ').lower()[0] \
                            in ['y', 'т', 'д'] else False
        if r_button:
            with open('address_book_in_alphabet_order.pickle', 'wb') as f:
                pickle.dump(address_book_in_alphabet_order, f)
            write_contacts_in_txt(address_book_in_alphabet_order)
            print(f"Всі дані контактів, актуальні на даний момент, збережені у файлі "
                  f"'address_book_in_alphabet_order.pickle'\nА також список контактів виведений в текстовий файл "
                  f"'address_book.txt'. \nДо зустрічі.")
        else:
            print('======= За вибором користувача програма завершує роботу без збереження даних =======\nДо зустрічі.')

    else:
        print("Ви ввели неіснучий варіант вибору. Спробуйте ще раз.")
        t = input("Для цього натисніть клавішу 'Enter'...")

