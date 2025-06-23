def uscln(a,b):
    while b!=0:
        a,b = b,a % b
    return a
a = int(input("Nhập số nguyên a:"))
b =int(input("Nhập số nguyên b:"))
print("Ước số chung lớn nhất của a và b là",uscln(a,b))

    