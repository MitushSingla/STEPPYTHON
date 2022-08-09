mylst = []
 
 
num = int(input("Enter number of elements  : "))
 
 
for n in range(0, num):
 
 element = (input("Please enter a num:"))
 
 mylst.append(element) 
 
mytuple =tuple(mylst) 
 
print(mytuple) 