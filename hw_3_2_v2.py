print("Завдання №3.2.v2\nПрограма виведення слів із введеного тексту на екран")
print("_" * 52, "\nЦя програма приймає введені користувачем тексти, які складються зі слів,\nформує словник із "
                "статистикою введених слів і виводить цей словник на екран\nу вигляді форматованої таблиці зі словами "
                "в алфавітному порядку."
                "\n\nПам'ятайте, що для припинення введення тексту необхідно ввести пустий рядок.\n"
                "Давайте розпочнемо...")


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


radio_button = True
while radio_button:
    aw_list = text_input('Введіть текст: ')  # Створює список на основі тексту, отриманого від ф-ії text_input()
    aw_list.sort()
    aw_dict = {}
    for i in range(len(aw_list)):
        aw_dict[aw_list[i]] = aw_list.count(aw_list[i])

    print("\nНа основі всіх введених слів програма згенерувала таблицю зі слів введеного тексту, та кількості їх "
          "згадувань, розмістивши слова в алфавітному порядку.\nСтатистика слів: ")
    max_len = len(max(aw_list, key=len))

    for i in range(len(aw_list)):
        print('|', aw_list[i], ' '*(max_len-len(aw_list[i])), '|', aw_dict.get(aw_list[i]), '|')
    radio_button = check_exit()
