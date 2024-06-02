n = int(input())

""" 
Problem 1:
Based on input print following pattern
example if n=5
output should be:
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
"""
print("Problem 1 Solution")
for i in range(2*n):
    if i < n:
        for _ in range(n-i):
            print("*",end="")
        # Add Space
        for _ in range(i*2):
            print(" ",end="")
        for _ in range(n-i):
            print("*",end="")
    else:
        for _ in range(i-n+1):
            print("*", end="")
        for _ in range((2*n-i-1)*2):
            print(" ",end="")
        for _ in range(i-n+1):
            print("*", end="")
    print()

""" 
Problem 2:
Based on input print following pattern
example if n=5
output should be:
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

"""
print("Problem 2 solution")
for i in range(2*n-1):
    if i < n:
        for _ in range(i+1):
            print("*", end="")
        for _ in range((n-i-1)*2):
            print(" ", end="")
        for _ in range(i+1):
            print("*", end="")
    else:
        for _ in range(2*n-i-1):
            print("*",end="")
        for _ in range((i-n+1)*2):
            print(" ",end="")
        for _ in range(2*n-i-1):
            print("*",end="")
        
        
    print()

""" 
Problem 3:
Based on input print following pattern
example if n=5
output should be:
****
*  *
*  *
****

"""
print("Problem 3 Solution")
for i in range(n-1):
    if (i == 0) or (i == n-1-1):
        print("*" * (n-1), end="")
    else:
        print("*", end="")
        print(" "*(n-3), end="")
        print("*", end="")
    print()

""" 
Problem 4:
Based on input print following pattern
example if n=5
output should be:
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4

"""
print("### Problem 4 - Solution ###")
m =4
for i in range(2*m -2):
    for j in range(2*m-1):
        row = min(i,2*m-2-i)
        col = min(j,2*m-2-j)
        ans = min(row,col)
        print(m-ans,end=" ")
    print()

