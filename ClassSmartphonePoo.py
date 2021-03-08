#Create the Smartphone class with 2 attributes, size and interface and create the MP3Player class with capacity attributes.
#The MP3player class must inherit the attributes of the Smartphone class."

class Smartphone:

    def __init__(self, size, interface):
        self.size = size
        self.interface = interface

class MP3Player(Smartphone):
        
    def __init__(self, capacity, size = "Small", interface = "Led"):
        self.capacity = capacity
        Smartphone.__init__(self, size, interface)

    def print_mp3player(self):
        print("Values ​​for the created object: %s %s %s" %(self.size, self.interface, self.capacity))

device1 = MP3Player("64 GB")
device1.print_mp3player()
