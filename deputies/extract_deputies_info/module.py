import requests
import re
from bs4 import BeautifulSoup


def get_deputies_list():
    url = "https://www.sejm.gov.pl/sejm10.nsf/poslowie.xsp?type=A"
    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")

    deputies_list = []

    deputies_raw = soup.find_all('a', id=re.compile("Poslowie"))
    for deputy in deputies_raw:
        deputies_list.append(
            {
                'id': re.search("id=(\d{3})", deputy.get('href')).group(1),
                'imie': deputy.get_text().split()[1],
                'nazwisko': deputy.get_text().split()[0]
            }
        )

    return deputies_list


def get_deputy_personal_info(deputy_id: str):

    info_list = ['lista', 'okreg', 'glosy', 'klub', 'urodzony', 'wyksztalcenie', 'szkola', 'zawod']

    url = f"https://www.sejm.gov.pl/sejm10.nsf/posel.xsp?id={deputy_id}&type=A"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    personal_info = dict()

    for info in info_list:
        personal_info[info] = get_info(soup, info)

    return personal_info


def get_info(soup: BeautifulSoup, info: str):
    return soup.find('p', id=re.compile(info, re.IGNORECASE)).parent.find('p', {'class': 'right'}).get_text()


x = get_deputies_list()
y = get_deputy_personal_info(x[0]['id'])
print(x[0])
print(y)
