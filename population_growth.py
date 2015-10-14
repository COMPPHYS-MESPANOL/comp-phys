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


#Matthew Espanol
#Matthew Del Rosario
#October 13 2015
import urllib
import re
from pprint import pprint as p

counter = 1
guys_names = []
lady_names = []
while counter < 5:
    first_url = 'http://www.prokerala.com/kids/baby-names/boy/page-'+str(counter)+'.html'
    second_url = 'http://www.prokerala.com/kids/baby-names/girl/page-'+str(counter)+'.html'
    file1 = urllib.urlopen(first_url)      
    lines1 = file1.readlines()
    file1.close()    
    file2 = urllib.urlopen(second_url)      
    lines2 = file2.readlines()
    file2.close()

    for line1 in lines1:
        m1 = re.search("(nameDetails\">)([A-Z].*[a-z])<", line1)
        if m1:
            guys_names.append(m1.group(2))
            
    for line2 in lines2:
        m2 = re.search("(nameDetails\">)([A-Z].*[a-z])<", line2)
        if m2:
            lady_names.append(m2.group(2))
    counter += 1
p(guys_names)
p(lady_names)    
