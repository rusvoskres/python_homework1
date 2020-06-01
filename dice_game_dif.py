from dice_game import Dice

class Dice_dif(Dice):
    def __init__(self, N,type):
        super().__init__(N)
        self.type_game=type

    def __str__(self):
        super().__str__()
        if self.type_game == 1:
            return f'Нужно угадать числа как непорядоченную пару'
        elif self.type_game==2:
            return f'Нужно угадать хотя бы одно значение'
        elif self.type_game==3:
            return f'Нужно, чтобы совпадали суммы чисел'

    def throw_dices(self):
        # type 1: совпала как непорядоченная пара
        # type 2: совпало хотя бы одно значение
        # type 3: совпала сумма

        self.current_throw+=1
        if self.current_throw>self.throw_num:
            raise Exception('Вы превысили количество попыток')
        print(f'Попытка номер: {self.current_throw}')
        dice_1 = int(input('Введите первое число:'))
        dice_2 = int(input('Введите второе число:'))
        print(f'Вы ввели числа: ({dice_1}, {dice_2})')
        if self.type_game ==1:
            if {dice_1, dice_2} == {self._hidden_num1,self._hidden_num2}:
                return True
            else:
                return False
        elif self.type_game == 2:
            if dice_1 in {self._hidden_num1, self._hidden_num2} \
                    or dice_2 in {self._hidden_num1, self._hidden_num2}:
                return True
            else:
                return False
        elif self.type_game == 3:
            if dice_1+dice_2 == self._hidden_num1+self._hidden_num2:
                return True
            else:
                return False

if __name__ == '__main__':
    dice_game=Dice_dif(5, 2)
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
