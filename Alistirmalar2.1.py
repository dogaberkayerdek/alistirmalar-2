import random
k = random.randint(10,98)

while k % 11 == 0:
         k=random.randint(10,98)


sayi=0
while (sayi != k):
    sayi=int(input("Oyuna başlamak için bir 2 basamakli bir sayı yazınız"))

    if sayi >= 10 and sayi <= 98:
        dogruyer=0
        yanlisyer=0
        if sayi//10 == k // 10:
            dogruyer +=1
        if sayi % 10 == k % 10:
            dogruyer +=1
        if sayi //10 == k % 10:
            yanlisyer -=1
        if sayi % 10 == k // 10:
            yanlisyer -=1
        if dogruyer == 0 and yanlisyer ==0:
            print("2 basamaktaki sayılar da yanlış")
        if dogruyer == 1 and yanlisyer ==0:
            print("Basamaklardan birini buldun!")
        if yanlisyer == -1 and dogruyer ==0:
            print("Basamaklardan birini buldun fakat yanlış yerde")
        if yanlisyer == -2 and dogruyer ==0:
            print("Sayıyı tersten yazdın")
    else:
        sayi=int(input("10 ile 98 arasında bir sayı yazınız ! "))

print("Tebrikler doğru Tahmin !!! ")    
        


