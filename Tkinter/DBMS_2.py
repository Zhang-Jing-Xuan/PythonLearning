import os
import tkinter as tk
import tkinter.font as tkFont
window = tk.Tk()
window.title('DBMS')
window.minsize(100,100)

def Return():
    window1.destroy()
    
def changeString():
    global window1
    window1 = tk.Tk()
    window1.title('DBMS')
    window1.minsize(100,100)
    text_output = tk.Text(window1, width=70, height=20)
    button1 = tk.Button(window1,text="返回",command=Return,padx=32,pady=4,bd=4)
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
    text_output.pack()
    button1.pack()


text_input  = tk.Text(window, width=70, height=20)
button = tk.Button(window,text="执行",command=changeString,padx=32,pady=4,bd=10)
text_input.pack()
button.pack()
window.mainloop()