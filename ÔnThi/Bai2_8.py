def nhap_day():
    n = int(input("Nhập số lượng phần tử (0 < n < 100): "))
    while n <= 0 or n >= 100:
        n = int(input("Nhập lại n (0 < n < 100): "))
    day = []
    for i in range(n):
        x = int(input(f"Nhập phần tử thứ {i+1}: "))
        day.append(x)
    return day

def in_so_duong_dau_tien(day):
    print("Các số dương đầu tiên trong dãy:")
    for num in day:
        if num > 0:
            print(num, end=' ')
    print()

def sap_xep_giam_va_xoa_am(day):
    day_moi = [x for x in day if x >= 0]  # Bỏ số âm
    day_moi.sort(reverse=True)  # Sắp xếp giảm dần
    print("Dãy sau khi xóa số âm và sắp xếp giảm dần:")
    print(day_moi)

# Chương trình chính
day_so = nhap_day()
in_so_duong_dau_tien(day_so)
sap_xep_giam_va_xoa_am(day_so)
