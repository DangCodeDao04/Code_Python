from tkinter import *
window = Tk()
window.title("Welcome to Uneti.")

#thêm label có nội dung Hello font chữ "Arial Bold , cỡ chữ 50"
lbl = Label(window,text = "A", font=("Arial Bold", 50),fg="red" )

window.geometry("280x80")
lbl.grid(column=1, row = 0) # xác định vị trí của label
lbl.pack(anchor="center")
window.mainloop()