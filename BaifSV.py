#Xây dựng chương trình quản lý môn học gồm các thông tin: Mã môn học, tên môn học , số tín chỉ.
#Chương trình thực hiện được các công việc sau:
#Nhập được 1 danh sách môn học
#hiện thị thông tin các môn học
#Thêm được một môn học
#xóa được một môn học theo mã
#Tìm kiếm thông tin môn học theo cả 3 trường: Mã môn học, tên môn học , và số tín chỉ 
#Ghi thông tin
#Đọc

class MonHoc:
    def __init__(self,maMH,tenMH,soTC):
        self.maMH = maMH
        self.tenMH = tenMH
        self.soTC =soTC
        
    #Hiện thị 
    def hien_thi(self):
        print("Mã môn học:",self.maMH)
        print("Tên môn học:",self.tenMH)
        print("Số tín chỉ: ",self.soTC)
 
dsMH = [] 
 #Nhập được 1 danh sách môn học
def nhapDSMH():
    n = int(input("Nhập vào số lượng môn học")) 
    for i in range(n):
        maMH = input("Nhập vào mã môn học")
        tenMH = input("Nhập vào tên môn học")
        soTC  = input("Nhập số tín chỉ của:") 
        mh = MonHoc(maMH,tenMH,soTC)
        dsMH.append(mh)
def hienthiDSMH():
    print("Danh sách môn học là:")
    for i in range(len(dsMH)):
        print("Thông tin môn học ",i + 1)
        dsMH[i].hien_thi()
            
def main():
    nhapDSMH()         
    hienthiDSMH() 
main()