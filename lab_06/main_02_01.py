"""Звягин Даниил ИУ7-13Б
Номер 2a - Удаление элемента из списка
с заданной позиции средствами языка python
"""

# Для заполнения списка
from random import randint

length = -1
while length < 1:
    length = int(input(
        "Введите желаюмую длину начального списка (int)\n> "
    ))
    if length < 1:
        print("Ошибка! Длина списска не может быть меньше 1")

arr = [0] * length
input_flag = input(
    "\nЗаполнить список случайными числами? [Y/n]\n> "
)


if input_flag in ['N', 'n']:
    input_flag = False
else:
    input_flag = True

if input_flag:
    for i in range(length):
        arr[i] = randint(-100, 100)
else:
    for i in range(length):
        arr[i] = int(input(
            f"Введите значение {i+1}-го элемента списка (int): "
        ))

out_flag = input(
    "\nВывести исходный список? [N/y]\n> "
)

if out_flag in ['N', 'n', '']:
    out_flag = False
else:
    out_flag = True

if out_flag:
    for i, el in enumerate(arr):
        print(f'{i+1:>4}-й элемент: {el:.7g}')

pos = -1

while pos < 0 or pos > length - 1:
    pos = int(input(
        "\nВведите, с какого места (не индекса) в списке нужно удалить элемент (int)\n> "
    ))
    pos -= 1
    if pos < 0:
        print("Ошибка! Позиция не может быть меньше единицы\n" +
              "(вообще может, но мы же не хотим удалять с конца)")
    elif pos > length - 1:
        print("Ошибка! Позиция за пределами списка!")

arr.pop(pos)

for i, el in enumerate(arr):
    print(f'{i+1:>4}-й элемент: {el:.7g}')