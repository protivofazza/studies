print("Завдання №2.1\nПрограма для обчислення коренів квадратного рівняння")
print("_" * 52)
print("Ця програма знаходить корені рівняння типу ax2 + bx + c = 0\n\nДавайте зазначимо коефіцієнти рівняння:")

radio_button_is_val_digit = False
s = ''
while not radio_button_is_val_digit:
    s = input('Введіть лінійний коефіцієнт (a): ')
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
                        "\t\tЗначення коефіцієнту має бути числом. Для продовження програми вам необхідно ввести число."
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
                print("\t\tЧисло не може мати більше однієї розділюючої коми. Для продовження програми вам необхідно "
                      "ввести число правильно.\n\t\tЯкщо ви хочете завершити програму - введіть 'exit'.")
            else:
                print("\t\tЗначення коефіцієнту має бути числом. Для продовження програми вам необхідно ввести число.\n"
                      "\t\tЯкщо ви хочете завершити програму - введіть 'exit'.")
    else:
        radio_button_is_val_digit = True
if point == 1:
    a = float(s)
else:
    a = int(s)

radio_button_is_val_digit = False
s = ''
while not radio_button_is_val_digit:
    s = input('Введіть лінійний коефіцієнт (b): ')
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
                        "\t\tЗначення коефіцієнту має бути числом. Для продовження програми вам необхідно ввести число."
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
                print("\t\tЧисло не може мати більше однієї розділюючої коми. Для продовження програми вам необхідно "
                      "ввести число правильно.\n\t\tЯкщо ви хочете завершити програму - введіть 'exit'.")
            else:
                print("\t\tЗначення коефіцієнту має бути числом. Для продовження програми вам необхідно ввести число.\n"
                      "\t\tЯкщо ви хочете завершити програму - введіть 'exit'.")
    else:
        radio_button_is_val_digit = True
if point == 1:
    b = float(s)
else:
    b = int(s)

radio_button_is_val_digit = False
s = ''
while not radio_button_is_val_digit:
    s = input('Введіть лінійний коефіцієнт (c): ')
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
                        "\t\tЗначення коефіцієнту має бути числом. Для продовження програми вам необхідно ввести число."
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
                print("\t\tЧисло не може мати більше однієї розділюючої коми. Для продовження програми вам необхідно "
                      "ввести число правильно.\n\t\tЯкщо ви хочете завершити програму - введіть 'exit'.")
            else:
                print("\t\tЗначення коефіцієнту має бути числом. Для продовження програми вам необхідно ввести число.\n"
                      "\t\tЯкщо ви хочете завершити програму - введіть 'exit'.")
    else:
        radio_button_is_val_digit = True
if point == 1:
    c = float(s)
else:
    c = int(s)


D = b ** 2 - 4 * a * c
x1 = (-b + D ** 0.5) / (2 * a)
x2 = (-b - D ** 0.5) / (2 * a)


if D < 0:
    print("\nРівняння не має дійсних коренів. Розв'язком рівняння є два комплексні корені:\nX1 =", x1, "\nX2 =", x2)
elif D == 0:
    round(x1, 4)
    print("\nРівняння має один корінь:\nX =", x1)
else:
    round(x1, 4)
    round(x2, 4)
    print("\nРівняння має два дійсні корені:\nX1 =", x1, "\nX2 =", x2)
