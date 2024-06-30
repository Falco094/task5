class Animal:
    def __init__(self,name,age,species):
        self.name = name
        self.age = age
        self.species = species
    def make_sound (self):
        print("Maman is barking")
        
self = Animal("Maman", 30 , "Chi wawa")
print(f"name: {self.name}, age: {self.age}, species:{self.species}")

class butterfly(Animal) :
    
    def make_sound(self):
        print(f"{self.name}singing")
        
        
self = butterfly ("Blue Moropho" , 21 , "Meme")
print(f"name:{self.name}, age: {self.age},species:{self.species}")


class banda(Animal):
    def mane_size(self):
        print("Grand")
        
    def make_sound(self):
        print("Bleat")
        
self = banda ("Banda" , 25 , "Kong fu banda" )
print(f'name : {self.name}, age: {self.age}, species: {self.species}')



# couldnt do any more sry , i've forget how do i print the names of sounds ;.;
# and when i came to exercise 3 i saw that i already did it so i skipped .
# im i doing well ? i need ur feedback pls 
#Thankx
     