'''The function sortList takes the list 'data' and adds the elements in that list to new lists which are sorted by distance, apparent brightness, and absolute brightness. First 'counter' is intialized to 1,and the 'counter' is increased by 1 
after every running of the while loop. As the 'counter' is less than 3, the while loop looks at the different 
elements of the list. 1: sorts 'data' by distance into list dist_sort, and then that list is sorted into distance. A similar thing occurs for 
counter=2 and counter=3. The lists are reversed at the end so that the names appears before the sorting parameter'''


'''Name, Distance, Apparent Brightness, Absolute Brightness'''
data = [
('Alpha Centauri A',    4.3, 0.26,     1.56),
('Alpha Centauri B',    4.3, 0.077,    0.45),
('Alpha Centauri C',    4.2, 0.00001,  0.00006),
("Barnard's Star",      6.0, 0.00004,  0.0005),
('Wolf 359',            7.7, 0.000001, 0.00002),
('BD +36 degrees 2147', 8.2, 0.003,    0.006),
('Luyten 726-8 A',      8.4, 0.000003, 0.00006),
('Luyten 726-8 B',      8.4, 0.000002, 0.00004),
('Sirius A',            8.6, 1.00,     23.6),
('Sirius B',            8.6, 0.001,    0.003),
('Ross 154',            9.4, 0.0002,   0.0005),
]

from pprint import pprint

distance = []
dist_sort = []
apparent = []
app_sort = []
trueB = []
trueB_sort = []

def sortList(x):
    counter = 1
    while counter <= 3:
        if counter == 1:
            distance = [[x[a][counter], x[a][0]] for a in range(0, len(x))]
            dist_sort = sorted(distance)
        elif counter == 2:
            apparent = [[x[a][counter], x[a][0]] for a in range(0, len(x))]
            app_sort = sorted(apparent)
        elif counter == 3:
            trueB = [[x[a][counter], x[a][0]] for a in range(0, len(x))]
            trueB_sort = sorted(trueB)
        counter += 1
    
    dist_sort = [dist_sort[num][::-1] for num in range(0, len(x))]
    app_sort = [app_sort[num][::-1] for num in range(0, len(x))]
    trueB_sort = [trueB_sort[num][::-1] for num in range(0, len(x))]
    
    print "Ranked by Distance:";pprint(dist_sort)
    
    print "Ranked by Apparent Brightness:";pprint(app_sort)
    
    print "Ranked by Absolute Brightness:";pprint(trueB_sort)

  
sortList(data)