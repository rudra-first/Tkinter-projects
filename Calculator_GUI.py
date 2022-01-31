import operator
import math
import tkinter as tk

Calculated_Number = 0
Sign = ""

ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.truediv,
       'x⁻⁻': operator.pow,
       '²√': math.sqrt}
#----------------------------------------------------------------------------------------------------------
def number_inserter(Btn_Num):
    Number_of_Btn = Ent_EnterNumber.get()
    NewNumber = Number_of_Btn + Btn_Num
    Ent_EnterNumber.delete(0, tk.END)
    Ent_EnterNumber.insert(0, NewNumber)


def Change_Sign(_operator):
    global Sign
    Sign = _operator
    Lbl_Sign['text'] = Sign


Counter = 0
def On_Symbol_Click(SecondNumber):
    global Calculated_Number
    global Counter
    if Ent_EnterNumber.get() != "":
        if Counter < 1:
            Counter += 1
            Lbl_EnteredNumber['text'] = Ent_EnterNumber.get()
        elif Counter >= 1:
            Calculated_Number = ops[Sign](SecondNumber, float(Ent_EnterNumber.get()))
            Lbl_EnteredNumber['text'] = str(Calculated_Number)
    Ent_EnterNumber.delete(0, tk.END)

def Clear():
    global Sign
    global Calculated_Number
    Ent_EnterNumber.delete(0, tk.END)
    Sign = ""
    Calculated_Number = 0
    Lbl_EnteredNumber['text'] = "0"
    Lbl_Sign['text'] = ""

def Equals():
    global Calculated_Number
    global Counter
    Counter = 0
    if Sign == "+" or "x⁻⁻" or "-" or "/" or "*":
        Calculated_Number = ops[Sign](float(Lbl_EnteredNumber['text']), float(Ent_EnterNumber.get()))
    elif Sign == "²√":
        if Ent_EnterNumber.get() != "":
            Calculated_Number = ops[Sign](float(Ent_EnterNumber.get()))
        elif Lbl_EnteredNumber['text'] != "0":
            Calculated_Number = ops[Sign](float(Lbl_EnteredNumber['text']))
    Lbl_EnteredNumber['text'] = str(Calculated_Number)
    Ent_EnterNumber.delete(0, tk.END)

def BackSpace():
    Ent_EnterNumber.delete(len(Ent_EnterNumber.get())-1)

def On_Sqrt_Click():
    global Calculated_Number
    if Ent_EnterNumber.get() != "":
        Lbl_EnteredNumber['text'] = Ent_EnterNumber.get()
        Calculated_Number = ops[Sign](float(Lbl_EnteredNumber['text']))
        Lbl_EnteredNumber['text'] = str(Calculated_Number)
        Ent_EnterNumber.delete(0, tk.END)
    else:
        Calculated_Number = ops[Sign](float(Lbl_EnteredNumber['text']))
        Lbl_EnteredNumber['text'] = str(Calculated_Number)
        Ent_EnterNumber.delete(0, tk.END)


#----------------------------------------------------------------------------------------------------------
Window = tk.Tk()
Window.title("Simple Calculator")
Window.rowconfigure(0, minsize=50, weight=2)
Window.rowconfigure(1, minsize=200, weight=2)
Window.columnconfigure(0, minsize=300, weight=2)
#----------------------------------------------------------------------------------------------------------

frm_Entry = tk.Frame(master=Window, relief=tk.GROOVE)
frm_Entry.grid(row=0, column=0)

frm_ForBtn = tk.Frame(master=Window, borderwidth=5)
frm_ForBtn.grid(row=1, column=0, sticky='nsew')
frm_ForBtn.rowconfigure([0], minsize=100, weight=2)
frm_ForBtn.columnconfigure([0, 1], minsize=100, weight=2)

frm_NumberBtn = tk.Frame(master=frm_ForBtn, bg="Light Blue")
frm_NumberBtn.grid(row=0, column=0, sticky='nsew')
frm_NumberBtn.rowconfigure([0, 1, 2, 3], minsize=75, weight=2)
frm_NumberBtn.columnconfigure([0, 1, 2], minsize=50, weight=2)

frm_SymbolBtn = tk.Frame(master=frm_ForBtn, bg="Dark Blue")
frm_SymbolBtn.grid(row=0, column=1, sticky='nsew')
frm_SymbolBtn.rowconfigure([0, 1, 2, 3], minsize=75, weight=2)
frm_SymbolBtn.columnconfigure([0, 1], minsize=50, weight=2)

#----------------------------------------------------------------------------------------------------------
Lbl_Sign = tk.Label(master=frm_Entry, text="", fg='grey')
Lbl_Sign.grid(row=0, column=2)

Lbl_EnteredNumber = tk.Label(text="0", master=frm_Entry)
Lbl_EnteredNumber.grid(row=0, column=1, sticky='nw')

