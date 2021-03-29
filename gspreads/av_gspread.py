import datetime
from Gspread import Gspread
import sys


class AV_Gspread(Gspread):
    def __init__(self,  jsonf, SPREADSHEET_KEY, theme):
        super(AV_Gspread, self).__init__(jsonf, SPREADSHEET_KEY)
        self.theme = theme

    def get_header_range(self, header_len):
        alfas = []
        for i in range(65, 65+header_len):
            alfas.append(chr(i))

        format_range = alfas[0]+'1:'+alfas[-1]+'1'

        return format_range

    def get_header_items(self):
        header_items = []
        try:
            items = self.theme['items']
            for items_name in items:
                for item_name in items[items_name]:
                    if (items[items_name][item_name]['required'] == True):
                        header_items.append(
                            items[items_name][item_name]['name'])
        except Exception as e:
            print('ヘッダー項目の取得失敗')
            print(str(e))

        return header_items

    def get_title(self):
        return self.theme['theme_name'] + \
            datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")

    def write(self, contents):
        if not contents:
            print('コンテンツがありません。')
            return

        # # シートを新規作成
        title = self.get_title()
        self.add_sheet(title)

        # ヘッダー項目を取得
        header_items = self.get_header_items()
        # ヘッダーが入るセルの場所を取得
        header_range = self.get_header_range(len(header_items))

        # シートに新しいデータを書き込む
        ws = self.get_worksheet(title)
        ws.format(header_range, {'textFormat': {'bold': True}})
        ws.update(header_range, [header_items])
        super().write(ws, contents)
