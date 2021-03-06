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


a = is_digit_pro('Введіть квадратичний коефіцієнт (a): ')
b = is_digit_pro('Введіть лінійний коефіцієнт (b): ')
c = is_digit_pro('Введіть вільну сталу коефіцієнт (c): ')


b_indicate = ' -' if b < 0 else ' +'
b_mod = b*-1 if b < 0 else b
c_indicate = ' -' if c < 0 else ' +'
c_mod = b*-1 if c < 0 else c

print("\nВи ввели рівняння вигляду ", a, 'x2', b_indicate, ' ', b_mod, 'x', c_indicate, ' ', c_mod, ' = 0', sep='')

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
