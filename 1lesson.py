import string

name = "Anastasia"
print(name)
age = 19
print("I am ", age)
print(name * 5, " If I use *")
print(name + name + name + name + name, " If I use +")

username = input("What is ur name?\n")
print("Hi! ", username)
try:
    userage = input("How old r u?\n")
    userage = int(userage)
    print(userage, " U r so baby)))")
except ValueError:
    print("Just enter the numbers")
    userage = input("How old r u?\n")
    userage = int(userage)
    print(userage, " U r so baby)))")

if userage <= age:
    print("U are really baby")
elif userage > 150:
    print("Hi... ghost...")
    userage = int(input("Ur real age?\n"))
elif userage < 0:
    print("Hi... time traveler...")
    userage = int(input("Ur real age?\n"))
else:
    print("it doesn't matter that u r older\n")

print(username[1:], " from 2 symbol")
print(username[::-1], " backwards")
print(username[-3::], " last 3 symbols")
print(username[:5:], " first 5 symbols")

let = list(username)
count = len(let)
print(count, " number of letters")

numbers_of_userage = [int(a) for a in str(userage)]
sumnum = sum(numbers_of_userage)
print(sumnum, " sum of numbers of ur age")

prodd = 1
for i in range(len(numbers_of_userage)):
    prodd *= numbers_of_userage[i]
print(prodd, " prod of numbers of ur age")

print(username.lower())
print(username.upper())
print(username.capitalize())
print(username.swapcase())

print("How much is 2+2*2?\n")
answer = int(input())
if answer == 6:
    print("U r genius!")
else:
    print("U r loser, try agan")
    answer1 = int(input())
    if answer1 == 6:
        print("Good for u")
print("Thx!")