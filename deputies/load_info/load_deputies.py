import pandas as pd
import logging
from sqlalchemy import create_engine, inspect

logger = logging.getLogger(__name__)

class DeputiesLoader:
    @staticmethod
    def load_deputies(deputies: pd.DataFrame):
        engine = create_engine('sqlite:///deputies.db')

        inspector = inspect(engine)
        if inspector.has_table('deputies'):
            engine.execute('DROP TABLE deputies')

        deputies.to_sql('deputies', engine, index=False)
