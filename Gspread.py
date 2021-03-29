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

    # 二次元配列を受け取ってデータをスプレッドシートに書き込む[{'a':'aa'},{'b':'bb'}]
    def write(self, ws, contents):
        try:
            for i, content in enumerate(contents):
                for j, key in enumerate(content):
                    ws.update_cell(i+2, j+1, content[key])
        except Exception as e:
            print('シートの書き込みに失敗しました。')
            print(str(e))
