def uscln(a,b):
    while(b !=0):
        a,b = b,a % b
    return a
def bscln(a,b):
       return a * b/uscln(a,b)
a = int(input("Nhâp số nguyên dương a:"))
b = int(input("Nhập số nguyên dương b: "))

if a > 0 and b > 0:
    print("USCLN của",a,"và của",b,"là:",uscln(a,b))
    print("BSCLN của", a,"và của", b,"là:",bscln(a,b))
    