import pandas as pd
sales=pd.read_csv("sales.csv")
m=sales['USERID'].unique()
cus=pd.read_csv("cust.csv")
#print(m)
filt=m
filt=cus["TSIID"].isin(filt)
cus=cus.loc[filt]
print(cus)
print("customers each salesmam have")
print(cus["TSIID"].value_counts())