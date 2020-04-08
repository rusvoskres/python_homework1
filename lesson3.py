# -*- coding: utf8 -*-
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

my_text='Все счастливые семьи похожи друг на друга, каждая несчастливая семья несчастлива по-своему.' \
'Все смешалось в доме Облонских. Жена узнала, что муж был в связи с бывшею в их доме француженкою-гувернанткой, и объявила мужу, что не может жить с ним в одном доме. Положение это продолжалось уже третий день и мучительно чувствовалось и самими супругами, и всеми членами семьи, и домочадцами. Все члены семьи и домочадцы чувствовали, что нет смысла в их сожительстве и что на каждом постоялом дворе случайно сошедшиеся люди более связаны между собой, чем они, члены семьи и домочадцы Облонских. Жена не выходила из своих комнат, мужа третий день не было дома. Дети бегали по всему дому, как потерянные; англичанка поссорилась с экономкой и написала записку приятельнице, прося приискать ей новое место; повар ушел вчера со двора, во время самого обеда; черная кухарка и кучер просили расчета.' \
'На третий день после ссоры князь Степан Аркадьич Облонский — Стива, как его звали в свете, — в обычный час, то есть в восемь часов утра, проснулся не в спальне жены, а в своем кабинете, на сафьянном диване. Он повернул свое полное, выхоленное тело на пружинах дивана, как бы желая опять заснуть надолго, с другой стороны крепко обнял подушку и прижался к ней щекой; но вдруг вскочил, сел на диван и открыл глаза.' \
'«Да, да, как это было? — думал он, вспоминая сон. — Да, как это было? Да! Алабин давал обед в Дармштадте; нет, не в Дармштадте, а что-то американское. Да, но там Дармштадт был в Америке. Да, Алабин давал обед на стеклянных столах, да, — и столы пели: Il mio tesoro 1 и не Il mio tesoro, а что-то лучше, и какие-то маленькие графинчики, и они же женщины», — вспоминал он.' \
'Глаза Степана Аркадьича весело заблестели, и он задумался, улыбаясь. «Да, хорошо было, очень хорошо. Много еще что-то там было отличного, да не скажешь словами и мыслями даже наяву не выразишь». И, заметив полосу света, пробившуюся сбоку одной из суконных стор, он весело скинул ноги с дивана, отыскал ими шитые женой (подарок ко дню рождения в прошлом году), обделанные в золотистый сафьян туфли, и по старой, девятилетней привычке, не вставая, потянулся рукой к тому месту, где в спальне у него висел халат. И тут он вспомнил вдруг, как и почему он спит не в спальне жены, а в кабинете; улыбка исчезла с его лица, он сморщил лоб.' \
'«Ах, ах, ах! Ааа!..» — замычал он, вспоминая все, что было. И его воображению представились опять все подробности ссоры с женою, вся безвыходность его положения и мучительнее всего собственная вина его.' \
'«Да! она не простит и не может простить. И всего ужаснее то, что виной всему я, виной я, а не виноват. В этом-то вся драма, — думал он. — Ах, ах, ах!» — приговаривал он с отчаянием, вспоминая самые тяжелые для себя впечатления из этой ссоры.' \
'Неприятнее всего была та первая минута, когда он, вернувшись из театра, веселый и довольный, с огромною грушей для жены в руке, не нашел жены в гостиной; к удивлению, не нашел ее и в кабинете и, наконец, увидал ее в спальне с несчастною, открывшею все, запиской в руке.' \
'Она, эта вечно озабоченная, и хлопотливая, и недалекая, какою он считал ее, Долли, неподвижно сидела с запиской в руке и с выражением ужаса, отчаяния и гнева смотрела на него.' \
'— Что это? это? — спрашивала она, указывая на записку.' \
'И при этом воспоминании, как это часто бывает, мучало Степана Аркадьича не столько самое событие, сколько то, как он ответил на эти слова жены.' \
'С ним случилось в эту минуту то, что случается с людьми, когда они неожиданно уличены в чем-нибудь слишком постыдном. Он не сумел приготовить свое лицо к тому положению, в которое он становился перед женой после открытия его вины. Вместо того чтоб оскорбиться, отрекаться, оправдываться, просить прощения, оставаться даже равнодушным — все было бы лучше того, что он сделал! — его лицо совершенно невольно («рефлексы головного мозга», — подумал Степан Аркадьич, который любил физиологию), совершенно невольно вдруг улыбнулось привычною, доброю и потому глупою улыбкой.' \
'Эту глупую улыбку он не мог простить себе. Увидав эту улыбку, Долли вздрогнула, как от физической боли, разразилась, со свойственною ей горячностью, потоком жестоких слов и выбежала из комнаты. С тех пор она не хотела видеть мужа.'

# 1) методами строк очистить текст от знаков препинания;
my_text=my_text.replace(',',' ').replace('.', ' ').replace('?', ' ').replace('!', ' ')\
    .replace(';', ' ').replace('—', ' ').replace('-', ' ').replace('«', ' ').replace('»', ' ')\
    .replace('(', ' ').replace(')', ' ').replace(':', ' ').replace(')', ' ')
print(type(my_text), my_text)

# 3) привести все слова к нижнему регистру (map);
# 5) выполнить light с условием: в пункте 2 дополнительно к приведению к нижнему регистру выполнить лемматизацию.
my_list=list(map(lambda x:morph.parse(x.lower())[0].normal_form
                 , list(filter(lambda x:x!='' # отфилььровываем пустые элементы
# 2) сформировать list со словами (split);
                               , my_text.split(' '))) ))
print(type(my_list),my_list)

stat={}
# 3) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
for i in range(0,len(my_list)):
    #print(my_list[i])
    if my_list[i] in stat.keys():
         stat[my_list[i]]+=1
    else:
        stat[my_list[i]]=1

set=set(stat)

# 4) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).
sorted_list=sorted(stat, key=stat.get, reverse=True)
print(sorted_list,type(sorted_list))

for i in range(5):
    print('Слово "', sorted_list[i], '" встречается в тексте', stat[sorted_list[i]] ,' раз' )

print('Другой способ, вывести сразу, без промежуточной переменной типа list:')
i=0
for w in sorted(stat, key=stat.get, reverse=True):
    print('Слово "', w, '" встречается в тексте', stat[w],' раз')
    i+=1
    if i==5 : break

# вывести количество разных слов в тексте (set).
# Тут set вроде не обязателен? Можно получить и из list или в чем идея?
print(stat, type(stat))
print(set, type(set))
print(stat.__len__())
print(set.__len__())
