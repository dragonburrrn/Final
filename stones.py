import random

Stones = int(input())
S = 0

def d1(S):
    S += 2
    return S

def d2(S):
    S *= 2
    return S

while S != 60:
    playerch = int(input())

    if playerch == 1:
        S = d1(S)
    else:
        S = d2(S)
    print("После игрока: ", S)

    if S >= 60:
        winner = "Человек"
        break

    Compch = random.random()

    if Compch % 2 == 1:
        S = d1(S)
    else:
        S = d2(S)

    print("После компа: ", S)

    if S >= 60:
        winner = "Компьютер"
        break

print(S)
print(winner)
