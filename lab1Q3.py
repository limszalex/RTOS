##Alex Lim Siew Zhuan 15597746 RT-OS 301
##LAB-1
##Using Python 2.7.6
##Q3
import math

pi = 3.1415926535897932384626433
twopi = float(2*pi)
halfpi = float(pi/2)

def cos_32s(x):
    c1 = 0.99940307
    c2 = -0.49558072
    c3 = 0.03679168
    x2 = x*x
    return (c1+x2*(c2+c3*x2))


def cos_32(x):
    x = math.fmod(x,twopi)
    if x<0:
            x = x*-1
    quad = int(x/halfpi)
    if quad == 0:
        return cos_32s(x)
    if quad == 1:
        return -cos_32s(pi-x)
    if quad == 2:
        return -cos_32s(x-pi)
    if quad == 3:
        return cos_32s(twopi-x)
i=0
line_ti ='{:>8}{:>18}{:>17}{:>13}'.format("cos(x)", "Algorithm Value", "Python Value", "Error")
print line_ti
while (i<=360):
    ans = cos_32(float(i))
    ans2 = math.cos(float(i))
    ans3 = ans2-ans
    if ans3<0:
        ans3=ans3*-1
    line_new = '{:>8}{:>18.12f}{:>18.12f}{:>18.12f}'.format("cos("+str(i)+")", ans, ans2, ans3)
    print line_new
    i=i+5
