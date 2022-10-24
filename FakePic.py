#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from tkinter import messagebox
import tkinter as tk
import random
import time
import os

def gettime():
    t = time.localtime()
    global timedate
    timedate = time.strftime("%Y%m%d%H%M%S", t)
    date_entry.delete(0, "end")
    date_entry.insert(0, timedate)
    return

def randsize():
    rand_size = random.uniform(1,4)
    rand_size = round(rand_size,2)
    size_entry.delete(0, "end")
    size_entry.insert(0,rand_size)
    return

def randformat():
    formats = ['jpg','jpeg','png','bmp']
    rands = random.randint(0,3)
    format_entry.delete(0, "end")
    format_entry.insert(0, formats[rands])
    return

def judge():
    time_get = date_entry.get()
    size_get = size_entry.get()
    format_get = format_entry.get()
    if time_get == "":
        gettime()

    if size_get == "":
        randsize()

    if format_get == "":
        randformat()

    return

def generate():
    judge()
    time_get = date_entry.get()
    size_get = size_entry.get()
    format_get = format_entry.get()
    if len(time_get) !=14:
        messagebox.showwarning("警告","日期长度非14位，继续可能操作会造成某些影响，建议重新检查")

    if float(size_get) >=8:
        messagebox.showerror("错误","文件大小不能超过8MB")
        return

    randnum = str(random.randint(1000,9999))
    filename = "IMG_" + time_get + randnum + ".txt"
    file_name = "IMG_" + time_get + randnum + "." + format_get
    size = int(float(size_get) *1024*1024)
    bool = messagebox.askokcancel("请确认", "将生成名为 " + file_name + " 的文件")
    if bool==True:
        file = open(filename, 'w')
        file.close()

        real_size = 0
        while size>real_size:
            statinfo = os.stat(filename)
            real_size=statinfo.st_size
            f=open(filename,'a')
            f.write('Copyright ThanatosXY.All Rights Reserved.\n'
                    'Copyright ThanatosXY.All Rights Reserved.\n'
                    'Copyright ThanatosXY.All Rights Reserved.\n')
            f.close()
        os.rename(filename,file_name)


root = tk.Tk()
root.title("虚假图片生成器")
root.geometry("780x440+230+110")

date_lab = tk.Label(root,text="输入日期         格式:年月日时分秒")
date_lab.place(x=24, y=2)
date_entry = tk.Entry(root)
date_entry.place(x=5,y=30)
date_btn = tk.Button(root,text="自动获取",width=6,command=gettime)
date_btn.place(x=160,y=25)

size_lab = tk.Label(root,text="输入大小         单位:MB")
size_lab.place(x=20,y=65)
size_entry = tk.Entry(root)
size_entry.place(x=5,y=90)
size_btn = tk.Button(root,text="随机大小",width=6,command=randsize)
size_btn.place(x=160,y=85)

format_lab = tk.Label(root,text="输入文件格式         例:jpg")
format_lab.place(x=15,y=120)
format_entry = tk.Entry(root)
format_entry.place(x=5,y=150)
format_btn = tk.Button(root,text="随机大小",width=6,command=randformat)
format_btn.place(x=160,y=145)

generate = tk.Button(root,text="生成",width=6,command=generate)
generate.place(x=30,y=190)

comment1 = tk.Label(root,text="使用说明\n")
comment1.place(x=450,y=15)
comment2 = tk.Label(root,text="1.输入的日期为14位纯数字,如2022年1月2日13点14分55秒,输入为20220102131455")
comment2.place(x=290,y=40)
comment3 = tk.Label(root,text="2.输入的文件大小值为0-8MB,由于生成速度原因所以设置了上限,生成速度约为0.1MB/s")
comment3.place(x=290,y=65)
comment4 = tk.Label(root,text="3.输入的文件格式可以为任意格式,常用图片格式为jpg,jpeg,png等")
comment4.place(x=290,y=90)
comment5 = tk.Label(root,text="4.所生成的虚假文件默认保存到此程序的路径下,后续版本可能会增加选择路径保存的功能")
comment5.place(x=290,y=115)

root.mainloop()
