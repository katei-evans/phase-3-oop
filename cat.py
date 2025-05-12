# instance methods have self keyword. Inorder to access instance methods, we need to create an instance of the class.
class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print("meow")

cat_1 = Cat("Fluffy")
cat_1.meow()
cat_2 = Cat("nola")
cat_2.meow()