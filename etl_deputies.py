import logging
import os
from deputies.extract_info.extract_deputies import DeputiesExtractor
from deputies.transform_info.transform_deputies import DeputiesTransformer
from deputies.load_info.load_deputies import DeputiesLoader

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
    deputies = DeputiesExtractor.get_deputies()
    deputies = DeputiesTransformer.transform_deputies(deputies)
    DeputiesLoader.load_deputies(deputies)


if __name__ == "__main__":
    main()
