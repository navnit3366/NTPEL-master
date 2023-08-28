'''
Lab Experiment 3b : Write a program to guess a number between 1 to 9
'''

import random
p=1
r=random.randint(1,9)
while p:
    num=int(input("Guess a digit:"))
    if num==r:
        print("Well Guessed!\n ")
        p=0
    else:
        print("Oops wrong guess! :( \n Try again!")
        
