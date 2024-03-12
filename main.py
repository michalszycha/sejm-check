import logging
import os
import deputies.extract_deputies_info.extract_deputies as dp_extract
import deputies.transform_deputies_info.transform_deputies as dp_transform

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
    extractor = dp_extract.DeputiesExtractor()
    transformer = dp_transform.DeputiesTransformer()
    deputies = extractor.get_deputies_as_df(True)
    transformer.transform_deputies(deputies, True)
    


if __name__ == "__main__":
    main()
