# class ClassName1():
#     ...
#     properties via __init__ method(self,prop1, prop2)
#         .. = prop1
#         .. = prop2
#     method definition()

# ClassName1(prop1,prop2)
"""
class Dog():
    def __init__(self,name,age):
                    , 'Miles',4
                    , 'Buddy',9
        self.name = name
        miles.name = 'Miles'
        buddy.name = 'Buddy'
        self.age = age
        miles.age = 4
        buddy.age = 9

#object/instance
# miles -> class Dog - 'Miles' - 4
miles = Dog('Miles',4) <===self
buddy = Dog('Buddy',9)
"""

class Dog():
    species = 'Canis familiaris'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # def __init__(self,inputed_name,inputed_age):
    #     self.name = inputed_name
    #     self.age = inputed_age

    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self,sound):
        return f"{self.name} says {sound}"
        """
        return self.name + " speak " + sound
        return "{} says {}".format(self.name,sound)
        return "{o_name} says {o_sound}".format(o.sound = sound, o.name = self.name)
        """

# instantiate an object
miles = Dog('Miles',4)
print(miles.name)
print(miles.age)
print(miles.species)
print(miles.description())
print(miles.speak('bark'))
print(f"Dog name: {miles.name}")
print("Dog name: {}".format(miles.name))
print("Dog name: {o_name}".format(o_name=miles.name))

buddy = Dog('Buddy',9)
print(buddy.name)
print(buddy.age)
print(buddy.species)
print(buddy.description())

print(dir(Dog))

class Mom():
    def __init__(self,name,hair_color):
        self.name = name
        self.hair_color = hair_color

# Child
class Children(Mom):
    def __init__(self,name,new_hair_color):
        self.name = name
        self.hair_color = new_hair_color
    
    # def change_hair_color()

mom = Mom('ani','cokelat')
print(f"{mom.name}'s hair color is {mom.hair_color}")
first_daughter = Children('ita','ungu')
print(f"{first_daughter.name}'s hair color is {first_daughter.hair_color}")

class Mom():
    def __init__(self,name,hair_color):
        self.name = name
        self.hair_color = hair_color
    
    def get_hair_color(self):
        return self.hair_color
    
    def change_hair_color(self,new_hair_color):
        self.hair_color = new_hair_color

# Child
class Children(Mom):
    def __init__(self,name,hair_color,age):
        super().__init__(name,hair_color)
        self.age = age
    # def __init__(self):
    #     super().__init__(self,name)
    
    # def change_hair_color(self,new_hair_color):
    #     self.hair_color = new_hair_color

mom = Mom('ani','cokelat')
print(f"{mom.name}'s hair color is {mom.hair_color}")
first_daughter = Children('ita','ungu',56)
print(f"{first_daughter.name}'s hair color is {first_daughter.hair_color}")



