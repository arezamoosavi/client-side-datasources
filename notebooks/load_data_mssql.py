import pandas as pd
from sqlalchemy import create_engine
import urllib
import pyodbc


df = pd.read_csv("atm_data.csv", delimiter=",")

print(df.head())

quoted = urllib.parse.quote_plus(
    "DRIVER={FreeTDS};SERVER=sqldata;PORT=1433;DATABASE=tempdb;UID=sa;PWD=P@ssword"
)
engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(quoted))


df.to_sql(
    "atm", schema="dbo", con=engine, if_exists="replace", chunksize=200, method="multi", index=False
)

print("The data is saved into sql server on atm table!")

result = engine.execute("SELECT COUNT(*) FROM [dbo].[atm]")
all_count = result.fetchall()

print("all record count from atm: ", all_count)
