o_lst=[]
for i in range(int(input())):
    o_lst.append(int(input()))
n=int(input())
o_lst.remove(n)
for i in o_lst:
    print(i)