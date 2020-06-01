import pickle

data = {'1': {1,2,3,1}, '2':['a','b','c','a'], '3': {0,1,2,0}}
print(data)

with open('data.pickle', 'wb') as f:
    pickle.dump(data,f)

with open('data.pickle', 'rb') as f:
    data_load=pickle.load(f)

print(data_load)

import csv
--------------------------------  CSV ---------------------------------------------------------
car_data = [['brand','price','year'],['volvo',1.5,'2017'],['lada',0.5,2018], ['audi',2.0,2019]]
print(car_data, type(car_data))

with open('example.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='&')
    writer.writerows(car_data)

print('Writing complete')

with open('example.csv') as f:
    reader=csv.reader(f,delimiter='&')
    for row in reader:
        print(row)

data_dict= [{'Name':'Dima', 'age':28},
            {'age':29, 'Name':'Kate'},
            {'Name':'Mike', 'age':31}]

field_names=['Name','age']
print(type(data_dict), data_dict)

with open('example_1.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f,delimiter='&', fieldnames=field_names)
    writer.writeheader()
    for i in range(len(data_dict)):
        writer.writerow(data_dict[i])

with open('example_1.csv') as f:
    reader=csv.DictReader(f, delimiter='&')
    for row in reader:
        print(dict(row))

import pandas as pd

DataFrame_from_csv = pd.read_csv('example_1.csv', sep='&')
print(DataFrame_from_csv)

--------------------------------  JSON ---------------------------------------------------------
import json

# dict_ex={'brand': 'Volvo', 'price': 1.50, 'Vol':     2.0}
dict_ex = [{'brand': 'Volvo', 'price': 1.50, 'Vol': 2.0}
           ,{'brand': 'Lada', 'price': 0.50, 'Vol': 1.0}
           ]

dict_to_json = json.dumps(dict_ex)
print(type(dict_to_json), dict_to_json)

with open('dict_to_json.txt', 'w', newline='') as f:
    json.dump(dict_ex, f)

with open('dict_to_json.txt', 'r') as f:
    data=json.load(f)

print(type(data), data)

data1 = json.loads(dict_to_json)
print(type(data1), data1)

import requests
response = requests.get('https://jsonplaceholder.typicode.com/todos')
todos=json.loads(response.text)

print(type(response), response)
print(type(todos), todos)

with open('todos.txt', 'w', newline='') as f:
    json.dump(response.text, f)

