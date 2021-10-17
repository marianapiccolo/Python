# Exercise 1
#Write a program that receives a natural number n on input and prints n! (factorial) in the output.

#1
""" n = int(input("Enter a number: "))

cont = 1
fat = 1

while cont <= n:
    fat = fat * cont 
    cont = cont + 1

print("%d! = %d" %(n, fat)) 
 """

#2 with for
n = int(input("Enter a number: "))
fat = 1 

for i in range(2, n+1):
    fat = fat * i

print("%d! = %d" %(n, fat))

