'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
import random

upperRange = int(input("Enter the upper limit of the secret number: "))
randomNumber = random.randrange(upperRange)
root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300, background='orange')
canvas1.pack()
title = tk.Label(root, text='Random Number Game', fg='blue', font=('Comic Sans MS', 19, 'bold'), background='orange')
canvas1.create_window(150, 50, window=title)
instructions = tk.Label(root, text='Put your guess in the box below and click guess', background='orange')
canvas1.create_window(150, 75, window=instructions)

numberEnt = StringVar()
number = tk.Entry(root, textvariable=numberEnt)


def guess():
    x = number.get()
    if int(x) > randomNumber:
        label1 = tk.Label(root, text='Too High', fg='green', font=('Comic Sans MS', 25, 'bold'), background='orange')
        canvas1.create_window(150, 200, window=label1)
    elif int(x) < randomNumber:
        label1 = tk.Label(root, text='Too low', fg='green', font=('Comic Sans MS', 25, 'bold'), background='orange')
        canvas1.create_window(150, 200, window=label1)
    else:
        label1 = tk.Label(root, text=f'You Guessed It, the number was {randomNumber}',
                          fg='green', font=('Comic Sans MS', 12, 'bold'), background='orange')
        canvas1.create_window(150, 200, window=label1)


button1 = tk.Button(text='Make Guess', command=guess, bg='brown', fg='white')
canvas1.create_window(150, 100, window=number)
canvas1.create_window(150, 135, window=button1)

root.mainloop()
'''

import random
import string

chars = string.ascii_letters + string.digits + '!@#$%^&*()-+='
seed = ' '.join(random.choice(chars) for i in range(999))
random.seed(seed)
upLimit = int(input("Enter upper range limit for secret number: "))
secretNum = random.randrange(upLimit)
guess = int(input("Enter your guess: "))
numGuesses = 1
print(secretNum)
while guess != secretNum and numGuesses != 5:
    if guess > secretNum:
        print("Too High, make another guess")
    elif guess < secretNum:
        print("Too low, make another guess")
    guess = int(input("Enter your guess: "))
    numGuesses += 1
    if numGuesses == 5 and guess != secretNum:
        print(f"You ran out of guesses the number was {secretNum}")
        exit()
print(f"You guessed the number it was {secretNum}")
