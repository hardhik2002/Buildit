# program-3 in buildit lab external
"""
Given two binary strings a and b, return their sum as a binary string.
Input:
Input contains two lines 
First binary number
Secondary binary number
Output:
Output contains one line
Sum of binary numbers
Sample input 1:
10
1
Sample Output 1:
11
Sample input 2:
101
10
Sample output 2:
111
Sample input 3:
1010
1011
Sample output 3:
10101

"""
b1=input()
b2=input()
b1,b2=int(b1),int(b2)
r=b1+b2
print(str(r))
