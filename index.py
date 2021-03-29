from gspreads.av_gspread import AV_Gspread
from themes.nukisuto import Nukisuto
from themes.iqoo import Iqoo
from themes.pornhub import Pornhub
from themes.javym import Javym
import schedule
import datetime
import time
import sys

nukisuto = Nukisuto('nukisuto')
contents = nukisuto.get_contents()
# javym = Javym('javym')
# contents = javym.get_contents()

print(contents)

sys.exit()


def job():
    try:
        print('-------------スクレイピング開始--------------')
        print(datetime.datetime.now())
        nukisuto = Nukisuto('nukisuto')
        iqoo = Iqoo('https://iqoo.me/')

        # 基盤クラスにget_write_contens()を作って、theme名を入れたら下のオブジェクト返してくれるメソッドを作れば良いかな。

        write_contents = [
            {
                'theme': nukisuto.theme,
                'contents': nukisuto.get_contents()
            },
            {
                'theme': iqoo.theme,
                'contents': iqoo.get_contents()
            }
        ]

        jsonf = 'av-sheet-5e65e23ebfc9.json'
        spread_sheet_key = '1UAKduCQdJp1GEQioTYEde_EPXDfL9DnhvSxvUCX6Ovs'
        for write_content in write_contents:
            gspread = AV_Gspread(jsonf, spread_sheet_key,
                                 write_content['theme'])
            gspread.write(write_content['contents'])
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
