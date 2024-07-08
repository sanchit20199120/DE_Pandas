import pandas as pd

df1 = pd.read_csv('/Users/sanchitbhardwaj/PycharmProjects/DE_Pandas/costs.csv')
print(df1)
print(df1)
print(df1.shape)
print(df1.columns)
print(df1['EC2-Other($)'].unique())
print(df1['EC2-Other($)'].nunique())


df2 = pd.read_csv('/Users/sanchitbhardwaj/PycharmProjects/DE_Pandas/costs.csv')
print(df2)

test_result = df1.compare(df2)
print(test_result)  # there is no difference in the df1 and df2 means test result pass at location1 and location 2



