def outer():
 s="Ludhiana" 
def inner1():
 s="punjab"
def inner2():
 nonlocal s
s="chandigarh"
def inner3():
 global s
s="Haryana"
print(s) 
inner1() 
print(s) 
inner2()
print(s) 
inner3()
print(s) 
outer()
print(s)

#Output
"""
File "<string>", line 6
SyntaxError: no binding for nonlocal 's' found

"""
