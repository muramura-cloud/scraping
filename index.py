from Gspread import Gspread
from nukisuto import Nukisuto
from iqoo import Iqoo
from avgle import Avgle
import schedule
import time
import sys


def job():
    nukisuto = Nukisuto('https://www.nukistream.com/')
    nukisuto_contents = nukisuto.get_contents()
    iqoo = Iqoo('https://iqoo.me/')
    iqoo_contents = iqoo.get_contents()

    contents = nukisuto_contents+iqoo_contents

    # Googleプラットフォームで作成した秘密鍵が記載されたjsonのパス
    jsonf = 'av-sheet-5e65e23ebfc9.json'
    # スプレッドシートでコピーしたリンクのkey
    spread_sheet_key = '1UAKduCQdJp1GEQioTYEde_EPXDfL9DnhvSxvUCX6Ovs'

    gspread = Gspread(jsonf, spread_sheet_key)
    gspread.write(contents)
    print('-------------スクレイピング終了--------------')


# 毎日夜8時に実行する
schedule.every().day.at('20:00').do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
