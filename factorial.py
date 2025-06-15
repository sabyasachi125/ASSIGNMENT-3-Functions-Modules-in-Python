***
factorial
0!=1
1!=1
2!=2 * (2-1)!=2
***
def factorial(n):
    if n <2:
        return 1
    else:
        return n * (factorial(n-1))
        
result=factorial(4)
print(result)