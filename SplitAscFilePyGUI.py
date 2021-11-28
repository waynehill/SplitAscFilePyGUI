#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HE.ZW
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
from tkinter import *  # 导入所有的tkinter特性？？为什么没有messagebox
import time

root    = tk.Tk()
root.withdraw()  # ??
windows = tk.Tk()
windows.title("ASC文件分割")
windows.geometry("380x200")  # 界面大小
# 设置输入框，对象是在windows上，show参数--->显示文本框输入时显示方式None:文字不加密，show="*"加密
FILE_COL_Entry = tk.Entry(windows, show=None)
FILE_COL_Entry.pack()  # ??mean what；pack用于设置在窗口内的位置及大小


def getFileDir():
    global file_path
    file_path = filedialog.askopenfilename()  # 单文件


def runSplit():
    start_time = time.time()
    global file_col_num
    file_col_num = FILE_COL_Entry.get()  # 获取输入的信息
    f = open(file_path, 'r')  # 打开文件
    i = 1  # 设置计数器
    while 1:  # 这里12345表示文件行数，如果不知道行数可用每行长度等其他条件来判断
        with open('outFile' + str(i) + '.asc', 'w') as f1:
            if i != 1:
                f1.writelines('base hex  timestamps absolute\n')
            for j in range(0, int(file_col_num)):  # 这里设置每个子文件的大小
                tmpLine = f.readline()
                if not tmpLine:
                    f1.close()
                    end_time = time.time()
                    time_span = end_time - start_time
                    if time_span > 3600:
                        tk.messagebox.showinfo('提示', '完成文件转换，源文件被分割为' + str(i) + '个文件, 耗时' + str(time_span/60/60) + '小时')
                    elif time_span > 60:
                        tk.messagebox.showinfo('提示', '完成文件转换，源文件被分割为' + str(i) + '个文件, 耗时' + str(time_span/60) + '分钟')
                    else:
                        tk.messagebox.showinfo('提示', '完成文件转换，源文件被分割为' + str(i) + '个文件, 耗时' + str(time_span) + '秒')
                    exit()
                else:
                    f1.writelines(tmpLine)
        i = i + 1
        f1.close()


#  说明文字
infoLable = tk.Label(windows, text='1 - 在输入框^^^输入分割后文件的行数\n2 - 点击<打开源文件>\n3 - 点击\'<开始分割>\' \n提示：500万行文件对应300M文件尺寸')
infoLable.pack()
#  弹出源文件地址获取对话框
b1 = tk.Button(windows, text="打开源文件(.asc)", width=25, height=2, command=getFileDir)
b1.pack()
#  启动分割
b2 = tk.Button(windows, text="开始分割", width=25, height=2, command=runSplit)
b2.pack()
# 设置文本框
#  t = tk.Text(windows, text="提示：500万行文件对应300M文件尺寸", height=2)
#  t.pack()

windows.mainloop()
