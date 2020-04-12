#!/usr/bin/env python3
# coding:utf8
import signal
import threading
import tkinter
import turtle
import time
from tkinter import *
import os
from base.thread_kill import stop_thread


PATH = os.path.abspath(os.path.dirname(os.getcwd()))
def open_turtle(text ,x ,y):
    try:

        turtle.setup(width=0.3, height=0.3)
        turtle.screensize(300, 300, "deepskyblue")

        turtle.color("white")
        turtle.speed(1)
        turtle.penup()
        time.sleep(0.5)
        turtle.goto(x, y)
        turtle.speed(1)
        turtle.pendown()
        turtle.write(text, font=("Times", 18, "bold"))
        time.sleep(1)
        turtle.color("red")
        turtle.speed(1)
        turtle.penup()
        time.sleep(0.5)
        turtle.goto(-80, -80)
        turtle.speed(1)
        turtle.pendown()
        turtle.write("等待系统运行 . . .", font=("Times", 16, "bold"))
        # 隐藏箭头
        turtle.hideturtle()

        # try:
        #     # 获取pid并杀死进程
        #     pid = os.getpid()
        #     print('已杀死pid为%s的进程,　返回值是:%s' % (pid, pid))
        #     os.kill(pid, signal.SIGILL)
        # except:
        #     print('杀死进程失败')
        # # 暂停界面，使得用户能够看见展示的图形
        # turtle.done()
    except:
        print('有主线程未结束')

def open_tkinter(path,quote,case_text):
    '''
    lable
    :param file:
    :param text:
    :return:
    '''
    root = Tk()
    try:
        text1 = Text(root, height=40, width=70)
        photo = PhotoImage(file=PATH+path)
        text1.insert(END, '\n')
        text1.image_create(END, image=photo)
        text1.pack(side=LEFT)
        text2 = Text(root, height=40, width=70)
        scroll = Scrollbar(root, command=text2.yview)
        text2.configure(yscrollcommand=scroll.set)
        text2.tag_configure('bold_italics', font=('Arial', 13,))
        text2.tag_configure('big', font=('Verdana', 20, 'bold'))
        text2.tag_configure('color', foreground='#476042',
                            font=('Tempus Sans ITC', 18, 'bold'))
        text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
        text2.insert(END, '\n web端自动化测试 \n', 'big')
        # quote = """
        #   -----------模拟用户登陆测试-----------
        # """
        text2.insert(END, quote, 'color')
        text2.insert(END, '\n   ' + case_text + '\n', 'bold_italics')
        text2.pack(side=LEFT)
        scroll.pack(side=RIGHT, fill=Y)

        # 显示倒计时Label
        lbTime = tkinter.Label(root, fg='red', anchor='w')
        lbTime.place(x=495,y=500,width=495)
        # lbTime.pack()  # 自动调整布局
        def autoClose():
            for i in range(10):
                lbTime['text'] = '距离窗口关闭还有{}秒'.format(10 - i)
                time.sleep(1)
            root.destroy()
            root.quit()
        t = threading.Thread(target=autoClose)
        t.setDaemon(True)
        t.start()
        root.mainloop()
        stop_thread(t)
        t.join()


    except:
        print('未能找到.gif图片路径')


def open_tk(path,case_text):
    '''
    :param path:
    :param case_text:
    :return:
    '''
    root = Tk()
    try:
        photo = PhotoImage(file=PATH+path)  # 声明一下图片
        print(PATH)
        theLabel = Label(root,
                         text=case_text,  # 载入文本
                         justify=CENTER,  # 声明文本的位置
                         image=photo,  # 载入图片
                         compound=CENTER,  # 声明图片的位置
                         font=("楷体", 20),  # 声明文本字体
                         fg="green"  # 声明文本颜色 .
                         )
        theLabel.pack()  # 自动调整布局
        #显示倒计时Label
        lbTime = tkinter.Label(root, fg='red', anchor='w')
        lbTime.place(x=380, y=260, width=250)
        L = threading.Lock()
        def autoClose():
            L.acquire()
            for i in range(10):
                lbTime['text'] = '距离窗口关闭还有{}秒'.format(10 - i)
                time.sleep(1)
            root.destroy()
            root.quit()
            L.release()

        tt = threading.Thread(target=autoClose)
        tt.setDaemon(True)
        tt.start()
        root.mainloop()
        stop_thread(tt)
        tt.join()
    except:
        print('未能找到.gif图片路径')