n = int(input("Nhập số phần tử trong (0<n<100) là:"))
while n<=0 or n>=100:
    print("Giá trị không hợp lệ.Vui lòng nhập lại.")
    n = int(input("Nhập số phần tử trong(0<n<100) là:"))
day_so = []
for i in range(n):
    x = int(input(f"Nhập số phần tử {i+1} là:"))
    day_so.append(x)
    