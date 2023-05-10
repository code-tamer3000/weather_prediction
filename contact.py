import os
import pandas as pd

def merge_excel_files(dir_path):
    excel_files = [f for f in os.listdir(dir_path) if f.endswith('.xlsx')] # получите список файлов в директории, оканчивающихся на .xlsx

    dfs = []
    for file in excel_files:
        file_path = os.path.join(dir_path, file) # получите полный путь к файлу
        df = pd.read_excel(file_path) # прочитайте таблицу из файла
        dfs.append(df) # добавьте таблицу в список dfs

    merged_df = pd.concat(dfs, ignore_index=True) # объедините все таблицы в одну и сбросьте индексы
    merged_df.to_excel(os.path.join(dir_path, 'database.xlsx'), index=False) # сохраните объединенную таблицу в ту же директорию, с именем файла database.xlsx
