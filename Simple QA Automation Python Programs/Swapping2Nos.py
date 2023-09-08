# Swap 2 Numbers

#Approach-1

number1=10
number2=100

temp=number1 # Create an empty variable "temp", where u can store the value of number1 variable.
number1=number2
number2=temp

print(f'the value of number1 after swapping is :  {number1}')  #100
print(f'the value of number1 after swapping is :  {number2}') #10 


#Approach-2

number1,number2=number2,number1
print(f'2nd the value of number1 after swapping is :  {number1}')  
print(f'the value of number1 after swapping is :  {number2}')



