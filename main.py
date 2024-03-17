# https://pythonworld.ru/moduli/modul-os.html
# https://pythonworld.ru/moduli/modul-os-path.html

#Импорт рабочих библиотек
import os
from tkinter import *

#Импорт функций из файла
from function import *

root = Tk()

#Цвет заднего окна
root['bg'] = '#fafafa'
#Наименование программы
root.title('Renaming Photo')
#Размер окна
root.geometry('500x450')
#Фиксация размера окна
root.resizable(width=False, height=False)

# Рамка, содержащая визуальные компоненты
frame = Frame(root, bg='white')
frame.place(relwidth=1, relheight=5)

title = Label(frame, text='Текст подсказка', bg='gray', font=40)
title.pack()
btn = Button(frame, text='Отправить', bg='gray', command=button_click)
btn.pack()

pathInput = Entry(frame, bg='gray',)
pathInput.pack()

formatInput = Entry(frame, bg='gray')
formatInput.pack()

root.mainloop()


DIRECTORY = 'C:/Users/mimiron/Downloads/photo_test' # где находятся файлы

for i, f in enumerate(os.listdir(DIRECTORY)):
    new_filename = 'Picture_' + str(i) + '.jpg' # названия, разумеется, должны быть разными
    print(f'Файл {f} переименован в {new_filename}')
    os.rename(
      DIRECTORY + '/' + f, # не забываем указывать директорию, где нужно изменить файл
      DIRECTORY + '/' + new_filename
    )
