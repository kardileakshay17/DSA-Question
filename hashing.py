#  hashing  a python  number list and then  find the frequency of the number in the list    

# n=[5,3,2,2,1,5,5,7,5,10]
# m=[10,111,1,9,5,6,7,2]

# hash_list=[0,1,2,1,0,4,0,1,0,0,1]
'''
for nums in n:
    hash_list[nums]+1

for nums in m:
    if nums<1 or nums>10:
        print(0)
    else:
        print(hash_list[nums])



freq_dict={}
for  nums in range(0,len(n)):
    freq_dict[n[nums]]=freq_dict.get(n[nums],0)+1
print(freq_dict)

for nums in m:
    if nums in freq_dict:
        print(freq_dict[nums])
    else:
        print(0)

'''        
#  hashing a python character list and then  find the frequency of the character in the list

# A="abdcdAsbdeCWEQQQQQQ3RWDWER"
# B=["a","b","c","d",'A','C','Q','R','W',]
# hash_list=[2,2,3,1,0,0,1,0,1]

# freq_dict={}
# for i in range(0,len(A)):
#     freq_dict[A[i]]=freq_dict.get(A[i],0)+1
# print(freq_dict)
 
# for i in B:
#     if i in freq_dict:
#         print(freq_dict[i])
#     else:
#         print(0)

A="azyxyyzaa"
B=['a','b','y','x']
hash_list=[0] * 26
for ch in A:
    Ascii_val=ord(ch)
    index=Ascii_val-97
    hash_list[index]+=1
    print(hash_list)
     
for ch in B:
    Ascii_val=ord(ch)
    index=Ascii_val-97
    print(hash_list[index])
