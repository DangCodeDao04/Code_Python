def ucnnlonhon1(n):
    for i in range (2,n+1):
        if n % i == 0:
            return i
n = int(input("Nhập số nguyên dương n:"))
print("Ước số chia hết cho n lớn hơn 1 là:",ucnnlonhon1(n))