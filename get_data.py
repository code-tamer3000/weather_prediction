import requests
import os
import pandas as pd
def get_data(dir_path) :
    i = 1933
    os.mkdir('datatables')
    while (i < 2023) :
        url = 'http://pogoda-service.ru/archive_gsod_res.php?country=RS&station=287220&datepicker_beg=06.01.' + str(i) + '&datepicker_end=23.12.2022&bsubmit=Посмотреть'
        response = requests.get(url)
        tables = pd.read_html(response.content)
        df = tables[0]  # замените 0 на индекс нужной таблицы, если на странице несколько таблиц
        df.to_excel(dir_path + r'\datatables\table' + str(i) + '.xlsx',index=False)  # замените table.xlsx на имя файла, куда нужно сохранить таблицу
        i += 4



