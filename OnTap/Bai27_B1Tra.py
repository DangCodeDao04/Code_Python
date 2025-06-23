def uscln(a,b):
    while(b != 0):
        a,b = b,a % b
    return a
def bscnn(a,b):
    return a * b/uscln(a,b)
a = int(input("Nhập số nguyên a:"))
b =int(input("Nhập số nguyên b:"))

print(f"USCLN của a và b là:",{uscln(a,b)})
print(f"BSCNN của a và b là:",{bscnn(a,b)})
