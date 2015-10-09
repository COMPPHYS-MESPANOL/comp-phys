#Matthew Espanol
#Matthew Del Rosario
#Project part 1
#October 8 2015
import random
import numpy 


class Dolphins:
    def __init__(self, name, mother, father, sex, age = 0):
        self.name = name
        self.mother = mother
        self.father = father
        self.sex = sex
        self.age = age
    
    def dolph_age(self):   #increases time by 1 year
        self.age += 1
        return self.age
    
    def procreate(self, dolphs):  #dolphs will be a dictionary 
        dad = False
        mom = False
        random_sex = random.sample(['male', 'female'], 1)[0]
        new_male = ''
        new_female = ''
        while dad == False or mom == False:
            if random.sample(dolphs, 1)[0].sex == 'male':
                new_male = random.sample(dolphs, 1)[0]
                dad = True
            if random.sample(dolphs, 1)[0].sex == 'female':
                new_female = random.sample(dolphs, 1)[0]
                mom = True
        while procreation == True:   #checks age, mother, father, age of partner which are the conditions for procreation
            if self.age < 8\
            or new_male.mother == new_female.mother\
            or new_male.father == new_female.father\
            or numpy.absolute(new_male.age - new_female.age) > 10:
                 procreation = False
            else:
                List_name.Dolphins(List_name, dolphs, dolphs, random_sex)   #if none of these set procreation to false, procreation instantiates new dolphin
    
