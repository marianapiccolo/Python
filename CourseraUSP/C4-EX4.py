#Program that reads a positive integer n and prints the n Fibonacci number 

n = int(input("Enter a number: "))

previous = 0
current = 1
i = 1

while i<n:
    next = previous + current
    previous = current
    current = next
    i = i + 1
print("F(%d) = %d" %(n, current))