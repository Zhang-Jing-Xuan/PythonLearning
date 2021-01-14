import os
import tkinter as tk
window = tk.Tk()
window.title('词法分析')
window.minsize(500,500)
 
#点击按钮后执行的函数
def changeString():
    text_output.delete('1.0','end')
    text = text_input.get('1.0','end')
    filename = '/Users/admin/Desktop/CL/C++/word_analyse/word_analyse/code.txt'
    with open(filename,'w') as f: 
        f.write(text)
    
    os.chdir("/Users/admin/Desktop/CL/C++/word_analyse/word_analyse/")
    f = os.popen("./a.out",'r')  
    data = f.readlines()
    data = data[0:-1:1]
    f.close()
    for i in data:
        text_output.insert("insert",i)
#创建文本输入框和按钮
text_input  = tk.Text(window, width=100, height=20)
text_output = tk.Text(window, width=100, height=20)
button = tk.Button(window,text="词法分析",command=changeString,padx=32,pady=4,bd=4)
 

#把Text组件和按钮放在窗口上，然后让窗口打开，并处理在窗口内发生的所有事件；
text_input.pack()
text_output.pack()
button.pack()
window.mainloop()

