from tkinter import * 
 
window = Tk() 
window.title("Welcome to Uneti") 
window.geometry('300x80') 
lbl = Label(window, text="Hello") 
lbl.grid(column=0, row=0) 
 
#Hàm khi nút được nhấn 
def clicked(): 
    lbl.configure(text="Xin chào bạn ") 
#Thêm một nút nhấn Click Me 
btn = Button(window, text="Ấn nút ", bg="orange",  
                       fg="red",command=clicked) 
 
#Thiết lập vị trí của nút nhấn có màu nền và màu chữ 
btn.grid(column=5, row=0) 
 
window.mainloop() 