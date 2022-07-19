print("Factorial Program")
def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)
f=factorial_recursive(3)
print(f)