import tkinter as tk
from tkinter import messagebox
import FirstScreen_support

# Function to visiable our first interface
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Knapsackfirst (root)
    FirstScreen_support.init(root, top)
    root.mainloop()

w = None
# initializing all the gui used components
class Knapsackfirst:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("400x300+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Knapsack")
        top.configure(background="#c0c0c0")

        # label to ask the user to select a version
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.1, rely=0.2, height=21, width=314)
        self.Label1.configure(background="#c0c0c0")
        self.Label1.configure(font="-family {System} -size 10 -weight bold")
        self.Label1.configure(foreground="#400000")
        self.Label1.configure(text='''Select your favourite knapsack version''')
        
        c_v = tk.StringVar(root)
        self.x =0

        # 2 Functions To make the user choose only one version
        def checkB():
            if c_v.get() == 'Yes':
                self.UnboundKnapsack.config(state="disable")
                self.x =  1
            else:
                self.UnboundKnapsack.config(state="normal")
                self.x = 0
            return self.x

        def check01():
            if c_v.get() == 'No':
                self.knapsack01.config(state="disable")
                self.x =  1
            else:
                self.knapsack01.config(state="normal")
                self.x = 0
            return self.x


        self.knapsack01 = tk.Checkbutton(top)
        self.knapsack01.place(relx=0.2, rely=0.4, relheight=0.083
                , relwidth=0.303)
        self.knapsack01.configure(background="#c0c0c0")
        self.knapsack01.configure(font="-family {System} -size 10 -weight bold")
        self.knapsack01.configure(justify='left')
        self.knapsack01.configure(text='''0_1 Knapsack''')
        self.knapsack01.configure(variable=c_v) 
        self.knapsack01.configure(onvalue='Yes', offvalue='')
        self.knapsack01.configure(command=checkB)

        self.UnboundKnapsack = tk.Checkbutton(top)
        self.UnboundKnapsack.place(relx=0.2, rely=0.533, relheight=0.083
                , relwidth=0.453)
        self.UnboundKnapsack.configure(background="#c0c0c0")
        self.UnboundKnapsack.configure(font="-family {System} -size 10 -weight bold")
        self.UnboundKnapsack.configure(foreground="#000000")
        self.UnboundKnapsack.configure(text='''Unbounded Knapsack''')
        self.UnboundKnapsack.configure(variable=c_v) 
        self.UnboundKnapsack.configure(onvalue='No', offvalue='')
        self.UnboundKnapsack.configure(command=check01)

        # The start botton to open the next interface to make the user start the game
        def ok():
            i=checkB()
            j=check01()
            if i == 1 or j==1:
               # if user choose (0-1 knapsack) the 0-1 knapsack window will open
               if i == 1:
                FirstScreen_support.destroy_window()
                import Knapsack
                Knapsack.vp_start_gui()
                # if user choose (Unbounded knapsack) the 0-1 knapsack window will open
               elif j == 1:
                FirstScreen_support.destroy_window()
                import UnboundedKnapsack
                UnboundedKnapsack.vp_start_gui()
                # if user wouldn't choose this message appears 
            else :
                messagebox.showerror("Warning", "Plz make a selection")

        self.selectKbtn = tk.Button(top)
        self.selectKbtn.place(relx=0.7, rely=0.733, height=34, width=47)
        self.selectKbtn.configure(background="#808080")
        self.selectKbtn.configure(borderwidth="3")
        self.selectKbtn.configure(font="-family {System} -size 10 -weight bold")
        self.selectKbtn.configure(text='''OK''')
        self.selectKbtn.configure(command=ok)





