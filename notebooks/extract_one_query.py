import time
import sys
import pandas as pd
import pyodbc


server = "sqldata"
database = "tempdb"
user = "sa"
table = "dbo.atm"
password = "P@ssword"

engine = pyodbc.connect(
    "DRIVER={{FreeTDS}};SERVER={};PORT=1433;DATABASE={};UID={};PWD={}".format(
        server, database, user, password
    )
)


def main(item_number, file_name):

    tic = time.time()

    query = "SELECT TOP {} * FROM {};".format(item_number, table)

    df = pd.read_sql(query, engine)

    toc = time.time()

    df.to_csv("{}.csv".format(file_name), index=False)

    print("the data shape is: {} and saved to {}".format(df.shape, file_name))
    print(
        "It take {} seconds to take {} data from {} table".format(
            toc - tic, item_number, table
        )
    )


if __name__ == "__main__":

    item_number = int(sys.argv[1])
    file_name = str(sys.argv[2])

    main(item_number, file_name)

