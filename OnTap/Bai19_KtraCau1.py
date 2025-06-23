def uscln(a,b):
    while(b !=0):
        a,b =b,a % b
    return a
def bscnn(a,b):
    return a * b/uscln(a,b)
a = int(input("Nhập số nguyên a:"))
b = int(input("Nhập số nguyên b:"))
if a> 0 and b >0:
    print("USCLN của", a, "và", b, "là:", uscln(a, b))
    print("BSCNN của", a, "và", b, "là:", bscnn(a, b))
else:
    print("Vui lòng nhập hai số nguyên dương.")