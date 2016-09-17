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

    # search all pages of drugs starting with that letter
    current_row_number = 3;
    for target_id in target_ids:

        print(target_id)

        # navigate to search page
        search_url = 'https://www.vectorbase.org/search/site/' + \
            target_id
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'lxml')

        # navigate to gene page
        gene_link = '/Gene/Summary/'
        pea_soup = soup.findAll('a', href=re.compile(gene_link))
        pea_soup_string = str(pea_soup.pop())
        link_ending = re.search('a href="(.*?)"', pea_soup_string)
        search_url = 'https://www.vectorbase.org' + link_ending.group(1)
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'lxml')

        pea_soup = soup.findAll('a', {"title":"GO: Cellular component"})

        if current_row_number == 13:
            code.interact(local=locals())

        # iterate to next row number
        current_row_number += 2

# help text and launch of vectorbaser
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('AUTO_VECTORBASE -- Written by Nathan Spencer 2016')
        print('Usage: python auto_vectorbase.py "path/to/excel/file.xlsx"')
    else:
        vectorbaser(sys.argv[1])
