# https://pythonworld.ru/moduli/modul-os.html
# https://pythonworld.ru/moduli/modul-os-path.html
import os
DIRECTORY = 'C:/Users/mimiron/Downloads/photo' # где находятся файлы

for i, f in enumerate(os.listdir(DIRECTORY)):
    new_filename = 'picture_' + str(i) + '.jpeg' # названия, разумеется, должны быть разными
    print(f'Файл {f} переименован в {new_filename}')
    os.rename(
      DIRECTORY + '/' + f, # не забываем указывать директорию, где нужно изменить файл
      DIRECTORY + '/' + new_filename
    )
