import os
import pandas

print(os.listdir())#list with all files folders in current directory

df1=pandas.read_json("supermarkets.json")
print(df1)

