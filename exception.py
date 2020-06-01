try:

    a=int(input('Введите первое число'))
    b=int(input('Введите второе число'))

    print(a/b)
except ZeroDivisionError as e:
    print('Так нельзя: ', e)
else:
    print('Все хорошо!')
finally:
    print('Это было не просто')