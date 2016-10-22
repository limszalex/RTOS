##Alex Lim Siew Zhuan 15597746 RT-OS 301
##LAB-1
##Using Python 2.7.6
##Q1
print '\n================================ Question 1a ================================'
print 'Alex'

print '\n================================ Question 1b ================================'
myname = raw_input("Full Name: ")
print 'Hello, '+myname
print '\n================================ Question 1c ================================'
myage = raw_input("Your Age?: ")
eyr = int(myage)+8
print 'Your Age, 8 years later will be: ['+str(eyr)+']'

##Q2
print '\n================================ Question 2 ================================'
text = open('script0702ainput.txt','r')

string = text.read()
word = string.split()
size = len(word)

i=0
large = len(word[i])

while (i<size):
    if large <= len(word[i]):
        large = len(word[i])
        theword = word[i]
        num = len(theword)
        print str(theword)+'['+str(num)+']'
    i=i+1
