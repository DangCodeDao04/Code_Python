class MonHoc:
    def __init__(self,maMH,tenMH,soTC): #hàm khởi tạo
        self.maMH = maMH
        self.tenMH = tenMH
        self.soTC = soTC
    def hienthi(self):
        print("Mã môn học",self.maMH)
        print("Tên môn học",self.tenMH)
        print("Số tín chỉ",self.soTC)
dsmh = [] #danh sách rỗng và gán biến vào đó

#Nhập 1 danh sách môn học 
def nhapdsmh():
    n = int(input("Nhập vào số lượng môn học:"))
    
    for i in range(n):
        maMH = input("Nhập mã môn học ")
        tenMH = input("Nhập tên môn học")
        soTC = input("Nhập số tín chỉ của môn học")
        mh = MonHoc(maMH,tenMH,soTC)
        dsmh.append(mh)
def hienthidsmh():
    print("Danh sách môn học là:")
    for i in range(len(dsmh)):
       print("Thông tin môn học ",i + 1)
    dsmh[i].hien_thi()
    
def themMH():
    print("Nhập vào thông tin môn học cần thêm:")
    maMH = input("Nhập vào mã môn học")
    tenMH = input("Nhập tên môn học ")
    soTC = input("Nhập vào số tín chỉ:  ")
    mh = MonHoc(maMH,tenMH,soTC)
    dsmh.append(mh)
    
def XoaMHTheoMa(maXoa):
    for mh in dsmh:
        if(mh.maMH ==maXoa):
            dsmh.remove(mh)
                
def timKiem(thongTin):
    for i in dsmh(len(dsmh)):
        if(dsmh[i].maMH == thongTin or dsmh[i].tenMH == thongTin or dsmh[i].soTC ==int(thongTin))
        dsmh[i].hienthidsmh()
            
  
                     
def main():
    nhapdsmh()
    maXoa = input("Nhâp vào mã MH cần xóa: ")
    XoaMHTheoMa(maXoa)
    print("Danh sách môn học sau khi xoa",maXoa)
    hienthidsmh()      
    
main()
