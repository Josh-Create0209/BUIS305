#Collect three inputs from user; Store in a varibale and complete addition and subtraction

number1=input('enter number 1')
number2=input('enter number 2')
number3=input('enter number 3')

print(number1, number2)

sum=(number1+number2)
print(sum)

sum=int(number1)+int(number2)
print(sum)

difference=int(number1)-int(number2)
multiplication=int(number1)*int(number2)
division=int(number1)/int(number2)
print(difference, multiplication, division)

sum=int(number1)+int(number2)+int(number3)
difference=int(number1)-int(number2)-int(number3)
multiplication=int(number1)*int(number2)*int(number3)
division=(int(number1)/int(number2))/int(number3)
print(difference, multiplication, division)

import math
print(math.pow(9,3))
print(math.sqrt(196))
print(math.trunc(5.678910111213))
print(math.log10(67))
sequence=(int(number1),int(number2),int(number3))
print(math.prod(sequence))
print(math.gamma(55))
print(math.hypot(56738))
print(math.log(3))
print(math.gcd(90,77))
print(math.ceil(44))
print(math.degrees(32))