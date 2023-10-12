import json
import os
from datetime import datetime

import openpyxl


def _get_file_name(path, ext):
    if (path is None) or (not os.path.exists(path)):
        path = './'
    file_name = f"{datetime.today().isoformat('-').replace(':', '-').split('.')[0]} .{ext}"

    res = os.path.join(path, file_name)
    return os.path.normpath(res)


def create_json(data, dest_path=None):
    file_name = _get_file_name(dest_path, 'json')

    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)


class _Excel:
    def __init__(self, file_name, data):
        self.file_name = file_name
        self.data = data
        self._book = openpyxl.Workbook()
        self._sheet = self._book.active

        self.words = list(self.data.keys())
        self.langs = list(self.data[self.words[0]].keys())

    def save_file(self):
        self._book.save(self.file_name)
        self._book.close()

    def create_demo(self):
        self._sheet['A1'].value = 10
        self._sheet['B1'].value = 11
        self._sheet['A2'].value = 20
        self._sheet['B2'].value = 21


def create_xlsx(data, dest_path=None):
    file_name = _get_file_name(dest_path, 'xlsx')

    table = _Excel(data=data, file_name=file_name)
    table.create_demo()
    table.save_file()

    print('ok')
