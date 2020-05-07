import random

# Функция формирует список длины N случайных имен списка names_list
def F(names_list, N):
    result=[None]*N # Инициализация списка из N пустых элементов
    for i in range (0,N):
        result[i]=names_list[int(random.random()*len(names_list))]
    return result
    # 2 способ - Использование готовой функции:
    # return random.choices(names_list, k=N)

# Функция вычисляет наиболее частое имя
def Common_Word(list):
    stat={}
    for i in range(0,len(list)):
        if list[i] in stat.keys():
            stat[list[i]]+=1
        else:
            stat[list[i]]=1
    sorted_list=sorted(stat,key=stat.get, reverse=True)
    return sorted_list[0]

# Функция вычисляет наиболее редкой начальной буквы
def Rare_Letter(list):
    stat={}
    for i in range(0,len(list)):
        if list[i][0:1] in stat.keys():
            stat[list[i][0:1]]+=1
        else:
            stat[list[i][0:1]]=1
    sorted_list=sorted(stat,key=stat.get, reverse=False)
    return sorted_list[0]

# Функция определяет дату последнего лога в файле:
def Last_Log_file(filename):
    text_file = open(filename, "r")
    lines = text_file.readlines()
    # print(lines)
    # print(len(lines))
    text_file.close()

    sorted_lines=sorted(lines,reverse=True)
    # print(sorted_lines[0])
    return sorted_lines[0][0:23]

if __name__=='__main__' :
    Names=['Алексей', 'Анна', 'Александр', 'Екатерина', 'Павел', 'Мария', 'Артемий', 'Андрей', 'Ирина', 'Олимпиада'
        , 'Надежда', 'Сергей', 'Вера', 'Любовь', 'Тимофей', 'Иоанн', 'Пётр', 'Ксения', 'София', 'Марфа']

    ch_list=F(Names, N=100)
    print(ch_list)

    print(Common_Word(ch_list))

    print(Rare_Letter(ch_list))

    print(Last_Log_file('log'))


# with open('log','r') as f:
#     for line in f:
#         curdate=line[0:23]
#         print(curdate)
#


# f=open('log', 'r')
# for line in f:
#     print(line)
# # content=f.read()
# # print(content)
# f.close()
