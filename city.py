import pandas as pd
from IPython.core.display import display
df=pd.options.display.float_format='{:.2f}'.format
df= pd.read_csv("original.csv")
#display(df)
print("AVERAGE OF each column")
print(df[['population','average_temperature','average_rainfall']].mean())
print("MIN VALUE OF each column")
print(df[['population','average_temperature','average_rainfall']].min())
print("MAx VALUE OF each column")
print(df[['population','average_temperature','average_rainfall']].max())
df['Ratio(temp/rainfall)']=(df['average_temperature']/df['average_rainfall'])
display(df)
df.to_csv('new_csv.csv')
