import logging
import os
from deputies.extract_deputies_info.extract_deputes import save_deputies_to_csv

log_path = "./logs"
log_file = "app.log"


def setup_logging():
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f"{log_path}/{log_file}"),
            logging.StreamHandler()
        ]
    )


def main():
    setup_logging()
    save_deputies_to_csv('deputies.csv')


if __name__ == "__main__":
    main()
