print("To calculate area :")
print("I.To calculate area of triangle:")
print("(a)With three sides")
#formula = (s*(s-a)(s-b)(s-c))**0.5 where s = (a+b+c)/2
a=float(5)
b=float(6)
c=float(9)
s = (a+b+c) / 2
area= (s*(s-a)(s-b)(s-c))**0.5
print('The area of traingle is' '%0.2f' %area)
print()
print("(b)With two sides")
a=float(15)
b=float(10)
area= a*b*1/2
print(area)
print()
print("II.To calculate area of rectangle:")
a=float(15.2)
b=float(0.5)
area=a*b
print(area)
print()
print("III.To calculate area of sqaure:")
a=float(20)
area=a**2
print(area)