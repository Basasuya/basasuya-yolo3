

import tkinter as tk
from tkinter import ttk
import numpy as np
import PIL
import PIL.ImageTk
# from PIL import Image, ImageFont, ImageDraw, ImageTk
import tkinter.filedialog
import pymongo as mongo


animalNumber = 80
animalClasses = ['person', 'bicycle', 'car', 'motorbike', 'aeroplane', 'bus', 'train', 'truck',
                 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
                 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella',
                 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard',
                 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana',
                 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'sofa',
                 'pottedplant', 'bed', 'diningtable', 'toilet', 'tvmonitor', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
                 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush', ]
varArray = []


if __name__ == '__main__':
    conn = mongo.MongoClient('127.0.0.1', 27017)
    db = conn.Basasuya

    allDB = tuple(db.collection_names())
    root = tk.Tk()
    root.geometry("1000x600+200+100")
    root.title("I have seen you before")

    w = tk.Canvas(root, width=1000, height=600, background="light blue")
    w.pack()

    w.create_rectangle(20, 15, 145, 135, outline='azure', fill='azure')
    wifi_img = PIL.Image.open('./src/photo.png').resize((80, 80))
    photo = PIL.ImageTk.PhotoImage(wifi_img)
    tk.Button(root, image=photo, width=80, height=80).place(x=30, y=20)
    tk.Label(root, fg='orangered', text='Camera Detection',
             bg='azure').place(x=20, y=110)

    w.create_rectangle(165, 15, 420, 135, outline='azure', fill='azure')
    wifi_img = PIL.Image.open('./src/photo2.jpg').resize((80, 80))
    photo2 = PIL.ImageTk.PhotoImage(wifi_img)
    tk.Button(root, image=photo2, width=80, height=80).place(x=175, y=20)
    tk.Label(root, fg='darkorange', text='insert into\nmongodb collection:',
             bg='azure').place(x=270, y=25)
    tk.Label(root, fg='orangered', text='Video Detection',
             bg='azure').place(x=230, y=110)
    ent1 = tk.Entry(root, width=13)
    ent1.place(x=270, y=60)

    w.create_rectangle(440, 15, 710, 135, outline='azure', fill='azure')
    wifi_img = PIL.Image.open('./src/photo3.jpg').resize((80, 80))
    photo3 = PIL.ImageTk.PhotoImage(wifi_img)
    tk.Button(root, image=photo3, width=80, height=80).place(x=455, y=20)
    tk.Label(root, fg='darkorange', text='read from\nmongodb collection:',
             bg='azure').place(x=560, y=25)
    tk.Label(root, fg='orangered', text='Video Detection Using MongoData',
             bg='azure').place(x=470, y=110)
    com1 = ttk.Combobox(root, width=10, values=allDB, state='readonly')
    com1.current(0)
    com1.place(x=565, y=65)

    w.create_rectangle(730, 15, 980, 135, outline='azure', fill='azure')
    wifi_img = PIL.Image.open('./src/photo4.jpg').resize((80, 80))
    photo4 = PIL.ImageTk.PhotoImage(wifi_img)
    tk.Button(root, image=photo4, width=80, height=80).place(x=740, y=20)
    tk.Label(root, fg='darkorange', text='analysis from\nmongodb collection:',
             bg='azure').place(x=835, y=25)
    tk.Label(root, fg='orangered', text='Detection Analysis',
             bg='azure').place(x=750, y=110)
    com2 = ttk.Combobox(root, width=10, values=allDB, state='readonly')
    com2.current(0)
    com2.place(x=850, y=65)

    com2 = ttk.Combobox(root, width=6, values=('cluster', 'analysis'), state='readonly')
    com2.current(0)
    com2.place(x=880, y=105)

    w.create_rectangle(20, 155, 900, 570, outline='azure', fill='azure')
    for i in range(animalNumber):
        var = tk.IntVar()
        varArray.append(var)
        but = tk.Checkbutton(
            root, text=animalClasses[i], variable=var, bg='azure')
        but.place(x=30 + i % 8*110, y=170 + i//8*40)

    w.create_rectangle(910, 155, 980, 570, outline='azure', fill='azure')
    tk.Label(root, fg='darkorange', text='predict\nthreshold:',
             bg='azure').place(x=910, y=170)
    slider1 = tk.Scale(root, from_=10, to=100, bg='azure', length=300)
    slider1.place(x=910, y=230)
    root.mainloop()
