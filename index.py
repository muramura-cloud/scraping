from gspreads.av_gspread import AV_Gspread
import importlib
import schedule
import datetime
import time
import sys


# 抽出したいテーマの名前(av_config)を指定する
themes = ['nukisuto', 'pornhub', 'iqoo']
jsonf = 'av-sheet-5e65e23ebfc9.json'
spread_sheet_key = '1UAKduCQdJp1GEQioTYEde_EPXDfL9DnhvSxvUCX6Ovs'


def job():
    write_contents = []

    try:
        print('-------------スクレイピング開始--------------')
        print(datetime.datetime.now())
        for theme in themes:
            module = importlib.import_module('themes.'+theme)
            theme_class = eval('module.'+theme.capitalize())(theme)

            content = {
                'theme': theme_class.theme,
                'contents': theme_class.get_contents()
            }

            write_contents.append(content)

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
