def ucln(a,b):
    while b != 0:
        a,b = b,a % b
    return a
def bscnn(a , b):
    return a * b // ucln(a,b)
a = int(input("Nhập số nguyên a:"))
b = int(input("Nhập số nguyên b:"))
print("USCLN của a và b là:",ucln(a,b))
print("BSCNN của a và b là:",bscnn(a,b))
