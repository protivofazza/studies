print("Завдання №1.3\nПрограма для огляду типів представлення чисел та деяких арифметичних оперцій над ними")
print("_" * 85)

value_1 = input('\nВведіть ціле число: ')

print("\nВідображення в форматі цілого числа (int)\t\t\t", int(value_1))
print("Відображення в форматі дійсного числа (float)\t\t", float(value_1))
print("Відображення в форматі логічного числа (bool)\t\t", bool(value_1))
print("Відображення в форматі комплексного числа (complex)\t", complex(value_1))
print("Відображення в строковому форматі (str)\t\t\t\t", value_1)

value_2 = input('\nВведіть ще одне ціле число: ')

result = int(value_1) + int(value_2)
print("\n- Результат   'int'\t", value_1, "+   'int'\t", value_2, "=", result, "з типом  ", type(result))
result = float(value_1) + float(value_2)
print("- Результат 'float'\t", value_1, "+ 'float'\t", value_2, "=", result, "з типом", type(result))

result = int(value_1) * int(value_2)
print("- Результат   'int'\t", value_1, "*   'int'\t", value_2, "=", result, "з типом  ", type(result))
result = float(value_1) * float(value_2)
print("- Результат 'float'\t", value_1, "* 'float'\t", value_2, "=", result, "з типом", type(result))

result = int(value_1) + float(value_2)
print("\n- Результат 'int'", value_1, "+ 'float'", value_2, "=", result, "з типом", type(result))
result = float(value_1) + int(value_2)
print("- Результат 'float'", value_1, "+ 'int'", value_2, "=", result, "з типом", type(result))

result = int(value_1) * float(value_2)
print("\n- Результат 'int'", value_1, "* 'float'", value_2, "=", result, "з типом", type(result))
result = float(value_1) * int(value_2)
print("- Результат 'float'", value_1, "* 'int'", value_2, "=", result, "з типом", type(result))

result = int(value_1) + complex(value_2)
print("\n- Результат   'int'", value_1, "+ 'complex'", value_2, "=", result, "з типом", type(result))
result = float(value_1) + complex(value_2)
print("- Результат 'float'", value_1, "+ 'complex'", value_2, "=", result, "з типом", type(result))

result = int(value_1) * complex(value_2)
print("\n- Результат   'int'", value_1, "* 'complex'", value_2, "=", result, "з типом", type(result))
result = float(value_1) * complex(value_2)
print("- Результат 'float'", value_1, "* 'complex'", value_2, "=", result, "з типом", type(result))

print("\n\n\nАрифметичні операції із булевими типами також можливі. ")  # Але для чого?
print("Також треба врахувати, що якщо передавати строкові дані в оператор bool, \nто булеве значення завжди буде "
      "дорівнювати 1")
print("_"*72)

result = bool(int(value_1)) + bool(int(value_2))
print("| - Результат  'bool'", value_1, "+ 'bool'", value_2, "=", result, "з типом", type(result))
result = bool(int(value_1)) * bool(int(value_2))
print("| - Результат  'bool'", value_1, "* 'bool'", value_2, "=", result, "з типом", type(result))

result = int(value_1) + bool(int(value_2))
print("|\n| - Результат   'int'", value_1, "+ 'bool'", value_2, "=", result, "з типом", type(result))
result = float(value_1) + bool(int(value_2))
print("| - Результат 'float'", value_1, "+ 'bool'", value_2, "=", result, "з типом", type(result))

result = int(value_1) * bool(int(value_2))
print("|\n| - Результат   'int'", value_1, "* 'bool'", value_2, "=", result, "з типом", type(result))
result = float(value_1) * bool(int(value_2))
print("| - Результат 'float'", value_1, "* 'bool'", value_2, "=", result, "з типом", type(result))
print("_"*72)

print("\n\n\nВаріанти взаємодії строкових типів даних між собою (str) та з іншими типами даних (bool, int, float "
      "complex)")
print("_"*135)

result = value_1 + value_2
print("| - Результат  'str'", value_1, "+ 'str'", value_2, "=", result, "з типом", type(result), "")
print("| - Додовання строкового типу даних (str) і будь-якого іншого типу даних (bool, int, float complex) неможливе")

result = value_1 * int(value_2)
print("|\n| - Результат  'str'", value_1, "* 'int'", value_2, "=", result, "з типом", type(result))
result = value_1 * bool(int(value_2))
print("| - Результат  'str'", value_1, "* 'bool'", value_2, "=", result, "з типом", type(result))

print("| - Множення між собою строкових типів даних (str*str) неможливе")
print("| - Множення між собою строкових типів даних та дійсних чисел (str*float) неможливе")
print("| - Множення між собою строкових типів даних та комплексних чисел (str*complex) неможливе")

result = value_1 * int(value_2) * bool(int(value_2))
print("|\n| - Результат  'str'", value_1, "* 'int'", value_2, "* 'bool'", value_2, "=", result, "з типом", type(result))

print("| - Якщо виконати множення строкового типу даних str на int чи bool з нульовим значенням, то результатом буде "
      "пуста строка з типом str")
print("_"*135)


print("\n\n\nВ змаганнях 'кожен сам за себе' премагає комплексне представлення даних (complex), друге місце у дійсного "
      "представлення даних (float)")
print("_"*135)

result = int(value_1) + float(value_2) + bool(int(value_2))
print("|\n|- Результат 'int'", value_1, "+ 'float'", value_2, "+ 'bool'", value_2, "=", result, "з типом", type(result))
result = int(value_1) + float(value_2) + bool(int(value_2)) + complex(value_1)
print("|- Результат 'int'", value_1, "+ 'float'", value_2, "+ 'bool'", value_2, "+ 'complex'", value_1, "=", result,
      "з типом", type(result))

result = int(value_1) * float(value_2) * bool(int(value_2))
print("|\n|- Результат 'int'", value_1, "* 'float'", value_2, "* 'bool'", value_2, "=", result, "з типом", type(result))
result = int(value_1) + float(value_2) * bool(int(value_2)) * complex(value_1)
print("|- Результат 'int'", value_1, "* 'float'", value_2, "* 'bool'", value_2, "* 'complex'", value_1, "=", result,
      "з типом", type(result))
print("_"*135)