o_lst=[]
eve_lst=[]
odd_lst=[]
for i in range(int(input())):
    n=int(input())
    o_lst.append(n)
for i in o_lst:
    if i%2==0:
        eve_lst.append(i)
    else:
        odd_lst.append(i)
for i in eve_lst:
    print(i)
for i in odd_lst:
    print(i)

