---
title: "Data Engineering: Pandas"
date: 2020-04-29 11:33:00 +0800
categories: [Data Engineering, Python, Pandas]
tags: [pandas]
---


All code is in [my github](https://github.com/byambaa1982/snowflake_data_scrape/blob/master/)

## Goal

I am asked to scrape and extract data [this website](https://snowflakecommunity.force.com/s/global-search/%40uri#q=snowflake&t=All&sort=relevancy&f:Type=[Answers]) 


### Data that we need to scape

index| ID                 |               created_at              |      new_date
-----| -------------------| --------------------------------------| ----------------|
0    | 1255161549892837376| Tue Apr 28 15:46:47 +0000 2020| name 1| Apr 28,2020     |
1    | 1255159041283719169| Tue Apr 28 15:36:49 +0000 2020| name 2| Apr 28,2020     | 
2    | 1255158930076053505| Tue Apr 28 15:36:23 +0000 2020| name 3| Apr 28,2020     |         

### Code explained 

Import the libraries which we need

```python 
import pandas as pd
import regex as re
```
Read CSV file into pandas dataframe
```python
df=pd.read_csv('snowflakedb.csv')
```
Split string into a list and pick right indice we need. 

```python
def pick_date(x):
	a_str=x.split()
	new_date=a_str[1]+" "+a_str[2]+","+a_str[5]
	return a_str
```
Create new feature using the above function
```python
try:
  for i in range(df.shape[0]-1):
    df['new_date'][i]=pick_date(df['created_at'][i])
except:
  print(i)
```

Create a new CSV file 

```python
df.to_csv("new.csv", index=False)
```

If you have anything to ask, please contact me clicking following link?


You can hire me [here](https://www.fiverr.com/coderjs)

Thank you