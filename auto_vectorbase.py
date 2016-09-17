from bs4 import BeautifulSoup
from openpyxl import load_workbook
import code
import requests
import re
import sys

# vectorbaser
def vectorbaser(file_path):

    # load up the worksheet, get the number of rows
    wb = load_workbook(filename=file_path, use_iterators=False)
    ws = wb.worksheets[0]
    num_rows = ws.get_highest_row()

    # iterate through target_ids, grab them
    target_ids = []
    for row in range(3, num_rows, 2):
        target_ids.append(ws.cell(row=row, column=1).value)

    code.interact(local=locals())

# help text and launch of vectorbaser
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('AUTO_VECTORBASE -- Written by Nathan Spencer 2016')
        print('Usage: python auto_vectorbase.py "path/to/excel/file.xlsx"')
    else:
        vectorbaser(sys.argv[1])
t
