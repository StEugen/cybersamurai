import pandas as pd
import shutil
import os

def convert_excel_to_csv(input_file):
    try:
        output_file = 'output.csv'

        data = pd.read_excel(input_file)
        data.to_csv(output_file, index=False, encoding='utf-8')

        input_file_path = 'output.csv'
        output_file_path = 'scudADwork.csv'

        with open(input_file_path, 'r', encoding='utf-8-sig') as input_file:
            content = input_file.read()

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(content)

        os.remove("./output.csv")


    except Exception as e:
        raise e

