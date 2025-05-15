def chao_hoi(ten):
    """"Hàm này chào người dùng theo tên. """
    return f"Xin chào,{ten}!"

print(chao_hoi("Nam"))

#hàm kiểm tra số chẵn hay số lẻ 
def kiem_tra_chan_le(n):
    """Hàm kiểm tra số chẵn hay lẻ  """
    if(n % 2 == 0):
        return "Số chẵn"
    else:
        return "Số lẻ "

#Goi hàm
print(kiem_tra_chan_le(4))
print(kiem_tra_chan_le(7))


#function 
#Tham số: Parameter
def tong(a,b):
    res = a + b
    return res
m,n = 10 , 20

print(tong(m,n)) #đối số =  tham số chính thức =  Argument

#Viết hàm tính giai thừa

def gt(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res


#Luyện tập hàm 
from math import *
# 1. Kiểm tra n là số nguyeennn tố nếu đúng là in ra 1 , sai in ra 0
def ham1(n):
    if n < 5:
        return False
    for i in range(2,isqrt(n)+1):
        if n % i == 0:
           return False
    return True    


  