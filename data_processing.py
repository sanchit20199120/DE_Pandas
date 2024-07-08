import pandas as pd

def read_csv_file(file_name):
    try:
        df = pd.read_csv(file_name)
    except FileNotFoundError:
        print("File not found in the given location")
    else:
        print(df)
#read_csv_file('/Users/sanchitbhardwaj/PycharmProjects/DE_Pandas/cost.csv')