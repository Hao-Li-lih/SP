import requests
from bs4 import BeautifulSoup
import pandas as pd

tables = []

confs = [
    [
        'https://ec.europa.eu/clima/ets/nap.do?languageCode=fr&nap.registryCodeArray=AT&nap.registryCodeArray=BE&nap.registryCodeArray=BG&nap.registryCodeArray=HR&nap.registryCodeArray=CY&nap.registryCodeArray=CZ&nap.registryCodeArray=DK&nap.registryCodeArray=EE&nap.registryCodeArray=EU&nap.registryCodeArray=FI&nap.registryCodeArray=FR&nap.registryCodeArray=DE&nap.registryCodeArray=GR&nap.registryCodeArray=HU&nap.registryCodeArray=IS&nap.registryCodeArray=IE&nap.registryCodeArray=IT&nap.registryCodeArray=LV&nap.registryCodeArray=LI&nap.registryCodeArray=LT&nap.registryCodeArray=LU&nap.registryCodeArray=MT&nap.registryCodeArray=NL&nap.registryCodeArray=XI&nap.registryCodeArray=NO&nap.registryCodeArray=PL&nap.registryCodeArray=PT&nap.registryCodeArray=RO&nap.registryCodeArray=SK&nap.registryCodeArray=SI&nap.registryCodeArray=ES&nap.registryCodeArray=SE&nap.registryCodeArray=&nap.registryCodeArray=GB&periodCode=-1&currentSortSettings=&resultList.currentPageNumber={page_number}&nextList=Next%3E',
        'tblNapSearchResult',
        6,
        2
    ],
    [
        'https://ec.europa.eu/clima/ets/caat.do?languageCode=fr&nap.registryCodeArray=AT&nap.registryCodeArray=BE&nap.registryCodeArray=BG&nap.registryCodeArray=HR&nap.registryCodeArray=CY&nap.registryCodeArray=CZ&nap.registryCodeArray=DK&nap.registryCodeArray=EE&nap.registryCodeArray=EU&nap.registryCodeArray=FI&nap.registryCodeArray=FR&nap.registryCodeArray=DE&nap.registryCodeArray=GR&nap.registryCodeArray=HU&nap.registryCodeArray=IS&nap.registryCodeArray=IE&nap.registryCodeArray=IT&nap.registryCodeArray=LV&nap.registryCodeArray=LI&nap.registryCodeArray=LT&nap.registryCodeArray=LU&nap.registryCodeArray=MT&nap.registryCodeArray=NL&nap.registryCodeArray=XI&nap.registryCodeArray=NO&nap.registryCodeArray=PL&nap.registryCodeArray=PT&nap.registryCodeArray=RO&nap.registryCodeArray=SK&nap.registryCodeArray=SI&nap.registryCodeArray=ES&nap.registryCodeArray=SE&nap.registryCodeArray=&nap.registryCodeArray=GB&periodCode=-1&currentSortSettings=&resultList.currentPageNumber={page_number}&nextList=Next%3E',
        'tblNapSearchResult',
        5,
        2
    ],
    [
        'https://ec.europa.eu/clima/ets/swissEuCaat.do?languageCode=fr&intAlloc.registryCodeArray=-1&intAlloc.registryCodeArray=AT&intAlloc.registryCodeArray=BE&intAlloc.registryCodeArray=BG&intAlloc.registryCodeArray=HR&intAlloc.registryCodeArray=CZ&intAlloc.registryCodeArray=DK&intAlloc.registryCodeArray=EE&intAlloc.registryCodeArray=FI&intAlloc.registryCodeArray=FR&intAlloc.registryCodeArray=DE&intAlloc.registryCodeArray=GR&intAlloc.registryCodeArray=HU&intAlloc.registryCodeArray=IS&intAlloc.registryCodeArray=IE&intAlloc.registryCodeArray=IT&intAlloc.registryCodeArray=LV&intAlloc.registryCodeArray=LU&intAlloc.registryCodeArray=MT&intAlloc.registryCodeArray=NL&intAlloc.registryCodeArray=NO&intAlloc.registryCodeArray=PL&intAlloc.registryCodeArray=PT&intAlloc.registryCodeArray=RO&intAlloc.registryCodeArray=ES&intAlloc.registryCodeArray=SE&intAlloc.registryCodeArray=&intAlloc.registryCodeArray=GB&currentSortSettings=&resultList.currentPageNumber={page_number}&nextList=Next%3E',
        'tblIntAllocSearchResult',
        2,
        2
    ],
    [
        "https://ec.europa.eu/clima/ets/account.do?languageCode=fr&account.registryCodes=AT&account.registryCodes=BE&account.registryCodes=BG&account.registryCodes=HR&account.registryCodes=CY&account.registryCodes=CZ&account.registryCodes=DK&account.registryCodes=EE&account.registryCodes=EU&account.registryCodes=FI&account.registryCodes=FR&account.registryCodes=DE&account.registryCodes=GR&account.registryCodes=HU&account.registryCodes=IS&account.registryCodes=IE&account.registryCodes=IT&account.registryCodes=LV&account.registryCodes=LI&account.registryCodes=LT&account.registryCodes=LU&account.registryCodes=MT&account.registryCodes=NL&account.registryCodes=XI&account.registryCodes=NO&account.registryCodes=PL&account.registryCodes=PT&account.registryCodes=RO&account.registryCodes=SK&account.registryCodes=SI&account.registryCodes=ES&account.registryCodes=SE&account.registryCodes=&account.registryCodes=GB&account.accountFullTypeCodes=100-7&account.accountFullTypeCodes=120-0&account.accountFullTypeCodes=100-9&account.accountFullTypeCodes=100-8&account.accountFullTypeCodes=121-0&account.accountFullTypeCodes=100-12&account.accountFullTypeCodes=100-13&account.accountFullTypeCodes=0-10&account.accountFullTypeCodes=0-11&account.accountFullTypeCodes=110-0&account.accountFullTypeCodes=100-0&account.accountFullTypeCodes=100-2&account.accountFullTypeCodes=100-5&account.accountFullTypeCodes=100-14&account.accountFullTypeCodes=100-15&account.accountFullTypeCodes=100-16&account.accountFullTypeCodes=100-17&account.accountFullTypeCodes=100-18&account.accountFullTypeCodes=100-19&account.accountFullTypeCodes=100-20&account.accountFullTypeCodes=100-21&account.accountFullTypeCodes=100-1&account.accountFullTypeCodes=100-3&account.accountFullTypeCodes=100-4&account.accountFullTypeCodes=100-24&account.accountFullTypeCodes=280-0&account.accountFullTypeCodes=270-0&account.accountFullTypeCodes=241-0&account.accountFullTypeCodes=130-0&account.accountFullTypeCodes=100-6&account.accountFullTypeCodes=100-25&account.accountFullTypeCodes=210-0&account.accountFullTypeCodes=100-26&account.accountFullTypeCodes=220-0&account.accountFullTypeCodes=230-0&account.accountFullTypeCodes=240-0&account.accountFullTypeCodes=250-0&account.accountFullTypeCodes=300-0&account.accountFullTypeCodes=411-0&account.accountFullTypeCodes=421-0&account.accountFullTypeCodes=422-0&account.accountFullTypeCodes=423-0&account.accountFullTypeCodes=100-27&account.accountFullTypeCodes=100-31&account.accountFullTypeCodes=100-29&account.accountFullTypeCodes=100-28&account.accountFullTypeCodes=100-30&account.accountFullTypeCodes=242-0&account.accountFullTypeCodes=100-22&account.accountFullTypeCodes=100-23&accountHolder=&searchType=account&currentSortSettings=&resultList.currentPageNumber={page_number}&nextList=Next%3E",
        "tblAccountSearchResult",
        5,
        1
    ],
    [
        'https://ec.europa.eu/clima/ets/oha.do?form=oha&languageCode=fr&account.registryCodes=AT&account.registryCodes=BE&account.registryCodes=BG&account.registryCodes=HR&account.registryCodes=CY&account.registryCodes=CZ&account.registryCodes=DK&account.registryCodes=EE&account.registryCodes=EU&account.registryCodes=FI&account.registryCodes=FR&account.registryCodes=DE&account.registryCodes=GR&account.registryCodes=HU&account.registryCodes=IS&account.registryCodes=IE&account.registryCodes=IT&account.registryCodes=LV&account.registryCodes=LI&account.registryCodes=LT&account.registryCodes=LU&account.registryCodes=MT&account.registryCodes=NL&account.registryCodes=XI&account.registryCodes=NO&account.registryCodes=PL&account.registryCodes=PT&account.registryCodes=RO&account.registryCodes=SK&account.registryCodes=SI&account.registryCodes=ES&account.registryCodes=SE&account.registryCodes=&account.registryCodes=GB&accountHolder=&installationIdentifier=&installationName=&permitIdentifier=&mainActivityType=-1&account.complianceStatusArray=0&account.complianceStatusArray=-&account.complianceStatusArray=A&account.complianceStatusArray=B&account.complianceStatusArray=C&account.complianceStatusArray=D&account.complianceStatusArray=E&account.complianceStatusArray=X&searchType=oha&currentSortSettings=&resultList.currentPageNumber={page_number}&nextList=Next%3E',
        "tblAccountSearchResult",
        10,
        1
    ]
]

