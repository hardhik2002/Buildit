lst=[]
for i in range(int(input())):
    sentence=[i for i in input().split()]
    lst.append(len(sentence))
print(max(lst))
