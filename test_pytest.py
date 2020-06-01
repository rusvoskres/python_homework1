fib_num= lambda n:fib_num(n-1)+fib_num(n-2) if n>2 else 1

print(fib_num(6))

def test1_fib_num():
    assert (fib_num(6)==8)

def test2_fib_num():
    assert (fib_num(5)==5)


def test3_fib_num():
    n = 10
    assert (fib_num(2*n)==fib_num(n+1)**2 - fib_num(n-1)**2)
