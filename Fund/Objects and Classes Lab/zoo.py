class Zoo:
    
    
    def __init__(self, zoo_name):
        self.zoo_name=zoo_name
        self.mammals=[]
        self.fish=[]
        self.birds=[]    
    
    __animals=0
    
    def add_animal(self, species, name):
        if species=="mammal":
            self.mammals.append(name)
        if species=="bird":
            self.birds.append(name)
        if species=="fish":
            self.fish.append(name)
        Zoo.__animals+=1
            
    def get_info(self, species):
        result=""
        if species=="mammal":
            result+=f"Mammals in {self.zoo_name}: {', '.join(x for x in self.mammals)}\n"
        if species=="bird":
            result+=f"Birds in {self.zoo_name}: {', '.join(x for x in self.birds)}\n"
        if species=="fish":
             result+=f"Fishes in {self.zoo_name}: {', '.join(x for x in self.fish)}\n"
        result+=f"Total animals: {Zoo.__animals}"
        return result
    
    
z_name=input()
zoo=Zoo(z_name)
count=int(input())
for i in range(count):
    animal_info=input().split(" ")
    zoo.add_animal(animal_info[0], animal_info[1])
a_type=input()
print(zoo.get_info(a_type))