import json
import os
from datetime import datetime
from itertools import product

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

    def _gen_words_keys(self):
        if len(self.words) <= 25:
            tmp = [chr(ltr) for ltr in range(66, (66 + len(self.words)))]
            return tmp[:len(self.words)]

        tmp = [chr(ltr) for ltr in range(66, 91)]
        letters = [chr(ltr) for ltr in range(65, 91)]
        factor = 1
        while True:
            if len(tmp) >= len(self.words):
                return tmp[:len(self.words)]
            factor += 1
            tmp += [''.join(tuples) for tuples in product(letters, repeat=factor)]

    def create_titles(self):
        cols_keys = self._gen_words_keys()

        for i in range(0, len(self.words)):
            self._sheet[f'{cols_keys[i]}1'].value = self.words[i]

        for j in range(0, len(self.langs)):
            self._sheet[f'A{j + 2}'].value = self.langs[j]

    def add_data(self):
        # колонки с нуля, строки с единицы
        col_index = 0
        cols_keys = self._gen_words_keys()
        print(cols_keys)

        for i in self.data.values():
            row_index = 1

            for j in i.values():
                row_index += 1
                print(j, row_index)
                self._sheet[f'{cols_keys[col_index]}{row_index}'].value = j

            col_index += 1

    def save_file(self):
        self._book.save(self.file_name)
        self._book.close()


def create_xlsx(data, dest_path=None):
    file_name = _get_file_name(dest_path, 'xlsx')

    table = _Excel(data=data, file_name=file_name)
    table.create_titles()
    table.add_data()
    table.save_file()
