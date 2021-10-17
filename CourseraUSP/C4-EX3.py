#Write a program that receives an integer on input, calculate and print the sum of the digits of this number on output

n = int(input("Enter a number: "))
i = 1
sum = 0
r = 0 

while n > 0:
    r = n%10
    n = n//10
    sum = sum + r
print("Sum = %d " %(sum))
