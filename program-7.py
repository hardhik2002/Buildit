"""
In a forest n trees are there in one sequence with various heights and tree heights are between 1 to 9.
Your task is to cut all n tree is in same height and that is maximum possible height.
The input is n digit number represent n tree heights.
For example: 3424
1 Tree :3
2 Tree :4
3 Tree :2
4 Tree: 4
The answer is 2 because, if you cut all trees at height 2 then the remaining part of
the tree from ground is same for all trees.
Input:
Given input as a number
Output:
It returns smallest tree.
Sample input 1:
342342
Sample output 1:
2
Sample input 2:
879797
Sample output 2:
7

"""
num=int(input())
min=9
while num>0:
    digit=num%10
    if min>digit:
        min=digit
    num=num//10
print(min)
