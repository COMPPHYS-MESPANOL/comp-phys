'''This class is very similar to the turtle class we did in class. Methods sing and age are 
the only extra additions.'''
#HW04
#Matthew Espanol
#Partner: Matthew Del Rosario
import datetime as dt
import random

class whale:
    def __init__(self, name, sex):
        
        self.name = name
        self.sex = sex
        self.birth = dt.datetime.now()

        if self.sex == 'M':
            sex = "male"
        elif self.sex == 'F':
            sex = "female"
        print 'A {:s} whale named {:s} has been born!'.format(self.sex, name)
        
    def age(self):
        self.newage = dt.datetime.now() - self.birth
        return self.newage

    def sing(self):
        return 5*'\a'
    def __str__(self):
        return 'A whale named {:s} age {:s}'.format(self.name, self.age())
    



WHALES = ['Wailmer', 'Wailord', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']    
Names = []    

limit = 0
while limit < len(whales):
    sex = random.sample(['male', 'female'], 1)[0]
    Names.append(whale(WHALES[limit], sex))
    print WHALES[limit]
    limit += 1
        
    