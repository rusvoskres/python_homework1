import sys
simple_list = [x**3 for x in range(100)]
print(type(simple_list))

# for i in simple_list:
#     print(i)

print('Memory simple_list:',sys.getsizeof(simple_list))

# неявные генераторы
simple_generator = (x**3 for x in range(100))
print(type(simple_generator))

# for i in simple_generator:
#     print(i)

print('Memory simple_generator:',sys.getsizeof(simple_generator))

# Явные генераторы

def generator_example_1(num):
    for i in range(num):
        yield(i**3)

gen=generator_example_1(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

import datetime
import os
import random
import psutil

colors = ['White', 'Black', 'Green']
brands = ['Volvo', 'Lada', 'Audi']

def cars(n):
    car_list = []
    for i in range(0,n):
        car={'colour':random.choice(colors),
             'brand':random.choice(brands),
             'id':i
             }
        car_list.append(car)
    return car_list

proc = psutil.Process(os.getpid())

print('Исп. память до вып. функции:' + str(proc.memory_info().rss/1000000))
beg=datetime.datetime.now()
cars_list = cars(1000000)
end=datetime.datetime.now()

proc = psutil.Process(os.getpid())
print('Исп. память после вып. функции:' + str(proc.memory_info().rss/1000000))
# print(cars_list)
print('Заняло {} секунд'.format(end-beg))


def cars_gen(n):
    car_list = []
    for i in range(0,n):
        car={'colour':random.choice(colors),
             'brand':random.choice(brands),
             'id':i
             }
        # car_list.append(car)
        yield car
    return car_list

print('Исп. память до вып. функции:' + str(proc.memory_info().rss/1000000))
beg=datetime.datetime.now()
cars_generator = cars_gen(1000000)
end=datetime.datetime.now()

proc = psutil.Process(os.getpid())
print('Исп. память после вып. функции:' + str(proc.memory_info().rss/1000000))
# print(cars_list)
print('Заняло {} секунд'.format(end-beg))

