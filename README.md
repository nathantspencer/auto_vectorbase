# auto_vectorbase
### What is auto_vectorbase?
`auto_vectorbase.py` is a web scraping Python script written for a very specific use case at West Virginia University. It can, however, be adapted for similar applications. The script grabs information about molecular function, biological process, cellular component, and other notes and appends them to a provided Excel spreadsheet. It is specific to the genus _Glossina_.
### How can I use it?
Running `auto_vectorbase.py` is simple. Simply place your Excel document in the `/auto_vectorbase` directory and run the following command from a terminal in that directory:

`$ python auto_vectorbase.py name_of_excel_file.xlsx`

The process may take some time, but the spreadsheet is saved every time a row of information is scraped, so don't worry if the script is interrupted. That being said, there is currently no way to pick up where you left off, so the script will begin from the start of your spreadsheet if you rerun it. If you are feeling adventurous, lines 23 and lines 27 can be adjusted to alter the range of rows that the script will fill.

### How should my Excel file be set up?
Your Excel file should be set up with the target ID (e.g. GPAI034476) of the gene in the first column. The second column is unused and can be blank or can contain values. The third column will be populated with cellular components, the fourth with biological process, the fifth with molecular function, and the sixth with additional notes. Your Excel file is assumed to have a header row, so processing will begin at row 2.

### What dependencies do I need to install?
Along with Python 3.x, the following python modules are required:
- [requests](http://docs.python-requests.org/en/master/)
- [bs4](https://www.crummy.com/software/BeautifulSoup/)
- [openpyxl](https://openpyxl.readthedocs.io/en/default/)
- [selenium](http://selenium-python.readthedocs.io/)

### Can I get help adapting this script to fit my needs?
Yes! Do not hesistate to contact me at nathantspencer@gmail.com with any questions or concerns.

_This software is not produced by or associated with vectorbase.org. It is provided here free for personal, commercial, and academic use._
