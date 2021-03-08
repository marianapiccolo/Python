#Create a class called Person() with the attributes: name, city, phone and email. Use at least 2 \ n ",
#special methods in its class. Create an object of your class and make a call to at least one of your methods \ n ",
# special \ n "

class Person():

    def __init__(self, name, city, phone, email):
        self.name = name
        self.city = city
        self.phone = phone
        self.email = email
        print("Object created")

    def __str__(self):
        return "User " + " " + self.name + " " + "lives in the city" + " " + self.city

P1 = Person("João", "São Paulo", 12345678, "joao@gmail.com")
print(str(P1)) 
