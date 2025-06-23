#Cho dãy n số nguyên (0<n<100). Hãy viết chương trình thực hiện các yêu cầu sau: 
#2_2_1.1. Tính tổng các phần tử là số lẻ 
3 
#2_3_1.2. Tìm phần tử nhỏ nhất của dãy
n =int(input("Nhập só lượng phần tử (0<n<100):"))
while n <=0 or n>=100:
    print("Giá trị không hợp lê.Vui lòng nhập lại.")
    n=int(input("Nhập só lượng phần tử (0<n<100):"))
    
day_so = []
#Nhập từng phần tử của dãy 
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}:"))
    day_so.append(x)
    #Tính tổng các phần tử là số lẻ 
tong_so_le = 0
for m in day_so:
    if m % 2 !=0:
        tong_so_le += m
#Tìm phẩn tử nhỏ nhất trong dãy 
min_ptu = min(day_so)

print("\n Kết quả:")
print("Tổng các số lẻ:",{tong_so_le})
print("Phần tử nhỏ nhất trong dãy:",{min_ptu})
    
        

 