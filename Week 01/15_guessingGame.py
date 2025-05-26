import random
num = random.randint(1,10)
guess = 0
while guess!=num:
    guess = int(input('Guess the number (1-10)" '))

print("correct!")