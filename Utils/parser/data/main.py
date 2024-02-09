import json
from xlwt import Workbook
import xlwt
import os
import asyncio
from my_functions import *


def collect_chat_information(channel_type, channel_title, members, admins, users):
    # Заменяем запрещенные символы в названии канала
    for x in ['\\', '|', '"', '/', ':', '?', '*', '<', '>']:
        channel_title = channel_title.replace(x, ' ')

    # Проверяем и создаем необходимые директории
    if os.path.exists(f'../Чаты') is False:
        os.mkdir(f'../Чаты')
    if os.path.exists(f'../Каналы') is False:
        os.mkdir(f'../Каналы')
    if os.path.exists(f'../{channel_type}/{channel_title}') is False:
        os.mkdir(f'../{channel_type}/{channel_title}')

    # Проверяем статус чата и записываем информацию в файлы
    if channel_type == 'ok':
        with open(f'../{channel_type}/{channel_title}/Участники {channel_title}.json', 'w', encoding='utf8') as f:
            with open(f'../{channel_type}/{channel_title}/Участники {channel_title}.txt', 'w', encoding='utf8') as file:
                all_users = {
                    'admins': admins,
                    'users.txt': members
                }
                f.write(json.dumps(all_users, indent=4, ensure_ascii=False,))
                if admins is not None:
                    file.write('Администраторы:\n')
                    for x in admins:
                        file.write(f'{str(admins[x])}\n')
                if len(members) > 0:
                    file.write('Пользователи:\n')
                    for x in members:
                        file.write(f'{str(members[x])}\n')

        # Создаем Excel-файл с информацией о пользователях
        wb = Workbook()
        style = xlwt.easyxf('pattern: pattern solid, fore_colour light_blue;'
                            'font: colour white, bold True;')
        n_list = 1
        sheet1 = wb.add_sheet(f'Users_{n_list}')
        sheet1.write(0, 0, 'Администраторы', style)
        sheet1.write(0, 1, 'ID', style)
        sheet1.write(0, 2, 'First Name', style)
        sheet1.write(0, 3, 'Last Name', style)
        sheet1.write(0, 4, 'Username', style)
        sheet1.write(0, 5, 'Телефон', style)
        sheet1.write(0, 6, 'Бот', style)
        sheet1.write(0, 7, 'Удалён', style)
        sheet1.write(0, 8, 'Скам', style)
        n = 1
        q = 1
        for x in users:
            sheet1.col(0).width = 256 * 17
            sheet1.col(1).width = 256 * 17
            sheet1.col(2).width = 256 * 25
            sheet1.col(3).width = 256 * 25
            sheet1.col(4).width = 256 * 25
            sheet1.col(5).width = 256 * 17
            sheet1.col(6).width = 256 * 7
            sheet1.col(7).width = 256 * 7
            sheet1.col(8).width = 256 * 7
            sheet1.write(n, 0, x['admin'])
            sheet1.write(n, 1, x['id'])
            sheet1.write(n, 2, x['first_name'])
            sheet1.write(n, 3, x['last_name'])
            sheet1.write(n, 4, x['username'])
            sheet1.write(n, 5, x['phone'])
            sheet1.write(n, 6, x['bot'])
            sheet1.write(n, 7, x['deleted'])
            sheet1.write(n, 8, x['scam'])
            n += 1
            q += 1
            if n == 30000:
                n_list += 1
                sheet1 = wb.add_sheet(f'Users_{n_list}"')
                n = 1
        wb.save(f'../{channel_type}/{channel_title}/Участники {channel_title}.xls')


