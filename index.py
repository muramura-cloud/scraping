from Gspread import Gspread
from nukisuto import Nukisuto
from iqoo import Iqoo
from pornhub import Pornhub
import schedule
import datetime
import time
import sys

# nukisuto = Nukisuto('nukisuto')
# contents = nukisuto.get_contents()
pornhub = Pornhub('pornhub')
contents = pornhub.get_contents()
print(contents)


sys.exit()


def job():
    try:
        print('-------------スクレイピング開始--------------')
        print(datetime.datetime.now())
        nukisuto = Nukisuto('https://www.nukistream.com/')
        nukisuto_contents = nukisuto.get_contents()
        iqoo = Iqoo('https://iqoo.me/')
        iqoo_contents = iqoo.get_contents()

        contents = nukisuto_contents+iqoo_contents

        jsonf = 'av-sheet-5e65e23ebfc9.json'
        spread_sheet_key = '1UAKduCQdJp1GEQioTYEde_EPXDfL9DnhvSxvUCX6Ovs'
        gspread = Gspread(jsonf, spread_sheet_key)
        gspread.write(contents)
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
