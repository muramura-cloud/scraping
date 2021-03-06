from av import Av
from Gspread import Gspread
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
import sys

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

