import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Gspread:
    def __init__(self, jsonf, SPREADSHEET_KEY):
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            jsonf, scope)
        gc = gspread.authorize(credentials)

        self.worksheet = gc.open_by_key(SPREADSHEET_KEY)

    def add_sheet(self, title):
        self.worksheet.add_worksheet(title=title, rows=100, cols=20)

    def delete_sheet(self, ws):
        self.worksheet.del_worksheet(ws)

    def get_worksheet(self, sheet_name):
        return self.worksheet.worksheet(sheet_name)

    # 二次元配列を受け取ってデータをスプレッドシートに書き込む
    def write(self, contents):
        if not contents:
            return

        # シートがある程度増えてきたらそれを削除する
        # self.delete_sheet(self.get_worksheet('high_quality_av'))

        # シートを新規作成
        now = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
        self.add_sheet(now)

        # シートに新しいデータを書き込む
        ws = self.get_worksheet(now)
        ws.format('A1:E1', {'textFormat': {'bold': True}})
        ws.update('A1:F1', [['サムネ', 'タイトル', 'リンク', '高評価', '高評価率', 'タグ']])
        for i, content in enumerate(contents):
            for j, val in enumerate(content):
                ws.update_cell(i+2, j+1, val)
