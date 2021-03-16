from Gspread import Gspread
from nukisuto import Nukisuto
from iqoo import Iqoo
from pornhub import Pornhub
import schedule
import datetime
import time
import sys


def job():
    try:
        print('-------------スクレイピング開始--------------')
        print(datetime.datetime.now())
        print(datetime.datetime.now())
        nukisuto = Nukisuto('https://www.nukistream.com/')
        nukisuto_contents = nukisuto.get_contents()
        iqoo = Iqoo('https://iqoo.me/')
        iqoo_contents = iqoo.get_contents()
        pornhub = Pornhub('https://jp.pornhub.com/')
        pornhub_contents = pornhub.get_contents(
            min_good_count=200, min_good_rate=0.85)

        contents = nukisuto_contents+iqoo_contents+pornhub_contents

        # Googleプラットフォームで作成した秘密鍵が記載されたjsonのパス
        jsonf = 'av-sheet-5e65e23ebfc9.json'
        # スプレッドシートでコピーしたリンクのkey
        spread_sheet_key = '1UAKduCQdJp1GEQioTYEde_EPXDfL9DnhvSxvUCX6Ovs'

        gspread = Gspread(jsonf, spread_sheet_key)
        gspread.write(contents)
        print('-------------スクレイピング終了--------------')
    except Exception as e:
        print('-------------スクレイピング失敗--------------')
        import traceback
        traceback.print.exc()


# 毎日夜8時に実行する
schedule.every().day.at('20:00').do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
