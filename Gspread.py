import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Gspread:
    def __init__(self, jsonf, SPREADSHEET_KEY):
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            jsonf, scope)
        gc = gspread.authorize(credentials)

        self.worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

    # 二次元配列を受け取ってデータをスプレッドシートに書き込む
    def write(self, contents):
        if not contents:
            return 

        for i, content in enumerate(contents):
            for j, val in enumerate(content):
                self.worksheet.update_cell(i+2, j+1, val)
