import pandas as pd
import logging
from sqlalchemy import create_engine, inspect, text

logger = logging.getLogger(__name__)


class DeputiesLoader:
    @staticmethod
    def load_deputies(deputies: pd.DataFrame):
        engine = create_engine("sqlite:///deputies.db")
        inspector = inspect(engine)
        connection = engine.connect()

        if inspector.has_table("deputies"):
            connection.execute(text("DROP TABLE deputies"))

        deputies.to_sql("deputies", engine, index=False)

        connection.close()
