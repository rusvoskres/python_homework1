import datetime
import os
import psutil

def show_time(f):
    def wrapper(*args,**kwargs):
        sd = datetime.datetime.now()
        # print(f(*args,**kwargs))
        ret=f(*args, **kwargs)
        print((datetime.datetime.now()-sd).microseconds,' milliseconds')
    return wrapper

def show_memory(f):
    def wrapper(*args,**kwargs):
        proc = psutil.Process(os.getpid())
        ms = proc.memory_info().rss
        ret=f(*args, **kwargs)
        proc = psutil.Process(os.getpid())
        print(str(proc.memory_info().rss-ms),' Bytes used')
    return wrapper

@show_time
@show_memory
def create_list_without_generator(num):
    list_sq=[]
    for i in range(1,num+1):
        list_sq.append(i)
    return list_sq

@show_time
@show_memory
def create_list_with_generator_seq(num):
    list_sq=[i for i in range(1,num+1)]
    return list_sq

@show_time
@show_memory
def create_list_with_generator(num):
    list_sq=[]
    for i in range(1,num+1):
        # list_sq.append(i)
        yield i
    return list_sq

create_list_without_generator(1000000)
create_list_with_generator_seq(1000000)
create_list_with_generator(1000000)

# gen=create_list_with_generator(19)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


