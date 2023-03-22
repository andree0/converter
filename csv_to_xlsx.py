import csv
import os
from xlsxwriter.workbook import Workbook


delimiter = input("Podaj znak podziału: ")
ending_files = {".csv", ".CSV", ".txt", ".TXT"}

files = [file for file in os.listdir("files_to_convert")]
for file in files:
    with open(f"files_to_convert/{file}", mode="r", encoding="utf-8") as csv_file:
        # zły znak podziału powoduje tylko zmianę rozszerzenia na .xlsx
        # do napisania funkcja wykrywająca znak podziału
        read_file = csv.reader(csv_file, delimiter=delimiter)
        if (ending := file[-4:]) in ending_files:
            new_file_name = file.replace(ending, ".xlsx")
            workbook = Workbook(f"converted_files/{new_file_name}")
            worksheet = workbook.add_worksheet("dane")
            row = 0
            for line in read_file:
                col = 0
                for cell in line:
                    worksheet.write_string(row, col, cell)
                    col += 1
                row += 1
            workbook.close()
            print(f"Przekonwertowano plik: {file} na {new_file_name}")
        else:
            print(f"Błędne rozszerzenie pliku: {file}")
