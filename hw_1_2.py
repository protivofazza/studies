print("Завдання №1.2\nПрограма для виводу результатів різних операцій над двома числами")
print("_" * 65)

value_1 = int(input('Введіть перше число: '))
value_2 = int(input('Введіть друге число: '))


print("\nРезультати арифметичних операцій над двома числами", value_1, "та", value_2)
print("-"*57)
result = value_1 + value_2
print("- Результат додавання:\t\t\t\t\t", value_1, "+", value_2, "=", result)
result = value_1 - value_2
print("- Результат віднімання:\t\t\t\t\t", value_1, "-", value_2, "=", result)
result = value_1 * value_2
print("- Результат множення:\t\t\t\t\t", value_1, "*", value_2, "=", result)
result = value_1 / value_2
print("- Результат ділення:\t\t\t\t\t", value_1, "/", value_2, "=", result)
result = value_1 // value_2
print("- Результат цілочисленного ділення:\t\t", value_1, "//", value_2, "=", result)
result = value_1 ** value_2
print("- Результат зведення в степінь:\t\t\t", value_1, "**", value_2, "=", result)
result = value_1 % value_2
print("- Результат залишку від ділення:\t\t", value_1, "%", value_2, "=", result)

print("\nРезультати операцій порівняння двох чисел", value_1, "та", value_2)
print("-"*57)
result = value_1 > value_2
print("- Результат порівняння:\t\t\t\t\t", value_1, ">", value_2, " ---", result)
result = value_1 < value_2
print("- Результат порівняння:\t\t\t\t\t", value_1, "<", value_2, " ---", result)
result = value_1 == value_2
print("- Результат порівняння:\t\t\t\t\t", value_1, "==", value_2, "---", result)
result = value_1 != value_2
print("- Результат порівняння:\t\t\t\t\t", value_1, "!=", value_2, "---", result)
result = value_1 >= value_2
print("- Результат порівняння:\t\t\t\t\t", value_1, ">=", value_2, "---", result)
result = value_1 <= value_2
print("- Результат порівняння:\t\t\t\t\t", value_1, "<=", value_2, "---", result)

print("\nРезультати логічних операцій для звичайних чисел майже не мають сенсу, проте вони можливі.\nДля чисел",
      value_1, "та", value_2, "вони видаватимуть такі результати:")
print("-"*57)
result = value_1 and value_2
print("- Результат логічного 'І':\t\t\t\t", value_1, "and", value_2, "---", result)
result = value_1 or value_2
print("- Результат логічного 'АБО':\t\t\t", value_1, "or", value_2, " ---", result)
print("- Логічний 'НІ' працює з одним числом")