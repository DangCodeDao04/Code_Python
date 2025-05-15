#tim ước số chung lớn nhất
#tìm bội số chung lơn nhất

def uscln(a,b):
    while(b != 0):
        a,b = b, a%b
    return a
def bscln(a,b):
    return a * b // uscln(a,b)
a = int(input("Nhập số a:"))
b = int(input("Nhập số b:"))

print("USCLN:",uscln(a,b))
print("BSCLN:",bscln(a,b))

