# check if a number is palindrome or not
n=1223345
num=n
result=0
for i in range(len(str(num))):
    ld=num%10
    result=result*10+ld
    num=num//10
    print(result)
if result==n:
    print("palindrome")
else:
    print("not palindrome")