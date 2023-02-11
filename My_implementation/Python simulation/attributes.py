class Person:
    num_of_people = 0
    def __init__(self, name) -> None:
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people(cls):
        return cls.num_of_people
    @classmethod
    def add_person(cls):
        cls.num_of_people +=1

p1 =Person("Tim")
p2 = Person("Jerry")
print(Person.number_of_people())