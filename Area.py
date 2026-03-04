import math
n=int(input("enter the sides of the triangle:"))
if n == 2:
   b = int(input("enter the breadth"))
   h = int(input("enter the height"))
   area = (b * h)/ 2
   if(b>0 and h>0):
     print(area)
   else:
     print"invalid value"
elif n == 3:
   a = int(input("enter the a value"))
   b = int(input("enter the b value"))
   c = int(input("enter the c value"))
   s = (a + b + c) / 2
   if(a>0 and b>0 and c>0):
       x = s * (s - a) * ( s - b ) * ( s - c )
       y = math.sqrt(x)
       print(y)
   else:
       print"invalid value"
else:
   print"invalid choice"
