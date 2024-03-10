import logging
from deputies.extract_deputies_info.extract_deputes import save_deputies_to_csv


def setup_logging():
    logging.basicConfig(filename='./logs/app.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    setup_logging()
    save_deputies_to_csv('deputies.csv')


if __name__ == "__main__":
    main()
