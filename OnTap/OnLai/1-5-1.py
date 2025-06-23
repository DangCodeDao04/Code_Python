def la_so_doi_xung(n):
    # Chuyển số thành chuỗi và so sánh với chuỗi đảo ngược của nó
    return str(n) == str(n)[::-1]

def main():
    # Nhập và kiểm tra điều kiện n >= 2
    n = int(input("Nhập số nguyên n (n ≥ 2): "))
    if n < 2:
        print("Vui lòng nhập số nguyên lớn hơn hoặc bằng 2.")
        return

    # Kiểm tra đối xứng
    if la_so_doi_xung(n):
        print(f"{n} là số đối xứng.")
    else:
        print(f"{n} không là số đối xứng.")

# Gọi hàm chính
main()
