print("Завдання №2.3\nПрограма обчислення і друку на екрані заданої кількості чисел із ряду Фібоначі")
print("_" * 78, "\nЦя програма продовжує на задане користувачем число n ряд чисел Фібоначі {Fn} = 1, 1, 2, 3, 5, 8, "
                "13, 21, 34, 55, 89, ...\n\nДавайте розпочнемо - початок ряду: \n{Fn} = 1, 1, ...")

n_1 = 1
n_2 = 1
n_3 = 2
while True:
    n = input("\nВкажіть, на скільки символів n програма повинна продовжити ряд Фібоначчі: ")

    if not n.isdigit() or n == '0':
        print("Необхідно ввести ціле число більше 0. Програма завершає роботу, до зустрічі.")
        exit(21)
    n_max = int(n)
    print('... ', end='')
    for i in range(n_max):
        print(n_3, ', ', sep='', end='')
        n_1 = n_2
        n_2 =n_3
        n_3 = n_1 + n_2
    print('...')
