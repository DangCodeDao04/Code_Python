n = int(input("Nhập số lượng phần tử (0<n<100)"))
if 0 < n <100:
    day_so = []
    for i in range(n):
        x = int(input(f"Nhập phần tử thứ {i+1}:"))
        day_so.append(x)
        
        #tinh tong các phần tử là số chẵn
        tong_chan = 0
    for x in day_so:
      if x % 2 == 0:
        tong_chan += x
        
        #tìm phần tử lớn nhất cảu dẫy
        lon_nhat = max(day_so)
    print("Tổng các phần tử là số chẵn:", tong_chan)
    print("Phần tử lớn nhất trong dãy:", lon_nhat)
else:
    print("Giá trị n không hợp lệ. Vui lòng nhập 0 < n < 100.")