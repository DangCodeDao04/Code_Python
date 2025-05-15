

#Ghi vao danh sach sinh vien

with open("d:/sinhvien.txt","w",encoding="utf-8") as f:
    while True:
        masv = input("Nhập mã sinh viên:")
        if masv =="":
            break
        hoten = input("Nhap họ tên:")
        namsinh = input("Nhập năm sinh:")
        f.write(masv + " , "+ hoten + "," + namsinh + "\n" )
        f.close()
        print("\n Đã Lưu")
        
        #dọc
        print("\n Danh sách sinh vien")
        f = open("d:/sinhvien.txt","r",encoding="utf-8")
        ch = f.read()
        print(ch)
       