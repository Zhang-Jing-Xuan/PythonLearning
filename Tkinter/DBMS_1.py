import os
import tkinter as tk
import tkinter.font as tkFont
window = tk.Tk()
window.title('DBMS')
window.minsize(100,100)
 
#点击按钮后执行的函数
def changeString():
    text_output.delete('1.0','end')
    text = text_input.get('1.0','end')
    filename = '/Users/admin/Desktop/CL/C++/DBMS_Shell/DBMS_Shell/test.txt'
    with open(filename,'w') as f: 
        f.write(text)
    
    os.chdir("/Users/admin/Desktop/CL/C++/DBMS_Shell/DBMS_Shell")
    f = os.popen("./a.out",'r')  
    data = f.readlines()
    data = data[0:-1:1]
    f.close()
    for i in data:
        text_output.insert("insert",i)

# create Scrollbar
scroll1 = tk.Scrollbar()
scroll1.pack(side=tk.RIGHT,fill=tk.Y)
scroll2 = tk.Scrollbar()
scroll2.pack(side=tk.RIGHT,fill=tk.Y)
#创建文本输入框和按钮
text_input  = tk.Text(window, width=40, height=10)
text_output = tk.Text(window, width=40, height=10)
button = tk.Button(window,text="执行",command=changeString,padx=32,pady=4,bd=4)


scroll1.pack(side=tk.RIGHT,fill=tk.Y) # side是滚动条放置的位置，上下左右。fill是将滚动条沿着y轴填充
scroll2.pack(side=tk.RIGHT,fill=tk.Y) # side是滚动条放置的位置，上下左右。fill是将滚动条沿着y轴填充
#把Text组件和按钮放在窗口上，然后让窗口打开，并处理在窗口内发生的所有事件；
text_input.pack()
scroll1.config(command=text_input.yview) # 将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
text_input.config(yscrollcommand=scroll1.set) # 将滚动条关联到文本框

text_output.pack()
scroll2.config(command=text_output.yview) # 将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
text_output.config(yscrollcommand=scroll2.set) # 将滚动条关联到文本框

button.pack()
window.mainloop()

