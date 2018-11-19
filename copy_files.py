""" Скрипт копирует файлы сопоставляя имя в источнике и
месте назначения и если имена папок совпадают, происходит
копирование папок со всеми файлами в этих папках, сохраняя структуру """

import os
import shutil
import re

src = r'E:\Лихасенко\Чертежи\# Новые'
dst = r'\\TERMINAL1\Public\Тех. Отдел\Конструкт. бюро\Разное\copy_test'

# Обходим файлы папки в источнике
for dir_src in os.listdir(src):
    try:
        name_src = ''
        # print('\t\tСписок файлов в src:', root, '\n', dirs, '\n', files, '\n')
        # print('\t\tСписок файлов в src:', dir_src, '\n')
        name_root = re.search('(([А-Я][А-Я])|(РЭО))-(Т8|Т10)', dir_src)
        if name_root:
            name_src = name_root.group(0)
            # print('\t\tПапка, которую копируем: ', name_src, '\n')

        # Обходим папки в месте назначения
        for dir, dirs_dst, files_dst in os.walk(dst):
            name_dst = ''
            # print('Список файлов в dst:', dir, '\n', dirs1, '\n', files1, '\n')
            name_dir = re.search('(([А-Я][А-Я])|(РЭО))-(Т8|Т10)$', dir)

            if name_dir:
                name_dst = name_dir.group(0)
                # print('\t\tПапка в которую копируем: ', res_name_dst, '\n')

                if name_src == name_dst:
                    # print('Совпадение!', dir_src, '=', dir)
                    path_dir_src = os.path.join(src, dir_src)
                    print('\n', dir_src)

                    for root, dirs, files in os.walk(path_dir_src):
                        dstpath = os.path.join(dir, dir_src)  # место назначения, куда копируем
                        # print(dstpath)

                        # Создаем папку в месте назначения, если не существует
                        if not os.path.exists(dstpath):
                            os.makedirs(dstpath)

                        for file in files:
                            srcfile = os.path.join(root, file)  # откуда копируем файл
                            # print("Откуда копируем: ", root, file)
                            dstfile = os.path.join(dstpath, file)  # куда копируем файл
                            # print("Куда копируем: ", dstpath, file, '\n')

                            # Если папка в месте назначения существует
                            if os.path.exists(dstpath):
                                # os.remove(dstfile)  # удаляем путь к файлу
                                shutil.copy(srcfile, dstfile)
                                print(file, ' - скопирован')

    except Exception as err:
        print('Ошибка!', '\n', err)




# for root, dirs, files in os.walk(src):
#         dstpath = os.path.join(dst, os.path.relpath(root, src))  # место назначения, куда копируем
#         if not os.path.exists(dstpath):
#             os.makedirs(dstpath)
#
#         for file in files:
#             srcfile = os.path.join(root, file)  # откуда копируем файл
#             print('\n', "Откуда копируем: ", srcfile)
#             dstfile = os.path.join(dstpath, file)  # куда копируем файл
#             print("Куда копируем: ", dstfile, '\n')
#
#             # Если папка в месте назначения существует
#             if os.path.exists(dstpath):
#                 # os.remove(dstfile)  # удаляем путь к файлу
#                 shutil.copy(srcfile, dstfile)


# Ловим ошибку из рекурсивного дерева копирования,
# чтобы можно было продолжить работу с другими файлами
# except(IOError, os.error) as why:
#     errors.append((srcfile, dstfile, str(why)))

# # Обрабатываем ошибку и отправляем лог в терминал
# except shutil.Error as err:
#     errors.extend(err.args[0])
#     print(err)
