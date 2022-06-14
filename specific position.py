"""
Program to insert an element in given array at specified position
without loosing any element and display resultant array.
"""
o_lst=[]
for i in range(int(input())):
    o_lst.append(int(input()))
n=int(input())
n2=int(input())
o_lst.insert(n,n2)
for i in o_lst:
    print(i)
