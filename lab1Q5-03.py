##Alex Lim Siew Zhuan 15597746 RT-OS 301
##LAB-1
##Using Python 2.7.6
##Q5 -03
import re
text = open('mess2.txt','r')
strg = text.read()
print "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", strg)) #3 captital 1 small letter 3 capitial pattern
