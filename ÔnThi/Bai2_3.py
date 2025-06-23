#Cho dãy n số nguyên (0<n<100). Hãy viết chương trình thực hiện các yêu cầu sau: 
#2_2_3.1. Tính trung bình cộng các phần tử là số lẻ 
#2_3_3.2. Tìm số lẻ nhỏ nhất của dãy 
import math
n = int(input("Nhập số lượng phần tử (0<n<100):"))
while n<=0 or n>=100:
    print("Giá trị không hợp lệ.Vui lòng nhập lại.")
    n = int(input("Nhập số lượng phần tử (0<n<100):"))
day_so = []
#Nhập các phần tử vào dãy 
for i in range(n):
    x =int(input(f"Nhập phần tử thứ {i+1}:"))
    day_so.append(x)
#Tính trung bình cộng các phần tử là số lẻ
#so_le = 0
#for m in day_so:
   # if m % 2 !=0:
        #so_le += m
        #tbc = sum(so_le)/len(so_le)
       # print("Trung bình cộng của các số lẻ:",{tbc})
tong = 0
dem = 0
for num in day_so:
    if num % 2 != 0:
        tong += num 
        dem +=1
if dem > 0:
    tbc = tong / dem
    print("Trung bình cộng của các số lẻ:",{tbc})
else:
    print("Không có số lẻ trong dãy.")       

    #Tìm số lẻ nhỏ nhất trong dãy
# Lọc ra danh sách các số lẻ
so_le = 0
for num in day_so:
    if num % 2 != 0:
        so_le += num
        
if so_le:
    min_le = min(so_le)
    print("Số lẻ nhỏ nhất trong dãy:", min_le)
else:
    print("Dãy không có số lẻ.")
