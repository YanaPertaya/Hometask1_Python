# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).



number = int(input('Введите четверть : '))
if number == 1:
    print('x>0 и до + бесконечности, у>0 b и до + бесконечности')
elif number ==2:
    print('x<0 и до - бесконечности, у>0 b и до + бесконечности')
elif number ==3:
    print('x<0 и до - бесконечности, у<0 b и до - бесконечности')
elif number ==4:
    print('x>0 и до + бесконечности, у<0 b и до - бесконечности')
else:
    print('Вы ввели не существующую четверть')

