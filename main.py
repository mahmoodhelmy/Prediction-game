import random


print("welcome to guessing game where you will have to guess the number predicted by cpu")
tries_wallet =[]
x=int(input("First input your first number: "))
y=int(input("Now input your second number"))
z=random.randint(x,y)
t=int(input("Now you have to predict my number pal, you have only three tries, Good luck! "))
while len(tries_wallet) != 3:
    tries_wallet.append(t)
    if t ==z:
        print("Nice catch")
        break
    else:
        t=int(input("Try again: "))
    if len(tries_wallet) == 3:
        print("You have used all your tries,Good luck next time")
        break




