from django.shortcuts import render
import os
import openpyxl
import pprint
from django.http import HttpResponse

def index(request):

    # Excelのテンプレートファイルの読み込み
    wb = openpyxl.load_workbook('exceldownload/exceltemplates/sample.xlsx')

    # Excelに値設定（今回は固定値を設定（２行分）
    sheet = wb['Sheet1']

    # 1行目(NO,機器ID,機器名称,系統,設置場所,重要度,耐用年数)
    sheet['A4'].value = 1
    sheet['B4'].value = 'kiki001'
    sheet['C4'].value = '機器１'
    sheet['D4'].value = '冷却系統'
    sheet['E4'].value = '建屋１'
    sheet['F4'].value = 'A'
    sheet['G4'].value = 10

    # 2行目(NO,機器ID,機器名称,系統,設置場所,重要度,耐用年数)
    sheet['A5'].value = 2
    sheet['B5'].value = 'kiki002'
    sheet['C5'].value = '機器２'
    sheet['D5'].value = '電気系統'
    sheet['E5'].value = '建屋２'
    sheet['F5'].value = 'B'
    sheet['G5'].value = 20

    # Excelを返すためにcontent_typeに「application/vnd.ms-excel」をセットします。
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s' % 'report.xlsx'

    # データの書き込みを行なったExcelファイルを保存する
    wb.save(response)

    # 生成したHttpResponseをreturnする
    return response