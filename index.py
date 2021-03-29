from gspreads.av_gspread import AV_Gspread
from themes.nukisuto import Nukisuto
from themes.iqoo import Iqoo
from themes.pornhub import Pornhub
import schedule
import datetime
import time
import sys


def job():
    try:
        print('-------------スクレイピング開始--------------')
        print(datetime.datetime.now())
        nukisuto = Nukisuto('nukisuto')
        nukisuto_contents = nukisuto.get_contents()
        iqoo = Iqoo('https://iqoo.me/')
        iqoo_contents = iqoo.get_contents()

        jsonf = 'av-sheet-5e65e23ebfc9.json'
        spread_sheet_key = '1UAKduCQdJp1GEQioTYEde_EPXDfL9DnhvSxvUCX6Ovs'
        # コンテンツはまとめて一括で記入できると良いね。テーマが多くなったときに備えて、
        n_gspread = AV_Gspread(jsonf, spread_sheet_key, nukisuto.theme)
        n_gspread.write(contents)
        i_gspread = AV_Gspread(jsonf, spread_sheet_key, iqoo.theme)
        i_gspread.write(contents)
        print('-------------スクレイピング終了--------------')
        print(datetime.datetime.now())
    except Exception as e:
        print('-------------スクレイピング失敗--------------')
        print(datetime.datetime.now())
        print(str(e))


# 毎日夜8時に実行する
schedule.every().day.at('20:00').do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
