##Alex Lim Siew Zhuan 15597746 RT-OS 301
##LAB-1
##Using Python 2.7.6
##Q5 -04
import urllib, re
loop = 1
time = 0
start = 1
while loop:
    if start == 1:
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" #the url link with unknown numebr at behind
        const = "and the next nothing is (\d+)" #the const string shown in webpage \d+ more than 1 int [any interger]
        print "first number 12345"
        rannumber = raw_input("input number: ")
        start = 0
    
    while start == 0:
        get = urllib.urlopen(url % rannumber).read()
        if re.search(const,get):
            rannumber = re.search(const,get).group(1) #search the const in get and get the interger group
            print get
        else:
            if time == 0:
                print get
                new = int(rannumber)/2
                print "After division: " + str(new)
                rannumber = int(new)
                time = 1
            else:
                print get
                loop = 0
                start = 2
