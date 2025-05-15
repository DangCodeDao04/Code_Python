#Bai1:
def uscln(a,b):
    #tinh uoc chung lon nhat 
    while b != 0:
        a,b = b,a % b
        
        
    return a
def bscnn(a,b):
    return  a * b // uscln(a,b)

#nhap hai so nguyen duong 
a =int(input("Nhap so nguyen duong a:"))
b = int(input("Nhap so nguyen duong b:"))

if a > 0 and b > 0:
    
    print("USCLN của", a, "và", b, "là:", uscln(a, b))
    print("BSCNN của", a, "và", b, "là:", bscnn(a, b))
else:
    print("Vui lòng nhập hai số nguyên dương.")