# Простой декоратор
def show_information(f):
    def wrapper(*args,**kwargs):
        print('Код до функции')
        f(*args,**kwargs)
        print('Код после функции')
    return wrapper

def simple_function():
    print('Я простая функция')

@show_information
def another_simple_function():
    print('Я тоже простая функция')
#
# simple_function()
#
# simple_function_decorated = show_information(simple_function)
#
# simple_function_decorated()
#
# another_simple_function()


# Декораторы с параметрами
def show_type(f):
    def wrapper(*args,**kwargs):
        print('Код1 до функции', type(args[0]))
        print(f(*args,**kwargs))
        print('Код1 после функции', type(args[1]))
    return wrapper

@show_information
@show_type
def my_add(a,b):
    return a+b

my_add(10,20)

# Пример

import time
import datetime
import requests

def show_time(f):
    def wrapper(*args,**kwargs):
        print(time.time())
        sd = datetime.datetime.now()
        print('url=',args[0])
        print(f(*args,**kwargs))
        print((datetime.datetime.now()-sd).microseconds,' milliseconds')
    return wrapper

@show_time
def request_example(url):
    webpage=requests.get(url)
    return webpage.text

url='https://google.com'
url='http://yandex.ru'
data = request_example(url)
print(data)

