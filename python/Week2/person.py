
# class Nperson(): #define the class, class always start in upper case
#     def __init__(self):
#         self.name = None #defining attributes
#         self.age = None
#         self.profession = None
#         self.height = None

# new_person = Nperson #creating new variable from the class
# new_person.name = "Liam" #assigning values to said attributes
# new_person.age = 25

class Person():
    def __init__(self,name,age,height): #sets so every object made from class has to have these attributes
        self.name = name
        self.age = age
        self.height = height
    def set_hair(self, person_hair):
        self.hair = person_hair
    def get_hair(self):
        print(self.hair)

person_x = Person("Liam",25,182) #setting the values for the necessary attributes


# print(person_x.name)
# print(person_x.age)
# print(person_x.height)



