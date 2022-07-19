print("Fibonacci Series:")
def Fibonacci(n):
    if n<0:
        print("incoreect value")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return Fibonacci(n-1)+ Fibonacci(n-2)
print("Fibonacci series of 9 is",Fibonacci(9))