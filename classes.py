class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def speak_name(self):
        return self.get_name()

class OlderPerson(Person):

    def __init__(self, name, age, wrinkles):
        Person.__init__(self, name, age)
        self.wrinkles = wrinkles

    def get_name(self):
        return self.name
    
    def speak_name(self):
        return self.get_name()

    def get_wrinkles(self):
        return self.wrinkles

grandpa = OlderPerson("Jebediah", 89, 40)

print(grandpa.speak_name())

print(grandpa.get_wrinkles())