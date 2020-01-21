print("Завдання №2.2\nПрограма обчислення суми натуральних чисел")
print("_" * 52)


def sum_of_natural_numbers(val_1, val_2):
    if val_1 == val_2 and val_1 >= 1:
        if int(val_1)/val_2 == 1.0:
            c = int(val_1)
        else:
            print("Ви вказали два однакових дійсних нецілих числа. В заданому інтервалі немає жодного "
                  "натурального числа!")
            c = 0

    elif val_1 < 1 and val_2 < 1:
        print("Обидва вказаних числа менше 1. Отже, в заданому інтервалі немає жодного "
              "натурального числа")
        c = 0

    elif (0 < (val_2 - val_1) < 1 or 0 < (val_1 - val_2) < 1) and int(val_1)/int(val_2) == 1.0 and \
            int(val_1)/val_1 != 1.0 and int(val_2)/val_2 != 1.0:
        print("В інтервалі між двома заданими числами немає жодного натурального числа")
        c = 0

    elif val_1 < 1 <= val_2:
        x = int(val_2)
        c = 0
        for i in range(1, x+1):
            c = i + c

    elif val_2 < 1 <= val_1:
        x = int(val_1)
        c = 0
        for i in range(1, x+1):
            c = i + c

    elif val_1 >= 1 and val_2 >= 1:
        x_min = val_1 if val_1 < val_2 else val_2
        x_max = val_2 if val_1 < val_2 else val_1
                                                        # print("x_min після визначення мін", x_min)
                                                        # print("x_max після визначення мін", x_max)
        x_min = int(x_min) if int(x_min)/x_min == 1.0 else (int(x_min) + 1)
        x_max = int(x_max)
                                                        # print("x_min після відкидання дробової частини", x_min)
                                                        # print("x_max після відкидання дробової частини", x_max)
        c = 0
        for i in range(x_min, x_max+1):
            c = i + c

    else:
        print("Сталася непередбачувана помилка. Самсінгонврон. Зверніться до розробника :)")
        exit(33)

    return c


check_exit = True
while check_exit:
                    # a = float(input('\nВведіть перше число: '))
                    # b = float(input('Введіть друге число: '))

 # ____________________________Введення з перевіркою другого числа____________________________
    radio_button_is_val_digit = False
    s = ''
    while not radio_button_is_val_digit:
        s = input('Введіть перше число: ')
        point = 0
        if not s.isdigit():
            if s == 'exit':
                exit(21)
            elif s[0] == '-':
                s2 = list(s)
                del s2[0]
                s_temp = ''.join(s2)
                if s_temp.isdigit():
                    radio_button_is_val_digit = True
                else:
                    point = 0
                    s_temp_2 = list(s_temp)
                    for i in range(len(s_temp)):
                        if s_temp[i] == '.':
                            point += 1
                            if point == 1:
                                del s_temp_2[i]
                    s4 = ''.join(s_temp_2)
                    if point == 1 and s4.isdigit():
                        radio_button_is_val_digit = True
                    elif point > 1:
                        print("\t\tЧисло не може мати більше однієї розділюючої коми. Для продовження програми вам "
                              "необхідно ввести число правильно.\n\t\tЯкщо ви хочете завершити програму - введіть "
                              "'exit'.")
                    else:
                        print(
                            "\t\tВведене значення має бути числом. Для продовження програми вам необхідно ввести число."
                            "\n\t\tЯкщо ви хочете завершити програму - введіть 'exit'.")
            else:
                point = 0
                s_temp_1 = list(s)
                for i in range(len(s)):
                    if s[i] == '.':
                        point += 1
                        if point == 1:
                            del s_temp_1[i]
                s3 = ''.join(s_temp_1)
                if point == 1 and s3.isdigit():
                    radio_button_is_val_digit = True
                elif point > 1:
                    print(
                        "\t\tЧисло не може мати більше однієї розділюючої коми. Для продовження програми вам необхідно "
                        "ввести число правильно.\n\t\tЯкщо ви хочете завершити програму - введіть 'exit'.")
                else:
                    print(
                        "\t\tВведене значення має бути числом. Для продовження програми вам необхідно ввести число.\n"
                        "\t\tЯкщо ви хочете завершити програму - введіть 'exit'.")
        else:
            radio_button_is_val_digit = True
    if point == 1:
        a = float(s)
    else:
        a = int(s)

# ____________________________Введення з перевіркою другого числа____________________________
    radio_button_is_val_digit = False
    s = ''
    while not radio_button_is_val_digit:
        s = input('Введіть друге число: ')
        point = 0
        if not s.isdigit():
            if s == 'exit':
                exit(21)
            elif s[0] == '-':
                s2 = list(s)
                del s2[0]
                s_temp = ''.join(s2)
                if s_temp.isdigit():
                    radio_button_is_val_digit = True
                else:
                    point = 0
                    s_temp_2 = list(s_temp)
                    for i in range(len(s_temp)):
                        if s_temp[i] == '.':
                            point += 1
                            if point == 1:
                                del s_temp_2[i]
                    s4 = ''.join(s_temp_2)
                    if point == 1 and s4.isdigit():
                        radio_button_is_val_digit = True
                    elif point > 1:
                        print("\t\tЧисло не може мати більше однієї розділюючої коми. Для продовження програми вам "
                              "необхідно ввести число правильно.\n\t\tЯкщо ви хочете завершити програму - введіть 'exit'.")
                    else:
                        print(
                            "\t\tВведене значення має бути числом. Для продовження програми вам необхідно ввести число."
                            "\n\t\tЯкщо ви хочете завершити програму - введіть 'exit'.")
            else:
                point = 0
                s_temp_1 = list(s)
                for i in range(len(s)):
                    if s[i] == '.':
                        point += 1
                        if point == 1:
                            del s_temp_1[i]
                s3 = ''.join(s_temp_1)
                if point == 1 and s3.isdigit():
                    radio_button_is_val_digit = True
                elif point > 1:
                    print(
                        "\t\tЧисло не може мати більше однієї розділюючої коми. Для продовження програми вам необхідно "
                        "ввести число правильно.\n\t\tЯкщо ви хочете завершити програму - введіть 'exit'.")
                else:
                    print(
                        "\t\tВведене значення має бути числом. Для продовження програми вам необхідно ввести число.\n"
                        "\t\tЯкщо ви хочете завершити програму - введіть 'exit'.")
        else:
            radio_button_is_val_digit = True
    if point == 1:
        b = float(s)
    else:
        b = int(s)

    f = sum_of_natural_numbers(a, b)
    print("Сума натуральних чисел, що знаходяться в діапазоні від", a, "до", b, "включно становить", f)
    ch = input('\nПовторити розрахунок для іншої пари чисел? (y/n):')
    if ch == 'y' or ch == 'Y' or ch == 'д' or ch == 'Д' or ch == 'т' or ch == 'Т':
        check_exit = True
    elif ch == 'n' or ch == 'N' or ch == 'н' or ch == 'Н':
        check_exit = False
    else:
        print("У вас не вийшло вибрати правильний варіант продовжити/закінчити, тому давайте зробимо це ще раз :)")
