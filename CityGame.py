import random
import json

# открываем json файл
with open('city.json', 'r', encoding='utf-8') as f:  # открыли файл
    text = json.load(f)  # загнали все из файла в переменную

# массив из городов и букв
gor = []
abc = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']
for txt in text:
    gor.append(txt['city'])
#print(gor)


# двумерный массив с гродами по алфавиту
city_double = [[]]
for i in range(len(abc)):
    city_double.append([])
    for j in gor:
        if abc[i] == j[0].lower():
            city_double[i].append(j)
#print(city_double)

#-----------------------------------------------------------
# начало игры:

game = True

while game == True:
    # игрок
    city = input()
    if city == "Стоп":
        game = False
    else:

        # исключаем ь,ъ,ы,ё

        if city[-1] == 'ъ' or city[-1] == 'ы' or city[-1] == 'ь' or city[-1] == 'ё':
            number1 = abc.index(city[0].lower())
            number = abc.index(city[-2].lower())
#            print(city[-2])
        else:
            number = abc.index(city[-1].lower())
            number1 = abc.index(city[0].lower())
#            print(city[-1])

        # создаем массив использованных городов
        #used_city = []

        # исключаем город игрока из массива
        if city in city_double[number1]:
            city_double[number1].pop(city_double[number1].index(city))
        #    used_city.append(city)
        else:
            print('Вы проиграли, такого города нет или вы повторились')
            break

        # выбор компьютера
        random_choice = random.choice(city_double[number])
        print(random_choice)

        # исключаем его выбор
        if random_choice in city_double[number]:
            city_double[number].pop(city_double[number].index(random_choice))
        #    used_city.append(random_choice)
        else:
            print('Вы проиграли, такого города нет')



#print(used_city)
