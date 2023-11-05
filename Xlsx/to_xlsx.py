import os

import pandas as pd

from Python_Sql_Requests import get_all_products_for_xlsx


def create_xlsx_file():
    data = get_all_products_for_xlsx()
    data_frame = pd.DataFrame(data)
    data_frame.columns = ['Product_Name', 'Description', 'Price', 'Category_id', 'Category_name', 'Brand_id',
                          'Brand_name']
    writer = pd.ExcelWriter('./example.xlsx', engine='xlsxwriter')
    data_frame.to_excel(writer, 'Sheet1')
    writer._save()
    os.rename('./example.xlsx', './data.xlsx')


def delete_xlsx_file():
    xlsx_file_path = './data.xlsx'
    if os.path.exists(xlsx_file_path):
        os.remove(xlsx_file_path)
        return 'Файл удален успешно.'
    else:
        return 'Файл не существует, удаление невозможно.'


create_xlsx_file()