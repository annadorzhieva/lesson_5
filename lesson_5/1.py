'''1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

text = input('Введите данные: \n')
file = open('text.txt', 'w')
while True:
    q = input()
    if q == '':
        print('Ввод данных закончен')
        break
    file.write(q+ '\n')
file.close()