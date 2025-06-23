n =int(input("Nhập số lượng phần tử (0<n<100):"))
while n <=0 or n>=100:
    print("Giá trị không hợp lệ.Vui lòng nhập lại.")
    n = int (input("Nhập số lượng phần tử (0<n<100):"))
day_so = []
for i in range(n):
    x = int(input(f"Nhập phần tử thư {i+1} là :"))
    day_so.append(x)
#In các số chẵn 
print("Các số chẵn trong dãy là:")
for m in day_so:
    if m % 2 == 0:
        print(m,end = ' ')
print() #dòng mới

#Xóa các số 0 khỏi dãy
day_khong_0 =[]
for m in day_so:
    if m !=0:
        day_khong_0.append(m)
print("Dãy sau khi xóa các số 0 là:",day_khong_0)