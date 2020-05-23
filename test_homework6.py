from divisor_master import *
from lesson4 import *

def test1_get_canon_decomposition_num():
    assert(get_canon_decomposition_num(937*967*991*991)==[937, 967, 991, 991])
    assert (get_canon_decomposition_num(3400) == [2, 2, 2, 5, 5, 17])
    assert (get_canon_decomposition_num(1024) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

def test2_get_canon_decomposition_num():
    assert(get_canon_decomposition_num(7)==[7])
    assert(get_canon_decomposition_num(11) == [11])
    assert (get_canon_decomposition_num(1) == [1])
    assert (get_canon_decomposition_num(2) == [2])


def test3_get_num_dividers():
    assert(get_num_dividers(8)==[1, 2, 4, 8])

def test4_is_num_simple():
    assert(is_num_simple(14)==False)
    assert (is_num_simple(7)==True)

def test5_get_max_simple_divider():
    # 3. Определяем самый большой простой делитель числа - при isSimleDividerOnly=True:
    assert(get_max_simple_divider(282)==47)
    # 5. Определяем самый большой (не обязательно простой) делитель числа - при isSimleDividerOnly=False:
    assert(get_max_simple_divider(282, isSimleDividerOnly=False)==141)

# Pro
def test6_F():
    Names = ['Алексей', 'Анна', 'Александр', 'Екатерина', 'Павел', 'Мария', 'Артемий', 'Андрей', 'Ирина', 'Олимпиада'
        , 'Надежда', 'Сергей', 'Вера', 'Любовь', 'Тимофей', 'Иоанн', 'Пётр', 'Ксения', 'София', 'Марфа']
    ch_list = F(Names, N=100)
    assert(len(ch_list)==100)

def test7_Rare_Letter():
    Names = ['Алексей', 'Анна', 'Александр', 'Екатерина', 'Артемий', 'Андрей']
    assert(Rare_Letter(F(Names, N=100)) == 'Е')
