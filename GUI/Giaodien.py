#-------Các widget trong tkinter
import tkinter as tk
 
 #tạo 1 cửa sổ chính của ứng dụng 
window = tk.TK()

#thêm các thành phần widget vòa cửa sổ
label = tk.Label(window,text="Hello World")
label.pack()
