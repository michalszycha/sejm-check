import logging
import pandas as pd
import re

logger = logging.getLogger(__name__)


class DeputiesTransformer:
    @staticmethod
    def __transform_date(deputies: pd.DataFrame):
        logger.info("Separate birthday column\n")
        deputies['data urodzenia'] = deputies['urodzony'].apply(lambda x: x.split(', ')[0])
        deputies['miejsce urodzenia'] = deputies['urodzony'].apply(lambda x: x.split(' ')[1])
        deputies = deputies.drop('urodzony', axis=1)
        return deputies

    @staticmethod
    def __transform_district(deputies: pd.DataFrame):
        logger.info("Separate district column\n")
        deputies['okreg nr'] = deputies['okreg'].apply(lambda x: re.split(r'\s+', x)[0])
        deputies['okreg miasto'] = deputies['okreg'].apply(lambda x: re.split(r'\s+', x)[1])
        deputies = deputies.drop('okreg', axis=1)
        return deputies

    def transform_deputies(self, deputies: pd.DataFrame, save_to_file: bool = False):
        deputies = self.__transform_date(deputies)
        deputies = self.__transform_district(deputies)
        if save_to_file:
            deputies.to_csv("transformed_deputies.csv", sep=',')
        return deputies


    
