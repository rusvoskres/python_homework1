# ---- Тернарные операторы ----------------------------------------------
age=17
def check_adult(age):
    check = 0
    if age>=18:
        check=1
    else:
        check=0
    return check

check = 1 if age>=18 else 0

check_adult_1 = lambda x: 1 if age>=18 else 0

print(check_adult(age), check, check_adult_1(age))

# ---- Генераторы последовательностей ----------------------------------------------
# Список
list_sq = []

N=10
for i in range(1,N+1):
    list_sq.append(i**2%10)

print(list_sq)

list_sq_q= [(i**2)%10 for i in range(1,N+1) if (i**2)%2==0]
print(list_sq_q)

# Словарь
dict_g= {i:i**2 for i in range(1,N+1)}
print(dict_g)

# Множество
set_g= {i**2 for i in range(1,N+1)}
set_g_d= {i**2%10 for i in range(1,N+1)}
print(set_g,set_g_d)

# Задача
list_names = ['Dima', 'Kate', 'oleg', 'Natali']
list_char = [x[0] if x[0].isupper() else x[0].title() for x in list_names ]
print(list_char)