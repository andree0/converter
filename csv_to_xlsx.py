import csv
import os
from xlsxwriter.workbook import Workbook

delimiter = input("Podaj znak podziału: ")

files = [file for file in os.listdir('files_to_convert') if file.endswith(
    '.csv')]
for file in files:
    with open(f'files_to_convert/{file}') as csv_file:
        read_file = csv.reader(csv_file, delimiter=delimiter)
        workbook = Workbook(f"converted_files/{file.replace('.csv', '.xlsx')}")
        worksheet = workbook.add_worksheet('dane')

        row = 0
        for line in read_file:
            col = 0
            for cell in line:
                worksheet.write_string(row, col, cell)
                col += 1

            row += 1
        workbook.close()
