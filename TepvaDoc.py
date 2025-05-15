f = open("d:\\ghithongtin.txt",'r',encoding = "utf-8")
s = f.readline()
print(s)

f = open("d:/DHMT16A1HN.txt","w",encoding = 'utf-8')

f.writelines("Lớp Mạng Máy Tính 16A1")

f = open("d:/DHMT16A1HN.txt",'r',encoding="utf-8")
for line in f:
    print(line)
f.close()

f = open("d:/DHMT16A1HN.txt",'r',encoding="utf-8")
ch = f.read(1)
text = f.readlines() # đọc tất cả các dòng
print(text)
print(ch)
f.close