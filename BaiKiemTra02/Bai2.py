def tinh_tong_chan(danh_sach):
    tong = 0
    for x in danh_sach:
        if x % 2 == 0:
            tong += x
    return tong
def tim_phan_tu_lon_nhat(danh_sach):
    return max(danh_sach)

# Nhập số lượng phần tử n
n = int(input("Nhập số lượng phần tử n (0 < n < 100): "))
if 0 < n < 100:
    day_so = []
    for i in range(n):
        so = int(input(f"Nhập phần tử thứ {i+1}: "))
        day_so.append(so)

    # a) Tổng số chẵn
    tong_chan = tinh_tong_chan(day_so)
    print(f"Tổng các phần tử chẵn trong dãy là: {tong_chan}")

    # b) Phần tử lớn nhất
    max_phan_tu = tim_phan_tu_lon_nhat(day_so)
    print(f"Phần tử lớn nhất trong dãy là: {max_phan_tu}")
else:
    print("Giá trị n không hợp lệ! Phải 0 < n < 100.")
