# エクセルのworkbookオブジェクトを取得(既存のエクセルファイル)
# book = openpyxl.load_workbook('AV.xlsx')
# エクセルのworkbookオブジェクトを取得(新規ファイル)
# book = openpyxl.Workbook()
# シートを取得
# sheet = book['Sheet']

# sheet['A1'] = 'タイトル'
# sheet['B1'] = 'リンク'
# sheet['C1'] = '高評価'
# sheet['D1'] = '高評価率'

# for i, content in enumerate(contents):
#     print(str(i + 1) + '行目')
#     for j, val in enumerate(content):
#         print(str(j + 1) + '個目')
#         sheet.cell(row=i + 2, column=j + 1).value = val

# book.save('AV.xlsx')

# book.close()
