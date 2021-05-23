import pandas as pd
from tkinter.filedialog import askopenfilename, askdirectory
from xlsxwriter.workbook import Workbook
import glob
import os
import csv


def results():

    def get_folder_location():
        selected_location = ""
        try:
            filename = askdirectory()
            selected_location = filename
            print("File Selected as " + selected_location)
        except Exception as Error:
            print(Error)
        return selected_location

    file_location = get_folder_location()

    def get_all_files(file_location):
        try:
            print("files gathered from " + file_location)
            all_files = glob.glob(os.path.join(file_location, "*.csv"))
            all_df = []
            for f in all_files:
                df = pd.read_csv(f, sep=',', error_bad_lines=False, delimiter=None, header=1, lineterminator='\n' )
                df["file"] = f.split(',')[-1]
                all_df.append(df)
            merged_df = pd.concat(all_df, ignore_index=True, sort=True)
            print(merged_df)
            merged_df.to_csv("merged.csv")
            print("MERGED CSV FILE CREATED")
        except Exception as Error:
            print("Merge CSV Error: ")
            print(Error)



    get_all_files(file_location)

    # filename_excel = get_folder_location().replace(".csv", ".xlsx")

    # def cvs_to_excel(filename_excel):
    #     try:
    #         for csvfile in glob.glob(os.path.join('.', '*.csv')):
    #             workbook = Workbook(filename_excel)
    #             worksheet = workbook.add_worksheet()
    #             with open(csvfile, 'rt', encoding='utf16') as f:
    #                 reader = csv.reader(f)
    #                 for r, row in enumerate(reader):
    #                     for c, col in enumerate(row):
    #                         worksheet.write(r, c, col)
    #             workbook.close()
    #             print("CSV to Excel Conversion is complete")
    #     except Exception as Error:
    #         print("CSV to EXCEL error: ")
    #         print(Error)

    # def pre_results(filename_excel):
    #     cvs_to_excel(filename_excel)

    # pre_results(filename_excel)


results()