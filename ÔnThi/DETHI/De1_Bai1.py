def ulcn(a,b):
    while b !=0:
        a,b = b,a % b
    return a
def bscnn(a,b):
    return a * b // ulcn(a,b)
a= int(input("Nhập số nguyên a:"))
b = int(input("Nhập số nguyên b:"))
print("Ước chung của a và b là:",ulcn(a,b))
print("Bộ số chung nhỏ nhất là:",bscnn(a,b))
