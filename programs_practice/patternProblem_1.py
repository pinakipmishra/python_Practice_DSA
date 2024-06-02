n = int(input())
""" 
Pattern Problem 1: Based on input print following pattern
example if n=5
output should be:
        *
       ***
      *****
     *******
    *********
"""
print("-------Patter Problem 1 - Solution-------")
for i in range (n):
    print(" "*(n-1-i)+"*" * ((i*2 + 1) *1), end="")
    print()
# Can be solved in single loop without using multiple loop
""" 
Pattern Problem 2: Based on input print following pattern
example if n=5
output should be:     
    *********
     *******
      *****
       ***
        *
"""
print("-------Patter Problem 2 - Solution-------")
for i in range (n,0,-1):
    print(" "*(n-i)+"*" * (((i-1)*2 + 1) *1), end="")
    print()
# Can be solved in single loop without using multiple loop
""" 
Pattern Problem 3: Based on input print following pattern
example if n=5
output should be:
        *
       ***
      *****
     *******
    *********
    *********
     *******
      *****
       ***
        *
"""
print("-------Patter Problem 3 - Solution-------")
for i in range (n):
    print(" "*(n-1-i)+"*" * ((i*2 + 1) *1), end="")
    print()
for i in range (n,0,-1):
    print(" "*(n-i)+"*" * (((i-1)*2 + 1) *1), end="")
    print()
# Here I am not using nested loop but my time complexity will be O(n)+O(n). Is my understanding correct

""" Pattern Problem 4: Based on input print following pattern
example if n=5
output should be:
*
**
***
****
*****
****
***
**
*

 """
print("-------Patter Problem 4 - Solution-------")
for i in range(1,n+1,1):
    print("*" * i,end="")
    print()
for i in range(n-1,0,-1):
    print("*"*i,end="")
    print()
# Here I am not using nested loop but my time complexity will be O(n)+O(n). Is my understanding correct
""" Pattern Problem 5: Based on input print following pattern
example if n=5
output should be:
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""
print("-------Patter Problem 5 - Solution-------")
for i in range(n):
    for j in range(i+1):
        print((i+j+1)%2, end="")
    print()

"""
Pattern Problem 5: Based on input print following pattern
example if n=5
output should be:
1      1       
12    21
123  321 
12344321
"""
print("-------Patter Problem 6 - Solution-------")
for i in range(n-1):
    for j in range(i+1):
        print(j+1,end="")
    for j in range ((n-i-2)*2):
        print(" ", end="")
    for j in range(i+1,0,-1):
        print(j,end="")
    print()
    