from tkinter import *
from PIL import ImageTk
import tkinter as tk
import os





def btn1_clicked():
    os.system("python playnt.py --data_dir")


def btn2_clicked():
    os.system("python speechspell.py --data_dir")

def btn3_clicked():
    os.system("python duo.py --data_dir")



app = Tk()
app.iconbitmap('icon.ico')

width=900
height=700
pos_x=width/2
pos_y=height/2

canvas = Canvas(app, width=width, height=height)

canvas.pack(padx=10, pady=10)

img_path=ImageTk.PhotoImage(file="lolbae.img")

shapes = canvas.create_image(width/2, height/2, image = img_path)

app.title("LOL Assistant")

app.geometry("900x700")

b1=tk.Button(app, text="플레이어 알림 및 검색",command=btn1_clicked, fg='#b18600', border=0, bg="#ff6363", font=('티머니 둥근바람 ExtraBold', 9))
b2=tk.Button(app, text="듀오 시너지 추천", command=btn3_clicked,fg='#b18600', border=0, bg="#3d85c6", font=('티머니 둥근바람 ExtraBold', 9))
b3=tk.Button(app, text="음성인식 스펠 체크",command=btn2_clicked, fg='#b18600', border=0, bg="#2d9400", font=('티머니 둥근바람 ExtraBold', 9))

b1.place(x=75, y=390, width=150, height=30)
b2.place(x=75, y=470, width=150, height=30)
b3.place(x=475, y=390, width=150, height=30)


app.mainloop()



