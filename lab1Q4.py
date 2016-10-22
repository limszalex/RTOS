##Alex Lim Siew Zhuan 15597746 RT-OS 301
##LAB-1
##Using Python 2.7.6
##Q4
print '\n================================ Question 4 ================================'
import random

def dice():
    n = [1,2,3,4,5,6]
    roll = random.choice(n)
    return roll

def snake(x):
    sh = [14,20,39,66,69,79,84,88]
    st =  [3,15,33,53,58,67,71,36]
    i=0
    while(i < 8):
        if x == sh[i]:
            x = st[i]
        i=i+1
    return x

def ladder(y):
    ls =  [6,24,30,49,82]
    le = [17,26,44,62,86]
    i=0
    while(i < 5):
        if y == ls[i]:
            y = le[i]
        i=i+1
    return y

pb_1 = 1 #initial p1
pb_2 = 1 #initial p2

##
while ((pb_1 <90) or (pb_2 <90)):
    ####Player 1####
    print 'Player 1 hit enter to roll'
    raw_input() #get enter
    p1roll = dice()
    pb_1=pb_1+p1roll

    if pb_1 >90:
        pb_1 =90
    
    print 'You rolled: ' + str(p1roll)
    print 'You are at spot: ' + str(pb_1)

    pb_1s = snake(pb_1)
    pb_1la= ladder(pb_1)
    
    if pb_1 != pb_1s:
        print 'You slide down from the snake, now at spot: ' + str(pb_1s)
        pb_1 = pb_1s

    elif pb_1 != pb_1la:
        print 'You climbed the ladder, now at spot: ' + str(pb_1la)
        pb_1 = pb_1la
    
    if pb_1 >=90:
        break
    
    ################
    print '\n'
    print '\n'
    ################
    
    ####Player 2####
    print 'Player 2 hit enter to roll'
    raw_input() #get enter
    p2roll = dice()
    pb_2=pb_2+p2roll

    if pb_2 >90:
        pb_2 =90
    
    print 'You rolled: ' + str(p2roll)
    print 'You are at spot: ' + str(pb_2)

    pb_2s = snake(pb_2)
    pb_2la = ladder(pb_2)
    
    if pb_2 != pb_2s:
        print 'You slide down from the snake, now at spot: ' + str(pb_2s)
        pb_2 = pb_2s
        
    elif pb_2 != pb_2la:
        print 'You climbed the ladder, now at spot: ' + str(pb_2la)
        pb_2 = pb_2la

    if pb_2 >=90:
        break
    
    ################
    print '\n'
    print '\n'
    ################
    
if pb_1>=90:
    print 'Player 1 Win'
else:
    print 'Player 2 win'
