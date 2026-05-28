# check if the number is armstrong or not
n=153
num=n
result=0
for i in range(len(str(num))):
    ld=num%10
    result=result+ld**3
    num=num//10
    print(result)
if result==n:
    print("armstrong")
else:
    print("not armstrong")

n=153
num=n
total=0
nod=len(str(num))
while num>0:
    ld=num%10
    total=total+(ld**nod)
    num=num//10
if total==n:
    print("armstrong")
else:
    print("not armstrong")