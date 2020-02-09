from string import whitespace, punctuation

print("Завдання №3.4.\nПрограма зі створення словника перекладів")
print("_" * 41, "\nЦя програма приймає запропоновані користувачем тексти, які складються зі слів,\nформує словник із "
                "них, записує переклад для кожного слова у словник і виводить цей словник на екран\nу вигляді "
                "форматованої таблиці."
                "\n"
                "Давайте розпочнемо...\n")


def get_vocabluary(text):
    result = {}
    table = []
    words = ['']
    tran_table_1 = str.maketrans("""!"#$%&()*+,./:;<=>?@[\\]^_`{|}~""", '                              ')
    words = text.replace(" - ", ' ').translate(tran_table_1).split()

    for i in range(len(words)):
        if words[i].capitalize() not in result.keys():
            result[words[i].capitalize()] = word_translating(words[i])
    return result


def word_translating(word_str):
    # global trans_word
    print('Необхідно внести в словник переклад слова "', word_str.capitalize(), '"', end='')

    check_enter = True
    while check_enter:
        word = list(input(': '))
        del_list = list(punctuation)
        del_list.extend(list(whitespace))
        count = 0
        for i in range(len(word)):
            if word[i] in del_list:
                count += 1
        if count == len(word) or ''.join(word) == '':
            check_enter = True
            print("Введене значення перекладу не може складатися з одних лише знаків пунктуаціїї і не може бути "
                  "пустим рядком.\nСпробуйте ввести переклад ще раз", end='')
        else:
            check_enter = False
            trans_word = ''.join(word)

    return trans_word


if __name__ == "__main__":
    TEXT = """Я працюю{{ важко /./,, )))**)  працюю\t
    
    \t \n
    
    \nпрацюю"""
    # TEXT = """З краю в край через увесь простір неба висіявся зорями Чумацький Шлях. Так назвали
    # колись вигин галактики. Магістральний канал проходить на південь якраз по цій зоряній трасі, по якій у сиву
    # давнину з усієї України їхали тисячі чумацьких мажар, щоб завантажитися сіллю на кримських соляних озерах.
    #
    #        """

    print("Запропонований текст виглядає наступним чином:\n", repr(TEXT), "\n\nДавайте заповнимо поля таблиці:")

    vocabulary = get_vocabluary(TEXT)
    voc_list_1 = list(vocabulary.keys())
    voc_list_2 = list(vocabulary.values())

    max_len_1 = len(max(voc_list_1, key=len))
    max_len_2 = len(max(voc_list_2, key=len))
    print("\nНа основі всіх введених слів програма згенерувала таблицю у форматі слово-переклад: ")
    for i in range(len(vocabulary)):
        print('|', ' ' * (max_len_1 - len(voc_list_1[i])), voc_list_1[i], '|', ' ' * (max_len_2 - len(voc_list_2[i])), voc_list_2[i], '|')

