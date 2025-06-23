def uscln(a,b):
    while(b!=0):
        a,b = b,a % b
    return a
def bscln(a,b):
    return a * b /uscln(a,b)

a = int(input("Nhập số nguyên a:"))
b = int(input("Nhập số nguyên b: "))
if a>0 and b>0:
    print("USCLN của a và b là:",uscln(a,b))
    print("BSCLN là: ",bscln(a,b))
    
