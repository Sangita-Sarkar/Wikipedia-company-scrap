import requests
from bs4 import BeautifulSoup
import json

def extract_data(url):
    data = {}

    required_fields = ["Trade name", "Industry", "Company type", "Founders", "Headquarters", "Products", "Number of employees"]
    to_list_process = ["Industry", "Founders", "Products"]

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    table_class = "infobox ib-company vcard"
    htmltable = soup.find('table', {'class': table_class})

    trs = htmltable.find_all('tr')

    for row in trs:
        th = row.find('th')
        td = row.find('td')
        if th:
            if th.text in required_fields:
                if th.text in to_list_process:
                    li_data = []
                    if td:
                        lis = td.find_all('li')
                        for li_elem in lis:
                            li_data.append(li_elem.text)
                        data[th.text] = li_data
                else:
                    data[th.text] = td.text

    print(data)


extract_data("https://en.wikipedia.org/wiki/Nvidia")