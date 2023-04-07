import pandas as pd
#pd.options.display.max_rows = 3
# df = pd.read_csv('veh_20.csv')
#print(df)
#print(df.head(1))
# print(df.tail(1))
# print(df.to_string())
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = pd.DataFrame(mydataset)

# print(myvar)
# a = [1, 7, 2]

# myvar = pd.Series(a)

# print(myvar[2])

# a = [1, 7, 2]

# myvar = pd.Series(a, index = ["x", "y", "z"])

# print(myvar)

#refer to the row index:
# print(myvar.loc[0])

#Data cleaning
df = pd.read_csv('veh_20.csv')
na_df = df.dropna()
# print(na_df)
na_df['Date'] = pd.to_datetime(na_df['Date'])

print(na_df.to_string())