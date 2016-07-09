import sys
import os

#파이썬에는 switch 문이 없음, 대신 if..elif..else 문을 이용해야 함.

number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # New block ends here
elif guess < number:
    # Another block
    print('No, it is a little higher than that')
    # You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
    # you must have guessed > number to reach here

print('if End')
# This last statement is always executed,
# after the if statement is executed.