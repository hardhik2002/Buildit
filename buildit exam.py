"""
A wrestling bout is a physical competition, between two teams namely X-team and Y-person, 
who attempt to gain and maintain a superior position. The team contains n persons with various powers p1,p2,p3,p4…..pn. 
The X-team is going to win only if you find a combination of two people’s power in x team is equal to Y person power. 
The team is busy with practice, please help them to find whether the team-x is won or not. If won then print “YES” otherwise print “NO”
INPUT:
First line contain x-team input values.
Second line contain Y-team player input value.
OUTPUT:
If X-team won then print “YES” otherwise print “NO”
Sample input 1:
23 45 67 89 12
57
Sample output 1:
YES
Sample input 2:
23 45 67 89 12
56
Sample output 2:
NO

"""

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
