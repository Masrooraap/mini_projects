import random
num = random.randint(1,10)
i = 0
while i<5:
    i=i+1
    guess = int(input('guess the number:'))
    if(i==5):
        print('you lost :( ')
    elif(guess<num):
        print(f'{guess} is lesser')
    elif(guess>num):
        print(f'{guess} is greater')
    elif(guess==num):
        print('you win :)')
        break