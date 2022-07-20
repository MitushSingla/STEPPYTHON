n1=int(input("please enter your first number:"))
n2 = int(input("please enter your second number:"))
optr=(input("please enter which operator you like:"))
if optr=='+':
    sum=n1+n2
    print("your sum is:",sum)
elif optr=='-':
    sub=n1-n2
    print("your subtraction is:",sub)
elif optr=='*':
    multiply=n1*n2
    print("your multiply is:",multiply)