# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет 

list = int(input('Введите число дня недели: '))
if list == 1 or list ==2 or list ==3 or list ==4 or list == 5:
    print('Не выходной')
elif list ==6 or list ==7:
    print('Выходной')
else:
    print('Вы ввели не корректное число')

