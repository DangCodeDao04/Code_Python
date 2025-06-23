#Hãy viết chương trình (có sử dụng các hàm) thực hiện các yêu cầu sau: 
#1_1_1.1. Nhập vào từ bản phím hai số nguyên dương a và b. Tính ước số chung lớn nhất 
#của a và b. 

def uscln(a,b):
    while b != 0:
        a,b = b,a % a
    return a

def bscnn(a,b):
    return  a * b //uscln(a,b)

a = int(input("Nhập vào số nguyên a:"))
b = int(input("Nhập vào số nguyên b:"))
if a > 0 and b > 0:
    print("USCLN của", a, "và", b, "là:", uscln(a, b))
    print("BSCNN của", a, "và", b, "là:", bscnn(a, b))
else:
    print("Vui lòng nhập hai số nguyên dương.")
    