import random
import json

with open('city.json', 'r', encoding='utf-8') as f:  # открыли файл
    text = json.load(f)  # загнали все из файла в переменную


gor = []
abc = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']
for txt in text:
    gor.append(txt['city'])


city_double = [[]]
for i in range(len(abc)):
    city_double.append([])
    for j in gor:
        if abc[i] == j[0].lower():
            city_double[i].append(j)


city = input()
print(city[-1])



used_city = []
used_city.append(city)

number1 = abc.index(city[0].lower())
number = abc.index(city[-1].lower())

if city in city_double[number1]:
    city_double[number1].pop(city_double[number1].index(city))

print(city_double[number1])

# print(number)
#
# print(pussyboy[number])
#
# print(random.choice(pussyboy[number]))



random_choice = random.choice(city_double[number])

print(random_choice)

if random_choice in city_double[number]:
    city_double[number].pop(city_double[number].index(random_choice))
print(city[number])

used_city.append(random_choice)


