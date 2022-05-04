powers =[int(i) for i in input().split()]
y_pow = int(input())

index = 0
yes = False
for i in powers:
    for j in powers[index+1:]:
        if i + j == y_pow:
            yes = True
    index += 1
if yes:
    print("Yes")
else:
    print("No")