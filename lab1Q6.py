##Alex Lim Siew Zhuan 15597746 RT-OS 301
##LAB-1
##Using Python 2.7.6
##Q6
print '\n================================ Question 6 ================================'
import random

class game:
    square = 1 #player block
        
    def dice(self):
        n = [1,2,3,4,5,6]
        roll = random.choice(n)
        return roll

    def snake(self,x):
        sh = [14,20,39,66,69,79,84,88]
        st =  [3,15,33,53,58,67,71,36]
        i=0
        while(i < 8):
            if x == sh[i]:
                x = st[i]
            i=i+1
        return x

    def ladder(self,y):
        ls =  [6,24,30,49,82]
        le = [17,26,44,62,86]
        i=0
        while(i < 5):
            if y == ls[i]:
                y = le[i]
            i=i+1
        return y
    def update(self):
        
        if self.square != game.snake(self,self.square):
            print 'You slide down from snake, now at spot: ' + str(game.snake(self,self.square))
            self.square = game.snake(self,self.square)
            
        elif self.square != game.ladder(self,self.square):
            print 'You climbed the ladder, now at spot: ' + str(game.ladder(self,self.square))
            self.square = game.ladder(self,self.square)
        

p1 = game()
p2 = game()

##
while ((p1.square <90) or (p2.square <90)):
    ####Player 1####
    print 'Player 1 hit enter to roll'
    raw_input() #get enter
    p1roll = game.dice(p1)
    p1.square = p1.square + p1roll

    if p1.square >90:
        p1.square =90
    
    print 'You rolled: ' + str(p1roll)
    print 'You are at spot: ' + str(p1.square)

    game.update(p1)
    
    if p1.square >=90:
        break
    
    ################
    print '\n'
    print '\n'
    ################
    
    ####Player 2####
    print 'Player 2 hit enter to roll'
    raw_input() #get enter
    p2roll = game.dice(p2)
    p2.square = p2.square +p2roll

    if p2.square >90:
        p2.square =90
    
    print 'You rolled: ' + str(p2roll)
    print 'You are at spot: ' + str(p2.square)

    game.update(p2)
    
    if p2.square >=90:
        break
    
    ################
    print '\n'
    print '\n'
    ################
    
if p1.square >=90:
    print 'Player 1 Win'
else:
    print 'Player 2 win'
