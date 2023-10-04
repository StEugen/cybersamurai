import pandas as pd
import shutil
import os


def convert_excel_to_csv(input_file):
    try:
        #input_file = input('Please provide filename: ')
        output_file = 'output.csv'

        data = pd.read_excel(input_file)
        data.to_csv(output_file, index=False, encoding='utf-8')

        #print(f'Conversion from {input_file} to {output_file} completed.')

        input_file_path = 'output.csv'
        output_file_path = 'scudADwork.csv'

        with open(input_file_path, 'r', encoding='utf-8-sig') as input_file:
            content = input_file.read()

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(content)

        os.remove("./output.csv")
        #print(f"The file {input_file_path} has been encoded with UTF-8 and saved as {output_file_path}.")

    except Exception as e:
        raise e
        #print(f"An error occurred: {str(e)}")
        #input()
