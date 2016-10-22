##Alex Lim Siew Zhuan 15597746 RT-OS 301
##LAB-1
##Using Python 2.7.6
##Q5 -02
text = open('mess.txt','r')
strg = text.read()
size = len(strg)
i=0
while (i<size):
    if str.isalpha(strg[i]):
        print strg[i]
    i=i+1
