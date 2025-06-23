
def so_nguyen_to(n):
   if n < 2:
       return False 
   else:
        for i in range(2, int(n **0.5) + 1):
            if i % 2 == 0:
                return False
            return True 
n = int(input("Nhập số nguyên n:"))
print("Đây là số nguyên tố là:",so_nguyen_to(n))
 