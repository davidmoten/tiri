#!/usr/bin/python
from random import randint
count = 0
while (count < 5):
    x = randint(1,100)
    y = randint(1,100)
    ans = input('What is ' + str(x) + ' + ' + str(y) + '? ')
    z = int(ans)
    if x + y == z:
        print('Correct!')
    else: 
        print('Nope! The answer is ' + str(x+y))
