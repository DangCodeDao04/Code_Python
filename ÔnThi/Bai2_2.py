n= int(input("Nhập số lượng phần từ (0<n<100): "))
while n <=0 or n>=100:
    print("Giá trị không hợp lê.Vui lòng nhập lại.")
    n=int(input("Nhập só lượng phần tử (0<n<100):"))
day_so = []

#Nhập phần từ vào dãy 
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}:"))
    day_so.append(x)
#Tổng các phần tử là số chẵn
tong_chan = 0
for m in  day_so:
    if m % 2 ==0:
        tong_chan += m

#Tìm số chẵn nhỏ nhất trong dãy
for i in day_so:
    if i % 2 == 0:
        min_chan == i
    if i < min_chan:
        min_chan = i
print("\n Kết quả:")
print("Tổng các số chẵn:",{tong_chan})
print("Số chẵn nhỏ nhất trong dãy:",{min_chan})