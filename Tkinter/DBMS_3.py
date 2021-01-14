import os
import tkinter as tk
import tkinter.font as tkFont
class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)

class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)
        
        self.tk.eval('''
            proc widget_proxy {widget widget_command args} {

                # call the real tk widget command with the real args
                set result [uplevel [linsert $args 0 $widget_command]]

                # generate the event for certain types of commands
                if {([lindex $args 0] in {insert replace delete}) ||
                    ([lrange $args 0 2] == {mark set insert}) || 
                    ([lrange $args 0 1] == {xview moveto}) ||
                    ([lrange $args 0 1] == {xview scroll}) ||
                    ([lrange $args 0 1] == {yview moveto}) ||
                    ([lrange $args 0 1] == {yview scroll})} {

                    event generate  $widget <<Change>> -when tail
                }

                # return the result from the real widget command
                return $result
            }
            ''')
        self.tk.eval('''
            rename {widget} _{widget}
            interp alias {{}} ::{widget} {{}} widget_proxy {widget} _{widget}
        '''.format(widget=str(self)))
        
class Example(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = CustomText(self)
        self.vsb = tk.Scrollbar(orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
        self.linenumbers = TextLineNumbers(self, width=40)
        self.linenumbers.attach(self.text)

        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

        # self.text.insert("end", "one\ntwo\nthree\n")
        # self.text.insert("end", "four\n",("bigfont",))
        # self.text.insert("end", "five\n")
    def _on_change(self, event):
        self.linenumbers.redraw()
    def get(self):
        return self.text.get('1.0','end')

def Return():
    window1.destroy()
    
def changeString():
    global window1
    window1 = tk.Tk()
    window1.title('Result')
    window1.minsize(100,100)
    text_output = tk.Text(window1, width=70, height=20)
    button1 = tk.Button(window1,text="返回",command=Return,padx=32,pady=4,bd=4)
    text_output.delete('1.0','end')
    text = E.get()
    filename = '/Users/admin/Desktop/CL/C++/DBMS_Shell/DBMS_Shell/test.txt'
    with open(filename,'w') as f: 
        f.write(text)
    
    os.chdir("/Users/admin/Desktop/CL/C++/DBMS_Shell/DBMS_Shell")
    f = os.popen("./a.out",'r')  
    data = f.readlines()
    data = data[0:-1:1]
    f.close()
    text_output.tag_configure("bigfont", font=("bold"))
    for i in data:
        text_output.insert("insert",i,)
    text_output.pack()
    button1.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.title('DBMS')
    E=Example(root)
    E.pack(side="top", fill="both", expand=True)
    # Example(root).pack(side="top", fill="both", expand=True)
    button = tk.Button(root,text="执行",command=changeString,padx=32,pady=4,bd=10)
    button.pack()
    root.mainloop()