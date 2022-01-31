import tkinter as tk
#-----------------------------------------------------------------------------------------------------
#Functions
#Function for Unit label
def set_Fahrenheit_label():
    Lbl_Temp_Unit["text"] = Btn_Fahrenheit['text']

def set_Celsius_label():
    Lbl_Temp_Unit["text"] = Btn_Celsius['text']

def Converting_Temp():
    Entered_Temp = int(Ent_Inp_Temp.get())
    if Lbl_Temp_Unit['text'] == Btn_Fahrenheit['text']:
        Out_Temp = (Entered_Temp - 32) * 5 / 9
        Lbl_Out_Temp['text'] = f'{Out_Temp}'
    elif Lbl_Temp_Unit['text'] == Btn_Celsius['text']:
        Out_Temp = Entered_Temp * 9/5 + 32
        Lbl_Out_Temp['text'] = f'{Out_Temp}'


#-----------------------------------------------------------------------------------------------------
Window = tk.Tk()

Window.columnconfigure([0, 1, 2, 3, 4], weight=1, minsize=20)
Window.rowconfigure(0, weight=1, minsize=20)
#-----------------------------------------------------------------------------------------------------
#Frames:
Frame1 = tk.Frame(master=Window, borderwidth=5, bg="Black")
Frame1.grid(row=0, column=1)

Frame2 = tk.Frame(master=Window, relief=tk.GROOVE)
Frame2.grid(row=0, column=3)

Frame3 = tk.Frame(master=Window, bg="Black")
Frame3.grid(row=0, column=4)
#-----------------------------------------------------------------------------------------------------
#widgets:

Lbl_Input_Temp = tk.Label(text="Input Temperature-->", fg="white", bg="black")
Lbl_Input_Temp.grid(row=0, column=0, padx=10)

Ent_Inp_Temp = tk.Entry(master=Frame1)
Ent_Inp_Temp.grid(sticky="nsew")

Lbl_Temp_Unit = tk.Label(text="*")
Lbl_Temp_Unit.grid(row=0, column=2)

Btn_Fahrenheit = tk.Button(master=Frame2, text="°F", command=set_Fahrenheit_label)
Btn_Fahrenheit.grid(padx=5, pady=5)

Btn_Celsius = tk.Button(master=Frame2, text="°C", command=set_Celsius_label)
Btn_Celsius.grid(padx=5, pady=5)

Btn_Convert = tk.Button(master=Frame3, text="-->", command=Converting_Temp)
Btn_Convert.grid(padx=10, pady=10)

Lbl_Out_Temp = tk.Label(text=f"")
Lbl_Out_Temp.grid(row=0, column=5)
#-----------------------------------------------------------------------------------------------------
Window.mainloop()
