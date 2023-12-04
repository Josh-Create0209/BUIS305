number1= int(input('Enter Number 1: '))
if(number1%3==0 and number1%5==0):
    print('Tic tac')
elif(number1%3==0):
    print('Tic')
elif(number1%5==0):
    print('Tac')

# While Loop
numbers = int(input('Enter Numbers: '))
while(numbers>=0 and numbers<=20):
    if (numbers % 3 == 0 and numbers % 5 == 0):
        print('Tic tac')
        break
    elif (numbers % 3 == 0):
        print('Tic')
        break
    elif (numbers % 5 == 0):
        print('Tac')
        break
    elif (numbers > 20):
        print('Invalid input because numbers is greater than 20 ')
    elif (numbers < 0):
        print('Invalid input because numbers is less than 0')
    else:
        print(numbers)

# RandomGenerator
import random
random_number=random.randint(10, 20)
number_2 = 0
count = 0
while count < 5:
    number_2 = int(input('Enter Number:'))
    if number_2 > 0:
        print('Greater than 0')
        break
    else:
        count += 1
        if count < 5:
            print('Try again')
        else:
            print('Max Attempts')
            break
print('User Number',number_2,'Random Number',random_number)
if number_2 == random_number:
    print('Match')
else:
    print('Not Match')