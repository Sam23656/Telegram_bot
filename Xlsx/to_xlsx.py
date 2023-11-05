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


def convert_xlsx_file_to_df():
    xlsx_file_path = './data.xlsx'
    data_frame = pd.read_excel(xlsx_file_path)
    return data_frame


def get_columns_and_rows(data_frame):
    result = []
    for index, row in data_frame.iterrows():
        product_name = row['Product_Name']
        description = row['Description']
        price = row['Price']
        category_id = row['Category_id']
        brand_id = row['Brand_id']
        result.append([product_name, description, category_id, brand_id, price])

    return result