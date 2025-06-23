n = int(input("Nhập số lượng phần tử của dãy (0 < n <100):"))
while n <=0 or n>=100:
    n =int(input("Vui lòng nhập lại n (0 < n < 100)"))
day_so = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}:"))
    day_so.append(x)
    
tong_chan = sum(x for x in day_so if x % 2 == 0)

max_value = max(day_so)

print("Tổng các phẩn tử chẵn trong dãy là:",tong_chan)
print("Phần tử lớn nhất trong dãy là:",max_value)