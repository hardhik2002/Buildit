"""
Program to find given value is single digit or not. If single digit print Yes or No

Sample Input 1:
99

Sample Output 1:
No
"""
n=input()
print(len(n))
if len(n)>1:
    print("No")
else:
    print("Yes")