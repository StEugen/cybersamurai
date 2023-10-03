import pandas as pd
import shutil

input_file = 'scudADwork.xlsx'
output_file = 'output.csv'

data = pd.read_excel(input_file)
data.to_csv(output_file, index=False, encoding='utf-8')

print(f'Conversion from {input_file} to {output_file} completed.')


input_file_path = 'output.csv'
output_file_path = 'utf8_encoded_file.csv'

with open(input_file_path, 'r', encoding='utf-8-sig') as input_file:
    content = input_file.read()

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(content)

print(f"The file {input_file_path} has been encoded with UTF-8 and saved as {output_file_path}.")
