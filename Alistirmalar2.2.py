def topla(n):
    if n == 1:
        return 1
    else:
        return topla(n-1)+ n
