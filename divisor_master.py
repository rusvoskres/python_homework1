import math
 # 2. Выводим список всех делителей числа
def get_num_dividers(num):
    div=[1]
    for i in range(2,num):
        # print(i)
        if num%i==0:
            div.append(i)
    div.append(num)
    return div

# 1. Проверка числа на простоту:
def is_num_simple(num):
    is_simple=True
    for i in range(2,num):
        # print(i)
        if num%i==0:
            is_simple = False
            break # завершаем - уже ясно, что число не простое
    return is_simple
    # другой способ - простой в использовании, но менее оптимальный
    # Если число делителей = 2 (1 и само число), то значит число простое:
    # return 1 if len(get_num_dividers(num))==2 else 0

# 3. Определяем самый большой простой делитель числа - при isSimleDividerOnly=True:
# 5. Определяем самый большой (не обязательно простой) делитель числа - при isSimleDividerOnly=False:
def get_max_simple_divider(num, isSimleDividerOnly=True):
    max_simple_divider=1
    for i in range(num-1,1,-1): #Если само число тоже считаем делителем, то начинаем цикл от num
        # print(i)
        if num%i==0:
            if isSimleDividerOnly and is_num_simple(i) \
                    or isSimleDividerOnly==False:
                max_simple_divider=i
                break # завершаем - найден наибольший делитель
    return max_simple_divider

# 4. Pro - Делаем каноническое разложение числа на простые множители:
def get_canon_decomposition_num(num):
    decomp_list=[]
    remainder=int(num)
    while remainder>2: #not is_num_simple(remainder):
        # print(remainder)
        max_div=int(math.sqrt(remainder)) # мин. делитель не может быть больше кв. корня числа
        is_div_found=False
        for i in range(2,max_div+1):
            # print(remainder, i)
            if remainder%i==0: #нашли наименьший делитель
                # print(remainder, i, '!!!')
                decomp_list.append(i)
                remainder=int(remainder/i)
                is_div_found=True
                break

        if remainder==2:
            decomp_list.append(remainder)
            break
        if not is_div_found: # если не нашли больше делителей - остался остаток - простое число
            decomp_list.append(remainder)
            break
    return decomp_list


# Проверки модуля:
if __name__=='__main__':
    # 2. Выводим список всех делителей числа
    print(get_num_dividers(8))
    # 1. Проверка числа на простоту:
    print(is_num_simple(14))
    # 3. Определяем самый большой простой делитель числа - при isSimleDividerOnly=True:
    print(get_max_simple_divider(282))
    # 5. Определяем самый большой (не обязательно простой) делитель числа - при isSimleDividerOnly=False:
    print(get_max_simple_divider(282, isSimleDividerOnly=False))
    # 4. Pro - Делаем каноническое разложение числа на простые множители:
    print(get_canon_decomposition_num(897924289))
    print(get_canon_decomposition_num(3400))
    print(get_canon_decomposition_num(1024))
    print(get_canon_decomposition_num(7))