Ent_EnterNumber = tk.Entry(master=frm_Entry, bg="White", width=50)
Ent_EnterNumber.grid(row=1, column=1, sticky='nsew')
#----------------------------------------------------------------------------------------------------------
Btn_1 = tk.Button(master=frm_NumberBtn, text="1", bg="White", width=7, height=2, command=lambda: number_inserter('1'))
Btn_1.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

Btn_2 = tk.Button(master=frm_NumberBtn, text="2", bg="White", width=7, height=2, command=lambda: number_inserter('2'))
Btn_2.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

Btn_3 = tk.Button(master=frm_NumberBtn, text="3", bg="White", width=7, height=2, command=lambda: number_inserter('3'))
Btn_3.grid(row=0, column=2, padx=5, pady=5, sticky='nsew')

Btn_4 = tk.Button(master=frm_NumberBtn, text="4", bg="White", width=7, height=2, command=lambda: number_inserter('4'))
Btn_4.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

Btn_5 = tk.Button(master=frm_NumberBtn, text="5", bg="White", width=7, height=2, command=lambda: number_inserter('5'))
Btn_5.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')

Btn_6 = tk.Button(master=frm_NumberBtn, text="6", bg="White", width=7, height=2, command=lambda: number_inserter('6'))
Btn_6.grid(row=1, column=2, padx=5, pady=5, sticky='nsew')

Btn_7 = tk.Button(master=frm_NumberBtn, text="7", bg="White", width=7, height=2, command=lambda: number_inserter('7'))
Btn_7.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')

Btn_8 = tk.Button(master=frm_NumberBtn, text="8", bg="White", width=7, height=2, command=lambda: number_inserter('8'))
Btn_8.grid(row=2, column=1, padx=5, pady=5, sticky='nsew')

Btn_9 = tk.Button(master=frm_NumberBtn, text="9", bg="White", width=7, height=2, command=lambda: number_inserter('9'))
Btn_9.grid(row=2, column=2, padx=5, pady=5, sticky='nsew')

Btn_0 = tk.Button(master=frm_NumberBtn, text="0", bg="White", width=7, height=2, command=lambda: number_inserter('0'))
Btn_0.grid(row=3, column=1, padx=5, pady=5, sticky='nsew')
#---------------------------------------------------------------------------------------------------------
Btn_BackSpace = tk.Button(master=frm_NumberBtn, text="⇦", width=7, height=2, command=BackSpace)
Btn_BackSpace.grid(row=3, column=2,  padx=5, pady=5, sticky='nsew')

Btn_Point = tk.Button(master=frm_NumberBtn, text=".", width=7, height=2, command=lambda: number_inserter('.'))
Btn_Point.grid(row=3, column=0,  padx=5, pady=5, sticky='nsew')
#---------------------------------------------------------------------------------------------------------
Btn_Add = tk.Button(master=frm_SymbolBtn, text='+', width=5, height=4, bg='grey',
                    command=lambda: [Change_Sign('+'), On_Symbol_Click(float(Lbl_EnteredNumber['text']))])
Btn_Add.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

Btn_Multiply = tk.Button(master=frm_SymbolBtn, text='*', width=5, height=4, bg='grey',
                         command=lambda: [Change_Sign('*'), On_Symbol_Click(float(Lbl_EnteredNumber['text']))])
Btn_Multiply.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

Btn_Divide = tk.Button(master=frm_SymbolBtn, text='/', width=5, height=4, bg='grey',
                       command=lambda: [Change_Sign('/'), On_Symbol_Click(float(Lbl_EnteredNumber['text']))])
Btn_Divide.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

Btn_Subtract = tk.Button(master=frm_SymbolBtn, text='-', width=5, height=4, bg='grey',
                         command=lambda: [Change_Sign('-'), On_Symbol_Click(float(Lbl_EnteredNumber['text']))])
Btn_Subtract.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')

Btn_Power = tk.Button(master=frm_SymbolBtn, text='x⁻⁻', width=5, height=4, bg='grey',
                      command=lambda: [Change_Sign('x⁻⁻'), On_Symbol_Click(float(Lbl_EnteredNumber['text']))])
Btn_Power.grid(row=2, column=1, padx=5, pady=5, sticky='nsew')

Btn_Root = tk.Button(master=frm_SymbolBtn, text='²√', width=5, height=4, bg='grey',
                     command=lambda: [Change_Sign('²√'), On_Sqrt_Click()])
Btn_Root.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')

Btn_C = tk.Button(master=frm_SymbolBtn, text='C', width=5, height=4, bg='grey',
                  command=Clear)
Btn_C.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')

Btn_Equal = tk.Button(master=frm_SymbolBtn, text='=', width=5, height=4, bg='grey',
                      command=Equals)
Btn_Equal.grid(row=3, column=1, padx=5, pady=5, sticky='nsew')
#---------------------------------------------------------------------------------------------------------
Window.mainloop()
