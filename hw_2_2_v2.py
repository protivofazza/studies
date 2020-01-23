print("Завдання №2.2\nПрограма обчислення суми натуральних чисел")
print("_" * 52)


def is_digit_pro(string):
    numbers_needed = None
    while numbers_needed is None:
        n = input(string)
        if not n.isdigit():
            if n == 'exit':
                print("Програма припиняє роботу за інструкцією користувача. До зустрічі.")
                exit(21)
            elif n[0] == '-':
                n2 = n[1:]
                if n2.isdigit():
                    numbers_needed = int(n)
                else:
                    point = 0
                    for i in range(len(n2)):
                        if n2[i] == '.':
                            point = 1
                            n2 = n2[:i] + n2[i + 1:]
                            break
                    if point == 1 and n2.isdigit():
                        numbers_needed = float(n)
                    else:
                        print(
                            "\t\tВведене значення має бути числом. Для продовження програми вам необхідно ввести число."
                            "\n\t\tЯкщо ви хочете завершити програму - введіть 'exit'.")
            else:
                point = 0
                n2 = n
                for i in range(len(n2)):
                    if n2[i] == '.':
                        point = 1
                        n2 = n2[:i] + n2[i + 1:]
                        break
                if point == 1 and n2.isdigit():
                    numbers_needed = float(n)
                else:
                    print(
                        "\t\tВведене значення має бути числом. Для продовження програми вам необхідно ввести число."
                        "\n\t\tЯкщо ви хочете завершити програму - введіть 'exit'.")
        else:
            numbers_needed = int(n)
    return numbers_needed


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
    a = is_digit_pro('Введіть перше число: ')
    b = is_digit_pro('Введіть друге число: ')

    f = sum_of_natural_numbers(a, b)
    print("Сума натуральних чисел, що знаходяться в діапазоні від", a, "до", b, "включно становить", f)
    ch = input('\nПовторити розрахунок для іншої пари чисел? (y/n):')
    if ch == 'y' or ch == 'Y' or ch == 'д' or ch == 'Д' or ch == 'т' or ch == 'Т':
        check_exit = True
    elif ch == 'n' or ch == 'N' or ch == 'н' or ch == 'Н':
        check_exit = False
    else:
        print("У вас не вийшло вибрати правильний варіант продовжити/закінчити, тому давайте зробимо це ще раз :)")