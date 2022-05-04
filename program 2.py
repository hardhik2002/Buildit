"""
You’re given strings jewels representing the types of stones that are jewels, and stones you have. 
Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so “a” is considered a different type of stone from “A”.
Input:
Input of two lines
First line is a string
Second line is also a string
Output:
Output single line – displays a number
Sample input 1:
a
abc
Sample Output 1:
1
Sample input 2:
aA
aAAbbbb
Sample output 2:
3

"""
str1=input()
str2=input()
count=0
for i in str1:
    if i in str2:
        count+=1
print(count)
