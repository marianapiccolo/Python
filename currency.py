#Create a module called coin.py with the built-in functions increase (), decrease (), double (), and half ().
#Make a program that imports this module and uses some of these functions.

def increase(price, tax):
    res = price + (price * tax/100)
    return res

def decrease(price, tax):
    res = price - (price * tax/100)
    return res

def double(price):
    res = price * 2
    return res

def half(price):
    res = price / 2
    return res

price = float(input("Enter the price: $"))
print(f'The half of {price} is {half(price)}')
print(f'The double of {price} is {double(price)}')
print(f'Increasing 10% we have {increase(price,10)}')
print(f'Decreasing 10% we have {decrease(price,10)}')

#developing
