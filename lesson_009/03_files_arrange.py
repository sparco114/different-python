# -*- coding: utf-8 -*-

import os, time, shutil
from zipfile import ZipFile


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class SortFilesByDate:

    def __init__(self, dir_path, sorted_dir_path):
        self.dir_path = os.path.normpath(dir_path)
        self.sorted_dir_path = sorted_dir_path

    def sort_from_dir(self):
        for dirpath, dirnames, filenames in os.walk(self.dir_path):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                time_file_sec = os.path.getmtime(full_file_path)  # берет время изменения файла m-modified
                time_file = time.gmtime(time_file_sec)
                full_sorted_dir_path = os.path.join(self.sorted_dir_path, str(time_file[0]), str(time_file[1]))
                if os.path.isdir(full_sorted_dir_path):
                    shutil.copy2(full_file_path, full_sorted_dir_path)
                else:
                    os.makedirs(full_sorted_dir_path)
                    shutil.copy2(full_file_path, full_sorted_dir_path)

    '''
    пока не смог настроить, чтоб при разархивировании сохранялась старая дата изменения файла. 
    Сейчас она устанавливается текущей
    
    А так же не смог сделать, чтоб файлый складывались прямо в папку, а не добавлялся путь, по которому 
    они лежат в архиве
    '''

    # def sort_from_zip(self):
    #     for dirpath, dirnames, filenames in os.walk(self.dir_path):
    #         print('зашел в папку')
    #         for file in filenames:
    #             print('начал перебирать файлы, взял один')
    #             with ZipFile(file, mode='r') as zfile:
    #                 print('открыл файл ZIP')
    #                 for inf in zfile.infolist():
    #                     print("взял инфо по файлу из архива")
    #                     if not inf.is_dir():
    #                         # print('JNLTKMYJ BVX:         ', os.path.basename(inf.filename))
    #                         print(inf.date_time)
    #                         full_sorted_dir_path = os.path.join(self.sorted_dir_path, str(inf.date_time[0]),
    #                                                             str(inf.date_time[1]))
    #                         if os.path.isdir(full_sorted_dir_path):
    #                             print(f"директория есть, добавил туда файл {os.path.basename(inf.filename)}")
    #                             zfile.extract(inf.filename, path=full_sorted_dir_path)
    #                         else:
    #                             print(f"директории нет, создал ее и добавил туда файл {os.path.basename(inf.filename)}")
    #                             os.makedirs(full_sorted_dir_path)
    #                             zfile.extract(inf.filename, path=full_sorted_dir_path)


path = './files/'
path_out = './sorted_files/'

ico = SortFilesByDate(path, path_out)
# ico.sort_from_dir()
ico.sort_from_zip()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