conf_number = 1

URL = confs[conf_number][0]
table_id = confs[conf_number][1]
number_of_pages = confs[conf_number][2]
header_position = confs[conf_number][3]



def create_all_links(url, number_of_pages):
    links = []
    for page_number in range(number_of_pages):
        links.append(url.format(page_number = page_number))
    return links

def parse_table(link, table_id):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'id': table_id})
    return table

def construct_csv(url, number_of_pages, table_id, header_position):
    links = create_all_links(url, number_of_pages)
    tables = []
    for page_number, link in enumerate(links):
        print("[I] Parsing page number:", page_number+1)
        tables.append(parse_table(link, table_id))
    
    if len(tables) != 0:
        # -------------------- Header --------------------------------
        header_items = []
        header = tables[0].find_all("tr")[header_position]
        
        for items in header:
            try:
                header_items.append(items.get_text().strip()) if items.get_text().strip() != '' else ''
            except:
                continue

        # ---------------------- Tables data -------------------------
        data = []
        for table in tables:
            rows = table.find_all("tr")[header_position+1:]
            table_data = []
            for row in rows:
                row_data = []
                cells = row.findAll("td", {'class': 'bgcelllist'})
                for cell in cells:
                    try:
                        row_data.append(cell.get_text().strip()) if cell.get_text().strip() != '' else ''
                    except:
                        continue
                table_data.append(row_data) if len(row_data) != 0 else ''
            data.extend(table_data)
        
        dataFrame = pd.DataFrame(data = data, columns = header_items[:-1])
        print("[I] Generating CSV...")
        dataFrame.to_csv('result.csv')

    else: 
        raise("No table found")


print("[I] Starting scraping operation...")
print("[I] URL:", URL.format(page_number = 0))
print("[I] Number of pages:", number_of_pages)

construct_csv(URL, number_of_pages, table_id, header_position)

print("[I] Done.")
