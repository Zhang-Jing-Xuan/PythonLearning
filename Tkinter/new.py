import tkinter as tk
import tkinter.font as tkFont
window=tk.Tk
window = tk.Tk()
window.title('DBMS')
window.minsize(100,100)

def Return():
    window1.destroy()
    
def changeString():
    global window1
    text = text_input.get('1.0','end')
    window1 = tk.Tk()
    window1.title('DBMS')
    window1.minsize(100,100)
    text_output = tk.Text(window1, width=45, height=10,font=tkFont.Font(size=15))
    button1 = tk.Button(window1,text="返回",command=Return,padx=32,pady=4,bd=4)
    text_output.insert("insert",text)
    text_output.pack()
    button1.pack()

text_input  = tk.Text(window, width=40, height=10,font=tkFont.Font(size=15))
button = tk.Button(window,text="执行",command=changeString,padx=32,pady=4,bd=4)
text_input.pack()
button.pack()
window.mainloop()