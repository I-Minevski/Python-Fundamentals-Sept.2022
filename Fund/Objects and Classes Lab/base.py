from build.lib.colorama.initialise import init

class Person:
    
    
    def __init__(self, first_name, last_name, age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    
    def say_hi(self):
        return f"Hello {self.first_name} {self.last_name}"
    
ivan = Person("Ivan", "Ivanov", 20)
print(ivan.say_hi())
print(ivan.age)