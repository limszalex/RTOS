##Alex Lim Siew Zhuan 15597746 RT-OS 301
##LAB-1
##Using Python 2.7.6
##Q5 -01
from string import maketrans 

string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc " \
    "dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq " \
    "rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu " \
    "ynnjw ml rfc spj."

word = list(string)
size = len(word)
i=0
while (i<size):
    if str.isalpha(word[i]):
        word[i] = chr(ord(word[i])+2) #shift forwards
        if str.isalpha(word[i])== 0: #if ascii key is no longer an alpha
            word[i] = chr(ord(word[i])-26) #shift backwards/rolback
    i=i+1
print ''.join(word)
