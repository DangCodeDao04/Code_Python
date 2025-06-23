n = int(input("Nhập số nguyên từ (0<n<100) là:"))
while n<=0 or n>=100:
    print("Giá trị không hợp lệ .Vui lòng nhập lại.")
    n=int(input("Nhập số nguyên từ (0<n<100) là:"))
day_so = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1} là:"))
    day_so.append(x)
    
#Dếm âm 
so_duong = 0
for m in day_so:
    if m < 0:
        so_duong += 1
print("\n Số lượng dãy số âm trong dãy là:",so_duong)

so_am=0
for m in day_so:
    if m < 0:
        if so_am ==0 or m < so_am:
            so_am = m
print("\n Số âm lớn nhất trong dãy là:",so_am) 