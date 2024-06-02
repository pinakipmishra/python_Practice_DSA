""" Pattern Problem1: Based on input print following pattern
example if n=5
output should be:
*****
*****
*****
*****
*****

 """
n = int(input())
print("-------Patter Problem1 - Solution-------")
for i in range (n):
    print("*"*n,end="")
    print()
# Can the Time Complexity O(n), since I am not using multiple loop

""" Pattern Problem 2: Based on input print following pattern
example if n=5
output should be:
*
**
***
****
*****

 """
print("-------Patter Problem2 - Solution-------")
for i in range(1,n+1,1):
    print("*" * i,end="")
    print()
# Can the Time Complexity O(n), since I am not using multiple loop
""" Pattern Problem 3: Based on input print following pattern
example if n=5
output should be:
1
12
123
1234
12345

 """
print("-------Patter Problem3 - Solution-------")
for i in range(1,n+1,1):
    for j in range(i):
        print(j+1,end="")
    print()

""" Pattern Problem 4: Based on input print following pattern
example if n=5
output should be:
1
22
333
4444
55555

 """
print("-------Patter Problem4 - Solution-------")
for i in range(1,n+1,1):
    print(str(i)*i,end="")
    print()
# Can the Time Complexity O(n), since I am not using multiple loop
""" Pattern Problem 5: Based on input print following pattern
example if n=5
output should be:
*****
****
***
**
*

 """
print("-------Patter Problem5 - Solution-------")
for i in range(n,0,-1):
    print("*"*i,end="")
    print()
# Can the Time Complexity O(n), since I am not using multiple loop

""" Pattern Problem 6: Based on input print following pattern
example if n=5
output should be:
12345
1234
123
12
1

 """
print("-------Patter Problem6 - Solution-------")
for i in range(n,0,-1):
    for j in range(i):
        print(j+1,end="")
    print()
