import logging
import os
import deputies.extract_deputies_info.extract_deputies as dp

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
    x = dp.DeputiesExtractor()
    x.get_deputies_as_df("deputies.csv")


if __name__ == "__main__":
    main()
