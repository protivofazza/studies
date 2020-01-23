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

