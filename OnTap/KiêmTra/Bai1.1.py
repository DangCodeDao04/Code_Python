def uscln(a,b):
    while(b != 0):
        a,b = b,a % b
    return a
a = int(input("Nhập số nguyên a:"))
b =int(input("Nhập số nguyên b:"))
print("USCLN là:",{uscln(a,b)})
