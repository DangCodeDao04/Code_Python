n =  int(input("Nhập số nguyên n:"))
while n>=0 or n<=100:
    n = int(input("Vui lòng nhập lại số nguyên trong khoảng(0<n<100):"))
day_so = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}:"))
    day_so.append(x)
tong_chan = (x for x in day_so if x % 2 ==0)
max_value = max(day_so)

print("Tổng các phần tử các số chẵn:",{tong_chan})
print("Phần tử lớn nhất của dãy:",{max_value})
