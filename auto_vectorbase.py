from bs4 import BeautifulSoup
import code
import requests
import re
import sys

# vectorbaser
def vectorbaser(file_path):
    print('no content')


# help text and launch of vectorbaser
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('AUTO_VECTORBASE -- Written by Nathan Spencer 2016')
        print('Usage: python auto_vectorbase.py "path/to/excel/file.xlsx"')
    else:
        vectorbaser(sys.argv[1])
