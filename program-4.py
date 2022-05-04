"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. 
You are given an array of string sentences, where each sentences[i] represents a single sentence.
Return the maximum number of words that appear in a single sentence.
Input:
Input contains n+1 lines
First line the number of sentences in the list
Next n lines contains n sentences
Output:
Output is a number
Sample input 1 :
3
alice and bob love IARE
i think so too
it is a test
Sample output 1:
5
Sample input 2:
1
This is so test
Sample Output 2:
4

"""
lst=[]
for i in range(int(input())):
    sentence=[i for i in input().split()]
    lst.append(len(sentence))
print(max(lst))
