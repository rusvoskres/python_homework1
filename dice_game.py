import random
class Dice:
    def __init__(self, N):
        self.throw_num=N
        self.current_throw=0

    def set_hidden_numbers(self):
        self._hidden_num1 = random.randint(1,6)
        self._hidden_num2 = random.randint(1,6)

    def __str__(self):
        return f'Загаданы 2 числа от 1 до 6. У вас есть {self.throw_num} попыток их угадать'

    def show_result(self):
        return f'Были загаданы числа: ({self._hidden_num1}, {self._hidden_num2}).'

    def throw_dices(self):
        self.current_throw+=1
        if self.current_throw>self.throw_num:
            raise Exception('Вы превысили количество попыток')
        print(f'Попытка номер: {self.current_throw}')
        dice_1 = int(input('Введите первое число:'))
        dice_2 = int(input('Введите второе число:'))
        print(f'Вы ввели числа: ({dice_1}, {dice_2})')
        if {dice_1, dice_2} == {self._hidden_num1,self._hidden_num2}:
            return True
        else:
            return False

if __name__ == '__main__':
    dice_game=Dice(5)
    dice_game.set_hidden_numbers()
    print(dice_game)
    try:
        for i in range(15):
            result = dice_game.throw_dices()
            print(result)
            if result:
                print('Вы выиграли!!!')
                print(dice_game.show_result())
                break
    except:
        print('Игра закончена. Вы проиграли')
        print(dice_game.show_result())
