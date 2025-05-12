class Pet:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print ("The pet is speaking")

class Dog(Pet):
    def __init__(self, name ,color):
        super().__init__(name)
        self.color = color

    def speak(self):
        super().speak()
        print ("dog is speaking")

class Cat(Pet):
    pass


dog1 = Dog("Bosko", "white")
# dog1.speak()
print(dog1.color)
print