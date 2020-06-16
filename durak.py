import random
from typing import List, Any


class Durak:
    _deck: List[Any]

    def __init__(self, first_attack, debug, is_comp_automatic=True, is_user_automatic=False):
        self.debug=debug
        self.user_turn_card = 0
        self.comp_turn_card = 0
        self.is_comp_automatic=is_comp_automatic
        self.is_user_automatic=is_user_automatic
        self.current_attack=first_attack # Кто атакует - 'user' или 'comp' - другой отбивается
        # self.current_turn = 'user' # Кто ходит - 'user' или 'comp' - либо ходит, либо отбивается
        self.is_last_attack_successfull = False
        self.suits = ['Трефа', 'Пика', 'Бубна', 'Черва']
        self.values = ['6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
        self._deck = [] # Колода карт
        self.active_cards = [] # Активные карты во время данного хода
        self.broken_cards = []  # Битые карты
        self.user_cards_known = [] # Польз. карты, о которых известно противнику (их взял при неудачных отбивках)
        self.comp_cards_known = []  # карты компа, о которых известно противнику (их взял при неудачных отбивках)
        # составляем полную колоду:
        for suit in self.suits:
             for value in self.values:
                 cur_card =[]
                 cur_card.append(suit)
                 cur_card.append(value)
                 cur_card.append(0) # вычисляемый порядок для хода- чем меньше, тем более предпочитительнее,
                 # что этой картой комп будет ходить и отвечать
                 self._deck.append(cur_card)

        # составляем перемешанную колоду
        rearranged_cards = []
        for i in range(len(self._deck)):
            cur_rnd=random.choices(self._deck, k=1)
            rearranged_cards.append(cur_rnd[0])
            self._deck.remove(cur_rnd[0])
        self._deck = rearranged_cards

        # Раздача карт пользователю и компу
        self.user_cards = []
        self._comp_cards = []
        for i in range(6):
            self.user_cards.append(self._deck[0])
            self._deck.remove(self._deck[0])
            self._comp_cards.append(self._deck[0])
            self._deck.remove(self._deck[0])
        # Следующая карта определяет козырь
        trump_card=self._deck[0]
        self.trump=trump_card[0]
        # Карту с козырем переносим в конец колоды:
        self._deck.remove(trump_card)
        self._deck.append(trump_card)
        # print(self._deck)

    # Вычисляем порядок карт для оптимального хода - чем меньше,тем более предпочитительнее,
    # что этой картой комп будет ходить и отвечать
    def calc_card_order_attack(self, card, cards):
        # Смотрим не козярная ли масть:
        trump_value=0
        if card[0]==self.trump:
            trump_value=9
        # Вычисляем количество таких же карт других мастей для выгодного хода:
        # (Комп старается ходить и отвечать парными картами)
        quantity_in_cards=-1
        for cur_card in cards:
            if card[1]==cur_card[1]:
                if cur_card[0]!=self.trump:
                    quantity_in_cards+=1
                else:
                    quantity_in_cards += 0.5
        # if self.debug:
        #     print(f'self.values.index(card[1])={self.values.index(card[1])}')
        #     print(f'trump_value={trump_value}')
        #     print(f'quantity_in_cards={quantity_in_cards}')
        return self.values.index(card[1])+trump_value-quantity_in_cards*3

    # Вычисляем порядок карт для оптимального ответа на атаку - чем меньше,тем более предпочитительнее,
    # что этой картой комп будет ходить и отвечать
    def calc_card_order_under_attack(self, card, cards):
        enemy_cards_known=[] # карты противника, о которых известно
        if self.current_attack=='user':
            # Атакует пользователь, - значит отбивается комп, а его противник - пользователь:
            enemy_cards_known = self.user_cards_known
        else:
            enemy_cards_known = self.comp_cards_known

        # Смотрим не козырная ли масть:
        trump_value=0
        if card[0]==self.trump:
            trump_value=9
        # Вычисляем количество таких же карт других мастей для выгодного хода:
        # (Комп старается отвечать парными картами)
        quantity_in_cards=-1
        for cur_card in cards:
            if card[1]==cur_card[1]:
                if cur_card[0]!=self.trump:
                    quantity_in_cards+=1
                else:
                    quantity_in_cards += 0.5

        # Вычисляем количество таких же карт других мастей в активных картах для выгодного хода:
        # (Комп старается отвечать картами, значения которых уже задействованы
        # - тогда меньше шансов, что у противника подобные найдутся)
        for cur_card in self.active_cards:
            if card[1]==cur_card[1]:
                if cur_card[0]!=self.trump:
                    quantity_in_cards+=1
                else:
                    quantity_in_cards+=0.5

        # Вычисляем количество таких же карт других мастей в битых картах для выгодного хода:
        # (Комп старается отвечать картами, значения которых уже были задействованы
        # - тогда меньше шансов, что у противника подобные найдутся)
        for cur_card in self.broken_cards:
            if card[1]==cur_card[1]:
                if cur_card[0]!=self.trump:
                    quantity_in_cards+=1
                else:
                    quantity_in_cards+=0.5

        # Стараемся не отбиваться картами, подобными тем, которые точно есть у противника
        # Чтобы он не завалил нас при своей атаке
        quantity_in_enemy_cards = 0
        for cur_card in enemy_cards_known:
            if card[1]==cur_card[1]:
                if cur_card[0]!=self.trump:
                    quantity_in_enemy_cards+=1
                else:
                    quantity_in_enemy_cards+=0.5
        # if self.debug:
        #     print(f'self.values.index(card[1])={self.values.index(card[1])}')
        #     print(f'trump_value={trump_value}')
        #     print(f'quantity_in_cards={quantity_in_cards}')
        return self.values.index(card[1])+trump_value-quantity_in_cards*4+quantity_in_enemy_cards*40

    def sort_cards(self, cards, is_attack):
        for cur_card in cards:
            if is_attack:
                cur_card[2]=self.calc_card_order_attack(cur_card, cards)
            else:
                cur_card[2]=self.calc_card_order_under_attack(cur_card, cards)
            # print(cur_card)
        cards = sorted(cards, key=lambda x:x[2])
        # print(cards)
        return cards

    def sort_user_cards(self):
        # is_attack=True
        if self.current_attack=='user':
            is_attack=True
        else:
            is_attack=False

        self.user_cards = self.sort_cards(self.user_cards, is_attack=is_attack)


    def sort_comp_cards(self):
        if self.current_attack=='user':
            is_attack=False
        else:
            is_attack=True
        self._comp_cards = self.sort_cards(self._comp_cards, is_attack=is_attack)

    def is_card_greater(self, greater_card, card):
        if greater_card[0]==card[0]:
            if self.values.index(greater_card[1])>self.values.index(card[1]):
                return True
            else:
                return False
        elif greater_card[0]==self.trump:
            return True
        else:
            return False

    def user_attack(self, is_debug):
        self.current_attack = 'user'
        self.is_attack_success=None
        is_attack_continue=True
        while is_attack_continue and not self.is_game_over():
            durak.sort_comp_cards()
            durak.sort_user_cards()
            # if is_debug:
            #     durak.show_debug()
            durak.show_situation()
            print('----------------------------- Ваша атака ----------------------------------')
            is_attack_continue = self.user_turn()
            if is_attack_continue:
                print('----------------------------- Ответ компа ----------------------------------')
                is_attack_continue = self.comp_turn()
                print(f'is_attack_continue = {is_attack_continue}')
            print('----------------------------------------------------------------------------')

    def comp_attack(self, is_debug):
        self.current_attack='comp'
        self.is_attack_success = None
        is_attack_continue=True
        while is_attack_continue and not self.is_game_over():
            durak.sort_comp_cards()
            durak.sort_user_cards()
            # if is_debug:
            #     durak.show_debug()
            durak.show_situation()
            print('----------------------------- Атака компа ----------------------------------')
            is_attack_continue = self.comp_turn()
            if is_attack_continue:
                print('----------------------------- Ваш ответ ----------------------------------')
                is_attack_continue = self.user_turn()
                print(f'is_attack_continue = {is_attack_continue}')
            print('----------------------------------------------------------------------------')

    # Допустимые номера карт для атаки
    def get_acceptable_attack_turn_nums(self, optimal_only=False):
        cards=[]
        result=[]
        if self.current_attack=='user':
            cards = self.user_cards
        else:
            cards = self._comp_cards

        # Первый ход при атаке нужно сходить в любом случае
        # даже если все карты очень хорошие и жалко отдавать:
        if self.active_cards==[]:
            optimal_only=False

        for card in cards:
            is_value_found=False
            if len(self.active_cards)==0:
                is_value_found=True
            else: # должна быть среди активных в текушей атаке:
                for cur_active_card in self.active_cards:
                    if card[1]==cur_active_card[1]:
                        if not optimal_only:
                            is_value_found = True
                        # не отдаем хорошие карты:
                        elif optimal_only and self.values.index(card[1])<=5 and card[0]!=self.trump:
                            is_value_found = True
            if is_value_found:
                result.append(cards.index(card))
        return result

    # Вычисляет допустимые номера карт для отбивающегося игрока
    def get_acceptable_under_attack_turn_nums(self):
        cards=[]
        result=[]
        if self.current_attack=='user':
            cards = self._comp_cards
            enemy_turn_card = self.user_turn_card
        else:
            cards = self.user_cards
            enemy_turn_card = self.comp_turn_card

        for cur_card in cards:
            # print(cur_card)
            # Ищет чем можно отбиться:
            is_found_card = False
            if self.is_card_greater(cur_card, enemy_turn_card):
                # self.comp_turn_card_num=self._comp_cards.index(cur_card)
                player_turn_card = cur_card
                is_found_card = True
                # break
            if is_found_card:
                result.append(cards.index(cur_card))
        return result

    # Ход атакующего, а другой будет отбиваться
    def attack_turn(self, is_automatic, is_give_extra_cards):
        turn_card_num=0
        player_cards=[]
        # enemy_cards_known = []  # карты противника, о которых известно
        player_cards_known = []  # карты игрока, о которых известно противнику
        if self.current_attack=='user':
            player_cards=self.user_cards
            # enemy_cards_known = self.comp_cards_known
            player_cards_known = self.user_cards_known
        else:
            player_cards=self._comp_cards
            # enemy_cards_known = self.user_cards_known
            player_cards_known = self.comp_cards_known

        acceptable_attack_turn_nums = self.get_acceptable_attack_turn_nums()
        if is_automatic:
            acceptable_optima_attack_turn_nums =  self.get_acceptable_attack_turn_nums(optimal_only=is_give_extra_cards)
            if acceptable_optima_attack_turn_nums!=[]:
                turn_card_num=acceptable_optima_attack_turn_nums[0]
            else:
                turn_card_num=-1
        else:
            contunue_answer = True
            print(f'Ваши карты: {list([x[0],x[1]] for x in player_cards)}')
            print(f'Допустимые номера карт для хода:{list(x + 1 for x in acceptable_attack_turn_nums)}')
            if acceptable_attack_turn_nums==[]:
                turn_card_num = -1
                print('Нечем дальше ходить - атака закончена!')
                if not is_give_extra_cards:
                    self.is_last_attack_successfull=False
                if not(self.is_user_automatic and self.is_comp_automatic):
                    stub=input('Нажмите Enter для продолжения...')
            while contunue_answer and acceptable_attack_turn_nums!=[]:
                # print(f'Ваши карты: {player_cards}')

                user_input = input(f'Ваш ход - вы атакуете: (введите номер карты от 1 до {len(player_cards)}). 0 - если закончили:')
                # print(turn_card_num)
                if user_input=='d':#debug
                    self.show_debug()
                    turn_card_num = 100
                elif user_input=='a':#auto
                    acceptable_optima_attack_turn_nums = self.get_acceptable_attack_turn_nums(optimal_only=True)
                    if acceptable_optima_attack_turn_nums != []:
                        turn_card_num = acceptable_optima_attack_turn_nums[0]
                    else:
                        turn_card_num = -1
                elif user_input.isnumeric():
                    turn_card_num = int(user_input)-1
                else:
                    turn_card_num=100

                if turn_card_num in acceptable_attack_turn_nums or turn_card_num==-1:
                    contunue_answer=False
                else:
                    print(f'Введите допустимый номер карты({list(x+1 for x in acceptable_attack_turn_nums)}) или 0 для окончания атаки')

        if turn_card_num>=0:
            # self.user_turn_card = player_cards[turn_card_num]
            player_turn_card=player_cards[turn_card_num]
            print(f'Ход:       ***{player_turn_card[0]} {player_turn_card[1]}***')
            if not(self.is_user_automatic and self.is_comp_automatic):
                stub=input('Нажмите Enter для продолжения...')
            self.active_cards.append(player_turn_card)
            player_cards.remove(player_turn_card)
            for cur_player_cards_known in player_cards_known:
                if player_turn_card[0]==cur_player_cards_known[0] and player_turn_card[1]==cur_player_cards_known[1]:
                    player_cards_known.remove(cur_player_cards_known)

            # Сохраняем ход атакующегося в переменных класса
            if self.current_attack=='user':
                self.user_turn_card=player_turn_card
            else:
                self.comp_turn_card=player_turn_card
            # self.current_turn = 'comp'
        else:
            if not is_give_extra_cards:
                # конец атаки - все бито, заносим все активные карты в битые:
                self.is_last_attack_successfull=False
                for card in self.active_cards:
                    self.broken_cards.append(card)
                self.active_cards=[]
                return False
            else: # Конец доброски доп. карт противнику, когда он не отбил
                return False
        return True

    # Ход - отбивка
    def under_attack_turn(self, is_automatic):
        turn_card_num=0
        player_cards=[]
        player_cards_known = []  # карты игрока, о которых известно противнику
        if self.current_attack=='user':
            # Атакует пользователь - значит отбивается компьютер
            player_name = 'Компьютер'
            player_cards=self._comp_cards
            # enemy_turn_card=self.user_turn_card
            player_turn_card=self.comp_turn_card
            player_cards_known = self.comp_cards_known
        else:
            # Атакует компьютер - значит отбивается пользователь
            player_name = 'Пользователь'
            player_cards=self.user_cards
            # enemy_turn_card = self.comp_turn_card
            player_turn_card = self.user_turn_card
            player_cards_known = self.user_cards_known

        acceptable_under_attack_turn_nums = self.get_acceptable_under_attack_turn_nums()
        # Берем первую подходящую в сортированном по приоритетам хода списке:
        if is_automatic:
            if acceptable_under_attack_turn_nums!=[]:
                turn_card_num=acceptable_under_attack_turn_nums[0]
            else:
                turn_card_num=-1
        else:
            contunue_answer = True
            print(f'Ваши карты: {list([x[0], x[1]] for x in player_cards)}')
            print(f'Допустимые номера карт для хода:{list(x + 1 for x in acceptable_under_attack_turn_nums)}')
            if acceptable_under_attack_turn_nums == []:
                turn_card_num = -1
                print('Нечем дальше ходить - отбивка закончена провалом!')
                self.is_last_attack_successfull=True
                if not(self.is_user_automatic and self.is_comp_automatic):
                    stub=input('Нажмите Enter для продолжения...')
            while contunue_answer and acceptable_under_attack_turn_nums != []:
                # print(f'Ваши карты: {player_cards}')
                user_input = input(f'Ваш ход - вы отбиваетесь: (введите номер карты от 1 до {len(player_cards)}). 0 - если берете:')
                if user_input == 'd': #debug
                    self.show_debug()
                    turn_card_num = 100
                elif user_input == 'a': #auto
                    acceptable_under_attack_turn_nums = self.get_acceptable_under_attack_turn_nums()
                    if acceptable_under_attack_turn_nums != []:
                        turn_card_num = acceptable_under_attack_turn_nums[0]
                    else:
                        turn_card_num = -1
                elif user_input.isnumeric():
                    turn_card_num = int(user_input) - 1
                else:
                    turn_card_num = 100

                if turn_card_num in acceptable_under_attack_turn_nums or turn_card_num == -1:
                    contunue_answer = False
                else:
                    print(f'Введите допустимый номер карты({list(x + 1 for x in acceptable_under_attack_turn_nums)}) или 0 если берете')

        # print('Ход компьютера:')
        # if is_found_card:
        if turn_card_num>-1:
            player_turn_card=player_cards[turn_card_num]
            print(f'{player_name} ходит так: ***{player_turn_card[0]} {player_turn_card[1]}***')

            # print(player_turn_card)
            self.active_cards.append(player_turn_card)
            player_cards.remove(player_turn_card)
            # if player_turn_card in player_cards_known:
            #     player_cards_known.remove(player_turn_card)
            for cur_player_cards_known in player_cards_known:
                if player_turn_card[0]==cur_player_cards_known[0] and player_turn_card[1]==cur_player_cards_known[1]:
                    player_cards_known.remove(cur_player_cards_known)
            # Сохраняем ход отбивающегося игрока в переменных класса:
            if self.current_attack == 'user':
                self.comp_turn_card = player_turn_card
            else:
                self.user_turn_card = player_turn_card
            if not(self.is_user_automatic and self.is_comp_automatic):
                stub = input('Нажмите Enter для продолжения...')
            return True
        else: # Нечем отбиться:
            print(f'{player_name} говорит: Нечем крыть! Беру!')
            if not(self.is_user_automatic and self.is_comp_automatic):
                stub=input('Нажмите Enter для продолжения...')
            self.is_last_attack_successfull=True
            # self._comp_cards.append(self.user_turn_card)
            print('Дача доп. карт противнику:')
            is_continue=True
            while is_continue:
                if self.current_attack=='user':
                    is_automatic=self.is_user_automatic
                else:
                    is_automatic=self.is_comp_automatic
                print(f'is_automatic={is_automatic}')
                is_continue= self.attack_turn(is_automatic=is_automatic, is_give_extra_cards=True)
            for card in self.active_cards:
                print(f'{player_name} берет карту {card}')
                player_cards.append(card)
            if not(self.is_user_automatic and self.is_comp_automatic):
                stub=input('Нажмите Enter для продолжения...')
            # Противник запоминает карты, которые были взяты:
            for card in self.active_cards:
                player_cards_known.append(card)
            self.active_cards=[]
                # self.active_cards.remove(card)
            return False
            # self.user_cards.remove(self.user_cards[self.user_turn_card_num])
        # return True

    # Ход пользователя
    def user_turn(self):
        if self.current_attack == 'user':
            return self.attack_turn(is_automatic=self.is_user_automatic, is_give_extra_cards=False)
        else:
            return self.under_attack_turn(is_automatic=self.is_user_automatic)

        return True

    def comp_turn(self):
        if self.current_attack == 'user':
            return self.under_attack_turn(is_automatic=self.is_comp_automatic)
        else:
            return self.attack_turn(is_automatic=self.is_comp_automatic, is_give_extra_cards=False)

    def show_debug(self):
        print('*** Отладочная информация ***')
        print(f'В колоде осталось {len(self._deck)} карт:')
        print(self._deck)
        print(f'Активных  {len(self.active_cards)} карт:')
        print(self.active_cards)
        for card in self.active_cards:
            print(f'активная карта {card}')
        print(f'Битых  {len(self.broken_cards)} карт:')
        print(self.broken_cards)

        print(f'Пользовательских засвеченых {len(self.user_cards_known)} карт:')
        print(self.user_cards_known)

        print(f'Компьютерных засвеченых {len(self.comp_cards_known)} карт:')
        print(self.comp_cards_known)

        print(f'У компьютера осталось {len(self._comp_cards)} карт:')
        print(self._comp_cards)

        print(f'У Вас осталось {len(self.user_cards)} карт:')
        print(self.user_cards)
        # print(f'Козырь: {self.Trump}:')
        # print(f'Козырь: {self.suits.index(self.Trump)}:')
        print('*** Отладочная информация конец ***')

    def show_situation(self):
        print(f' В колоде осталось {len(self._deck)} карт:')
        print(f'У компьютера осталось {len(self._comp_cards)} карт:')
        print(f'У Вас осталось {len(self.user_cards)} карт:')
        print(list([x[0],x[1]] for x in self.user_cards))
        print(f'Козырь: {self.trump}:')

    # Добор карт из колоды
    def add_on_cards(self):
        if len(self._deck)==0:
            return False
        print('Добор карт:')
        if self.current_attack=='user':
            # Карты добирает пользователь:
            while len(self.user_cards)<6 and len(self._deck)>0:
                cur_card=self._deck[0]
                print(f'Вы добрали из колоды карту: [{cur_card[0]} {cur_card[1]}]')
                if len(self._deck)==1: #последняя карта - она засвечена и известна противнику
                    self.user_cards_known.append(cur_card)
                self.user_cards.append(cur_card)
                self._deck.remove(cur_card)
            # Карты добирает комп:
            while len(self._comp_cards)<6 and len(self._deck)>0:
                cur_card=self._deck[0]
                if len(self._deck)==1: #последняя карта - она засвечена и известна противнику
                    self.comp_cards_known.append(cur_card)
                    print(f'Комп добрал из колоды последнюю карту: [{cur_card[0]} {cur_card[1]}]')
                self._comp_cards.append(cur_card)
                self._deck.remove(cur_card)

        if self.current_attack=='comp':
            # Карты добирает комп:
            while len(self._comp_cards)<6 and len(self._deck)>0:
                cur_card=self._deck[0]
                if len(self._deck) == 1:  # последняя карта - она засвечена и известна противнику
                    self.comp_cards_known.append(cur_card)
                    print(f'Комп добрал из колоды последнюю карту: [{cur_card[0]} {cur_card[1]}]')
                self._comp_cards.append(cur_card)
                self._deck.remove(cur_card)
            # Карты добирает пользователь:
            while len(self.user_cards)<6 and len(self._deck)>0:
                cur_card=self._deck[0]
                print(f'Вы добрали из колоды карту: [{cur_card[0]} {cur_card[1]}]')
                if len(self._deck)==1: #последняя карта - она засвечена и известна противнику
                    self.user_cards_known.append(cur_card)
                self.user_cards.append(cur_card)
                self._deck.remove(cur_card)
        return True

    def is_game_over(self):
        if len(self._deck)>0:
            return False
        elif len(self.user_cards)==0 or len(self._comp_cards)==0:
            return True
        else:
            False

    def play(self, is_debug):
        while not self.is_game_over():
            durak.sort_comp_cards()
            durak.sort_user_cards()
            # durak.show_debug()
            durak.show_situation()
            if self.current_attack=='user':
                self.user_attack(is_debug)
            else:
                self.comp_attack(is_debug)
            # print(f'is_attack_success = {self.is_last_attack_successfull}')
            if self.is_last_attack_successfull:
                print('Атака успешна')
            else:
                print('Атака провалилась')
            if not(self.is_user_automatic and self.is_comp_automatic):
                stub = input('Нажмите Enter для продолжения...')
            durak.add_on_cards()
            if not self.is_last_attack_successfull:
                if self.current_attack=='user':
                    self.current_attack='comp'
                else:
                    self.current_attack='user'

        if is_debug:
            self.show_debug()
        if len(self.user_cards)==0:
            print('*** Примите поздравления!!! Вы победитель!!! ***')
        elif len(self._comp_cards)==0:
            print('*** Увы! В этот раз Вы проиграли! ***')


if __name__ == '__main__':
    # Игра с пользователем - пользователь ходит сам. Первым ходит компьютер:
    # durak = Durak(first_attack = 'comp', debug=True, is_comp_automatic=True, is_user_automatic=False)

    # Полностью автоматическая игра - первым ходит компьютер
    # durak = Durak(first_attack='comp', debug=True, is_comp_automatic=True, is_user_automatic=True)
    # Полностью автоматическая игра - первым ходит пользователь
    durak = Durak(first_attack='user', debug=True, is_comp_automatic=True, is_user_automatic=True)
    durak.play(is_debug=True)


    # durak.user_cards.append(['Трефа', 'Туз', 0])
    # durak.user_cards.append(['Бубна', 'Туз', 0])
    # durak.user_cards.append(['Пика', 'Туз', 0])
    # durak.user_cards.append(['Черва', 'Туз', 0])

    # durak._comp_cards.append(['Трефа', 'Туз', 0])
    # durak._comp_cards.append(['Бубна', 'Туз', 0])
    # durak._comp_cards.append(['Пика', 'Туз', 0])
    # durak._comp_cards.append(['Черва', 'Туз', 0])
    # durak._comp_cards.append(['Черва', '8', 0])
    # durak.user_cards_known.append(['Трефа', '8', 0])
    # durak.user_cards.append(['Трефа', '8', 0])
    # # durak.user_cards_known.append(['Пика', '9', 0])
    # durak.user_cards.append(['Трефа', 'Туз', 0])
    # durak.comp_cards_known.append(['Черва', 'Туз', 0])
    # durak._comp_cards.append(['Черва', 'Туз', 0])
    # durak.trump = 'Черва'
    # durak.comp_cards_known.append(['Черва', '7', 0])


    # durak.user_attack(is_debug=True)
    # durak.current_attack='comp'
    # durak.comp_attack(is_debug=True)
    # print(f'is_attack_success = {durak.is_last_attack_successfull}')
    # durak.show_debug()
    # durak.add_on_cards()
    # durak.show_debug()
    #

