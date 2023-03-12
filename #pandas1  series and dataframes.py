import pandas as pd 
import numpy as np
# there are main two datatypes in the pandas h
# this are  the Series and dataframes 

s1=pd.Series([23,34,56,78,97,556])

#s1.index('a','b','c','d','e','f')

# this will always  print in the table format 

#the Series must written as the Series

# the series also has the names 

s1.name=' the something'





print(s1)

print(s1.dtype)



# user defined indexing  for the table 

s2=pd.Series( [23,34,56,78,97,556], index=( 'a','b','c','d','e','f'))


print(s2)

# creating the new series using the particular columns 

s3=pd.Series(s2,index=('a','b'))

print(s3)





