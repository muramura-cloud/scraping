from av import Av
from Gspread import Gspread
import json
import schedule
import datetime
import time
import sys


def job():
    print('job実行')

# schedule.every(1).minutes.do(job)

nukisuto = Av('https://www.nukistream.com/')
nukisuto_contents = nukisuto.get_contents()

iqoo = Av('https://iqoo.me/')
iqoo_contents = iqoo.get_contents()


contents = nukisuto_contents+iqoo_contents

# Googleプラットフォームで作成した秘密鍵が記載されたjsonのパス
jsonf = 'av-sheet-5e65e23ebfc9.json'
# スプレッドシートでコピーしたリンクのkey
spread_sheet_key = '1UAKduCQdJp1GEQioTYEde_EPXDfL9DnhvSxvUCX6Ovs'

gspread = Gspread(jsonf, spread_sheet_key)
gspread.write(contents)
