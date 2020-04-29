import pandas as pd
import regex as re

df=pd.read_csv('snowflakedb.csv')

def pick_date(x):
	a_str=x.split()
	new_date=a_str[1]+" "+a_str[2]+","+a_str[5]
	return a_str


try:
  for i in range(df.shape[0]-1):
    df['new_date'][i]=pick_date(df['created_at'][i])
except:
  print(i)


df.to_csv("new.csv", index=False)