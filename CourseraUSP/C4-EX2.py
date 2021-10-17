#Exercise 2 
#Enter a positive integer as input and print the first n natural odd numbers. 

n = int(input("Enter a number: "))

cont = 1
impar = 1

while cont<=n:
    print(impar)
    cont = cont + 1
    impar = impar + 2