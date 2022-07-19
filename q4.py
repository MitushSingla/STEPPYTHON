print("Armstrong Number checking:")
sum=0
num=1634
print(num)
order=len(str(num))
original_num=num
while(num>0):
    digit=num%10
    sum=sum+digit**order
    num=num//10
if sum==original_num:
    print("number is armstrong number")
else:
     print("number is not armstrong number")