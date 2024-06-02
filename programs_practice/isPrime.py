num = int(input())



def isPrime(num):
    i = 2
    while i*i <= num:
        if num%i == 0:
            return False
        i = i+1
    return True

ans = isPrime(num)
print(ans)