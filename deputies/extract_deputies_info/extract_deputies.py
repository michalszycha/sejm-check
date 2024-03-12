import pandas as pd
import requests
import re
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class DeputiesExtractor:
    @staticmethod
    def __get_deputies_list():
        logger.info("Deputies extraction starts.\n")
        url = "https://www.sejm.gov.pl/sejm10.nsf/poslowie.xsp?type=A"
        r = requests.get(url)

        soup = BeautifulSoup(r.content, "html.parser")

        deputies_list = []

        deputies_raw = soup.find_all('a', id=re.compile("Poslowie"))
        for deputy in deputies_raw:
            deputy_id = re.search("id=(\d{3})", deputy.get('href')).group(1)
            deputy_name = deputy.get_text().split()[1]
            deputy_lastname = deputy.get_text().split()[0]
            deputies_list.append(
                {
                    'id': deputy_id,
                    'imie': deputy_name,
                    'nazwisko': deputy_lastname,
                }
            )
            logger.info(f"Found deputy {deputy_name} {deputy_lastname} with id {deputy_id}")
        logger.info("Deputies extraction ends.\n")
        return deputies_list

    @staticmethod
    def __get_info(soup: BeautifulSoup, info: str):
        try:
            return soup.find('p', id=re.compile(info, re.IGNORECASE)).parent.find('p', {'class': 'right'}).get_text()
        except AttributeError:
            return None

    def __update_deputies_list(self, deputies):
        logger.info("Deputies info update starts.\n")
        for deputy in deputies:
            deputy.update(self.__get_deputy_personal_info(deputy['id']))
            logger.info(f"Updated {deputy['imie']} {deputy['nazwisko']}")
        logger.info("Deputies info update ends.\n")
        return deputies

    def __get_deputy_personal_info(self, deputy_id: str):
        info_list = ['lista', 'okreg', 'glosy', 'klub', 'urodzony', 'wyksztalcenie', 'szkola', 'zawod']

        url = f"https://www.sejm.gov.pl/sejm10.nsf/posel.xsp?id={deputy_id}&type=A"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        personal_info = dict()

        for info in info_list:
            personal_info[info] = self.__get_info(soup, info)

        return personal_info

    def get_deputies_as_df(self, save_to_file: bool = False):
        deputies = self.__get_deputies_list()
        deputies = self.__update_deputies_list(deputies)
        deputies_df = pd.DataFrame(deputies)
        if save_to_file:
            deputies_df.to_csv("deputies.csv", sep=',')
        return deputies_df
