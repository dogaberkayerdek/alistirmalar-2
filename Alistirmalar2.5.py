def asalmi(n):
    if n<2:
        return False
    else:
        for i in range ( 2,n):
            if n % i ==0:
                return False
        return True

    
def superasalmi(k):
    if k <= 0:
        return True
    if asalmi(k):
        return superasalmi(k//10)

for x in range (10000,100000):
    if superasalmi(x):
        print(x)
