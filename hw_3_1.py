from string import whitespace, punctuation

print("Завдання №3.1.\nПрограма підрахунку слів у тексті")
print("_" * 33, "\nЦя програма приймає введені користувачем тексти, які складються зі слів,\nформує словник із "
                "статистикою введених слів і виводить цей словник на екран\nу вигляді форматованої таблиці."
                "\n\nПам'ятайте, що для припинення роботи програми необхідно ввести пустий рядок.\n"
                "Давайте розпочнемо...")

# Пам'ятайте, що для припинення роботи програми необхідно ввести пустий рядок - пустий рядок - будь-що
# print('whitespace = {}'.format(repr(whitespace)))
# print('punctuation = {}'.format(repr(punctuation)))
# print('\n', punctuation)


def text_input(string):    # Ф-ія видаляє знаки пунктуації із введеного тексту (крім дефісу всередині слів та апострофу)
    table = []             # і повертає список, складений із слів введеного тексту, який був отриманий в форматі str
    words = ['']           # При цьому слова, введені за кожної нової ітерації вводу, додаються до введених раніше
    while words:
        tran_table = str.maketrans("""!"#$%&()*+,./:;<=>?@[\\]^_`{|}~""", '                              ')
        words = input(string).replace(" - ", ' ').translate(tran_table).lower().split()
        table.extend(words)
    return table


def check_exit():
    if input('Закінчити роботу програми? (Y/y/Т/т): ').lower()[0] in ['y', 'т', 'д']:
        return False
    else:
        return True

    # for word in words:
    #     if punctuation in word:
    #         word_1 = word[-1:]
    #     word_1 = word.lower()
    #     print(word_1, type(word_1))


radio_button = True
while radio_button:
    aw_list = text_input('Введіть текст: ')  # Створює список на основі тексту, отриманого від ф-ії text_input()
    aw_set = set(aw_list)
    aw_list_short = list(aw_set)
    aw_dict = {}
    for i in range(len(aw_list_short)):
        aw_dict[aw_list_short[i]] = aw_list.count(aw_list_short[i])

    max_len = len(max(aw_list_short, key=len))
    print("\nНа основі всіх введених слів програма згенерувала таблицю слів введеного тексту, та кількості їх "
          "згадувань.\nСтатистика слів: ")
    for i in range(len(aw_dict)):
        print('|', aw_list_short[i], ' '*(max_len-len(aw_list_short[i])), '|', aw_dict.get(aw_list_short[i]), '|', sep='')
    radio_button = check_exit()
