#%%
import config
import pandas as pd
import sqlalchemy as sa
import json
import numpy as np

DB, DB_STRING = config.get_database_connection()

try:
    engine = sa.create_engine(DB_STRING, echo = False)
    connection = engine.connect()

    print("Connected to {} Database!".format(DB))
except Exception as e:
    msg = "Database {} or Module not found".format(DB)
    print(msg)
    raise e

df = pd.read_json(config.JSON_FILE)
print(df.head())

try:
    df.to_sql(name=config.TARGET_TABLE, con=engine, schema=DB,
                if_exists='append', index=False)

    print("\nSuccessfully insert into {} database".format(DB))
except Exception as e:
    print("An error occurs during upload to mysql!")
    raise e

print("Finished!")