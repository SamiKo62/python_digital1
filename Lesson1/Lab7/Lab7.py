'''
The cube Game
 The player enter the amount of money that he want to play with
 each Game is 3 NIS the player enter the amount of money is 30 NIS the player can play 10 games if
 the player enter 31 NIS he can play 10 games but the program will notify that he has 1 NIS
 spear.
 In each game the player draw 2 cubes (each cube is 1-6)
 if the number of the 2 cubes are equal the player gain 100NIS
 if the number of the 2 cubes are equal and the number is 6 the player gain 1000 NIS
 if the number on the cubes are not equal and cube 2 equal to 2 the player gain 40 NIS
 if the number on the cubes are not equal and cube 1 equal to 1 the player gain 20 NIS
 if not the player do not gain money.
'''
from random import randint
from time import sleep
print("Wellcome to the cube Game\n..............\n")
amnt=input("Enter the amount of money to play each game is 3 NIS:")
gam=int(amnt)//3
c= int(amnt) % 3
print("You have:" + str(gam) +  "games")
print("Throwing dice \n...........\n")
b=0
b1=100
b2=1000
b3=20
b4=40
for i in range(0, gam):
    sleep(2)
    cub1=randint(1,6)
    cub2=randint(1,6)
    print("Game number:" + str(i+1) + "\n..........\n""Cube1:" + str(cub1) + "\ncube2:" + str(cub2))
    if(cub1==cub2):
        if (cub1 == 6):
            print("You won 1000 NIS")
            b = b + b2
        else:
            print("You won 100 NIS")
            b = b1+b
    elif(cub1==1):
        print("You won 20 NIS")
        b =  b + b3
    elif(cub2==2):
        print("You won 40 NIS")
        b = b + b4
    else:
        print("Sorry you did not win")
print("The amount of wining is:" + str(b) + " NIS ")
print("You have extra money: " + str(c) + " NIS ")
print("You have total amount of money: " + str(b+c) + " NIS ")











