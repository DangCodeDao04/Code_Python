import math
n =int(input("Nhập số lượng phần tử (0<n<100):"))
while n<=0 or n>=100:
    print("Giá trị không hợp lệ.Vui lòng nhập lại.")
    n = int(input("Nhập số lượng phần tử (0<n<100):"))
day_so = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}:"))
    day_so.append(x)
    
#In ra các số chính phương trong dãy 
def so_chinh_phuong(x):
    return int(math.sqrt(x)) ** 2 == x
print("Các số chính phương trong dãy là:")
for num in day_so:
    if so_chinh_phuong(num):
        print(num, end=' ')
print()

#Sắp xếp dãy tăng dần và xóa không chính phương
chinh_phuong = []
for x in day_so:
    if so_chinh_phuong(x):
        chinh_phuong.append(x)
chinh_phuong.sort()
print("Dãy sau khi sắp xếp tăng dần và xóa các số  không phải chính phương:", chinh_phuong)