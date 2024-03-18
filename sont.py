import math
n = int(input("nhap 1 so nguyen duong:"))
if n < 2:
    print(f"{n} ko phai so nguyen duong")
else:
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0 :
            print(f"{n} ko phai so nguyen to")
            break
    else:
        print(f"{n} la so nguyen to")