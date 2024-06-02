n = int(input())
""" Pattern Problem 1: Based on input print following pattern
example if n=5
output should be:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

 """
print("###Problem 1- Solution###")
k = 1
for i in range(1,n+1,1):
    for j in range(i):
        print(k , end=" ")
        k +=1
    print()

""" Pattern Problem 2: Based on input print following pattern
example if n=5
output should be:
A
AB
ABC
ABCD
ABCDE

Pattern Problem 3: Based on input print following pattern
example if n=5
output should be:
ABCDE
ABCD
ABC
AB
A
 """
def numToChar(num):
    return chr(num+65)
print("###Problem 2- Solution###")
for i in range(n):
    for j in range(i+1):
        print(numToChar(j),end="")
    print()

print("###Problem 3- Solution###")
for i in range(n,0,-1):
    for j in range(i):
        print(numToChar(j),end="")
    print()

"""
Pattern Problem 4: Based on input print following pattern
example if n=5
output should be:
A
BB
CCC
DDDD
EEEEE

"""
print("###Problem 4- Solution###")
for i in range(n):
    print(numToChar(i)*(i+1),end="")
    print()

"""
Pattern Problem 5: Based on input print following pattern
example if n=5
output should be:
   A
  ABA
 ABCBA
ABCDCBA
"""
print("Problem 5-Solution")
for i in range(n-1):
    for _ in range(n-i-2):
        print(" ",end="")
    #Left side of Pyramid
    for j in range(i):
        print(numToChar(j),end="")
    #Right side of Pyramid
    for j in range(i,-1,-1):
        print(numToChar(j),end="")
    print()

"""
Pattern Problem 6: Based on input print following pattern
example if n=5
output should be:
E
D E
C D E
B C D E
A B C D E
"""

print("Problem 6 - Solution")

for i in range (n):
    for j in range (i,-1,-1):
        print(numToChar(n-j-1), end= " ")
        
    print()