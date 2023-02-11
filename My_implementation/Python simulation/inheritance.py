class Pet:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet):
    def __init__(self, name, age, color) -> None:
        super().__init__(name, age)
        self.color = color
    def show(self):
        print(f"I am {self.name}, I am {self.age } years old and I am {self.color}")

    def speak(self):
        print("Meow")
class Dog(Pet):
    def speak(self):
        print("Wof")

p = Pet("Berger", 7)
p.show()
c = Cat("Jerry", 8, "blue")
c.show()
d = Dog("Tom", 5)
d.speak()
