import xlsxwriter
from save_on_excel_line import save_line


def save_on_excel_file(filename_excel):

    with open(filename_excel, 'a', encoding="utf-8") as ef:
        ef.workbook = xlsxwriter.Workbook(filename_excel)
        worksheet = ef.workbook.add_worksheet()

        # Add an Excel formats.

        bold_format = ef.workbook.add_format({'bold': True})

        worksheet.write('A1', 'Data Collection Time', bold_format)
        worksheet.write('B1', 'Tweet Time', bold_format)
        worksheet.write('C1', 'Tweet User Name', bold_format)
        worksheet.write('D1', 'Tweet Location', bold_format)
        worksheet.write('E1', 'Tweet Text', bold_format)
        worksheet.write('F1', 'Tweet Full Text', bold_format)
        worksheet.write('G1', 'URL', bold_format)

        ef.workbook.close()

    return True
