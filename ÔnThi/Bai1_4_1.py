def uscln(a,b):
    while b != 0:
        a,b = b,a % a
    return a
def bscnn(a,b):
    return a * b // uscln(a,b)
a = int(input("Nhập số nguyên n:"))
b =int(input("Nhập số nguyên b:"))
print("USCLN của a và b là:",uscln(a,b))
print("BSCNN của a và b là:",bscnn(a,b))