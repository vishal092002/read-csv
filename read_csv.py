"""Reads CSV File For Testing """
import pandas as pd

df= pd.read_csv('numbers.csv')

#4print(df)

value_1=df['value_1']
#print(value_1)

value_2=df['value_2']
#print(value_2)

result=df['result']
#print(result)

new_result=value_1+value_2
#print(new_result)

test_result=df[(df['result'] == new_result)]
print(test_result)