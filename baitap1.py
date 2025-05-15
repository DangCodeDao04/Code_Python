def uscln(a,b):
    while(b != 0):
        a,b = b , a % b
    return a
def bscnn(a,b):
    return a * b // uscln(a,b)

a = int(input("Nhập số a:"))
b = int(input("Nhập số b:"))
print("USCLN:",uscln(a,b))
print("BSCNN:",bscnn(a,b))
        
