from bs4 import BeautifulSoup
from openpyxl import load_workbook
import code
import requests
import re
import sys
from selenium import webdriver
import time

# vectorbaser
def vectorbaser(file_path):

    driver = webdriver.Firefox()

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
    wb.save(file_path);

    for target_id in target_ids:

        print(target_id)
        wb = load_workbook(filename=file_path, use_iterators=False)
        ws = wb.worksheets[0]

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

        # navigate to cellular component, grab info if it exists
        pea_soup = soup.findAll('a', {"title":"GO: Cellular component"})
        if len(pea_soup) > 0:
            pea_soup_string = str(pea_soup.pop())
            link_ending = re.search('href="(.*?)"', pea_soup_string)
            search_url = 'https://www.vectorbase.org' + link_ending.group(1)
            driver.get(search_url)
            time.sleep(3)
            source = driver.page_source
            cell_comp = re.search('<td style="width:25%;text-align:left">([a-z ]+)</td>', source)
            if not cell_comp is None:
                cell_comp = cell_comp.group(1)
                ws.cell(row=current_row_number, column=3).value = cell_comp

        # navigate to biological process, grab info if it exists
        pea_soup = soup.findAll('a', {"title":"GO: Biological process"})
        if len(pea_soup) > 0:
            pea_soup_string = str(pea_soup.pop())
            link_ending = re.search('href="(.*?)"', pea_soup_string)
            search_url = 'https://www.vectorbase.org' + link_ending.group(1)
            driver.get(search_url)
            time.sleep(3)
            source = driver.page_source
            bio_proc = re.search('<td style="width:25%;text-align:left">([a-z ]+)</td>', source)
            if not bio_proc is None:
                bio_proc = bio_proc.group(1)
                ws.cell(row=current_row_number, column=4).value = bio_proc

        # navigate to molecular function, grab info if it exists
        pea_soup = soup.findAll('a', {"title":"GO: Molecular function"})
        if len(pea_soup) > 0:
            pea_soup_string = str(pea_soup.pop())
            link_ending = re.search('href="(.*?)"', pea_soup_string)
            search_url = 'https://www.vectorbase.org' + link_ending.group(1)
            driver.get(search_url)
            time.sleep(3)
            source = driver.page_source
            mol_func = re.search('<td style="width:25%;text-align:left">([a-z -]+)</td>', source)
            if not mol_func is None:
                if(current_row_number == 7):
                    code.interact(local=locals())
                mol_func = mol_func.group(1)
                ws.cell(row=current_row_number, column=5).value = mol_func

        # navigate to orthologues, grab info if it exists
        pea_soup = soup.findAll('a', {"title":"GO: Molecular function"});

        # save, iterate to next row number
        wb.save(file_path)
        current_row_number += 2

    driver.Quit()


# help text and launch of vectorbaser
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('AUTO_VECTORBASE -- Written by Nathan Spencer 2016')
        print('Usage: python auto_vectorbase.py "path/to/excel/file.xlsx"')
    else:
        vectorbaser(sys.argv[1])
