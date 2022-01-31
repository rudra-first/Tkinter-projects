from tkinter import *

Number_Dict = {'Binary': bin,
               'Decimal': int,
               'Hexa-Decimal': hex,
               'Octal': oct}
Base_Dict = {'Binary': 2,
             'Hexa-Decimal': 16,
             'Decimal': 10,
             'Octal': 8}
#--------------------------------------------------------------------------------------------------------
def Change_Label_Name(Lbl, Btn):
    Lbl['text'] = Btn['text']

def ConversionFrom():
    Lbl_ToText['text'] = 'Converted Number'

def ConversionTo():
    if Lbl_ConvertFrom['text'] != '*':
        SystemFrom = Lbl_ConvertFrom['text']
        SystemTo = Lbl_ConvertTo['text']
        Entered_Number = int(Ent_FromEntry.get(), Base_Dict[SystemFrom])
        if SystemTo != 'Decimal':
            ConvertedNumber = Number_Dict[SystemTo](Entered_Number)
            Lbl_ToText['text'] = ConvertedNumber[2:len(ConvertedNumber)]
        else:
            Lbl_ToText['text'] = Number_Dict[SystemTo](Entered_Number)

            
#--------------------------------------------------------------------------------------------------------
window = Tk()
window.columnconfigure(0, minsize=400, weight=2)
window.rowconfigure([0, 1, 2], minsize=150, weight=2)
#--------------------------------------------------------------------------------------------------------
Frm_From = Frame(window)
Frm_FromButton = Frame(Frm_From)
Frm_FromEntry = Frame(Frm_From)
Frm_From.grid(row=0, column=0, sticky='nsew')
Frm_FromButton.grid(row=0, column=0, sticky='nsew')
Frm_FromEntry.grid(row=1, column=0, sticky='nsew')


Frm_From.columnconfigure(0, minsize=90, weight=2)
Frm_From.rowconfigure([0, 1], minsize=50, weight=2)

Frm_FromButton.columnconfigure([0, 1, 2, 3], minsize=75, weight=2)
Frm_FromButton.rowconfigure(0, minsize=30, weight=2)

Frm_FromEntry.columnconfigure(0, minsize=75, weight=2)
Frm_FromEntry.rowconfigure([0, 1], minsize=30, weight=2)
#--------------------------------------------------------------------------------------------------------

Frm_To = Frame(window)
Frm_ToButton = Frame(Frm_To)
Frm_ToEntry = Frame(Frm_To)
Frm_To.grid(row=2, column=0, sticky='nsew')
Frm_ToButton.grid(row=0, column=0, sticky='nsew')
Frm_ToEntry.grid(row=1, column=0, sticky='nsew')


Frm_To.columnconfigure(0, minsize=90, weight=2)
Frm_To.rowconfigure([0, 1], minsize=50, weight=2)

Frm_ToButton.columnconfigure([0, 1, 2, 3], minsize=75, weight=2)
Frm_ToButton.rowconfigure(0, minsize=30, weight=2)

Frm_ToEntry.columnconfigure(0, minsize=75, weight=2)
Frm_ToEntry.rowconfigure([0, 1], minsize=30, weight=2)
#--------------------------------------------------------------------------------------------------------
Lbl_ConvertArrow = Label(window, text='⇓')
Lbl_ConvertArrow.grid(row=1, column=0, sticky='nsew')
#--------------------------------------------------------------------------------------------------------
#ConvertFrom
Btn_FromBin = Button(Frm_FromButton, text='Binary', width=10, bg='white',
                     command=lambda: [Change_Label_Name(Lbl_ConvertFrom, Btn_FromBin), ConversionFrom()])
Btn_FromHexa = Button(Frm_FromButton, text='Hexa-Decimal', width=10, bg='white',
                      command=lambda: [Change_Label_Name(Lbl_ConvertFrom, Btn_FromHexa), ConversionFrom()])
Btn_FromOct = Button(Frm_FromButton, text='Octal', width=10, bg='white',
                     command=lambda: [Change_Label_Name(Lbl_ConvertFrom, Btn_FromOct), ConversionFrom()])
Btn_FromDeci = Button(Frm_FromButton, text='Decimal', width=10, bg='white',
                      command=lambda: [Change_Label_Name(Lbl_ConvertFrom, Btn_FromDeci), ConversionFrom()])

Lbl_ConvertFrom = Label(Frm_FromEntry, text='*')
Ent_FromEntry = Entry(Frm_FromEntry)

Btn_FromBin.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
Btn_FromHexa.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
Btn_FromOct.grid(row=0, column=2, sticky='nsew', padx=5, pady=5)
Btn_FromDeci.grid(row=0, column=3, sticky='nsew', padx=5, pady=5)

Lbl_ConvertFrom.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
Ent_FromEntry.grid(row=1, column=0, sticky='nsew', padx=15, pady=15)
#--------------------------------------------------------------------------------------------------------
#ConvertTo
Btn_ToBin = Button(Frm_ToButton, text='Binary', width=10, bg='white',
                   command=lambda: [Change_Label_Name(Lbl_ConvertTo, Btn_ToBin), ConversionTo()])
Btn_ToHexa = Button(Frm_ToButton, text='Hexa-Decimal', width=10, bg='white',
                    command=lambda: [Change_Label_Name(Lbl_ConvertTo, Btn_ToHexa), ConversionTo()])
Btn_ToOct = Button(Frm_ToButton, text='Octal', width=10, bg='white',
                   command=lambda: [Change_Label_Name(Lbl_ConvertTo, Btn_ToOct), ConversionTo()])
Btn_ToDeci = Button(Frm_ToButton, text='Decimal', width=10, bg='white',
                    command=lambda: [Change_Label_Name(Lbl_ConvertTo, Btn_ToDeci), ConversionTo()])

Lbl_ConvertTo = Label(Frm_ToEntry, text='*')
Lbl_ToText = Label(Frm_ToEntry, text='Converted Number')

Btn_ToBin.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
Btn_ToHexa.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
Btn_ToOct.grid(row=0, column=2, sticky='nsew', padx=5, pady=5)
Btn_ToDeci.grid(row=0, column=3, sticky='nsew', padx=5, pady=5)

Lbl_ConvertTo.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
Lbl_ToText.grid(row=1, column=0, sticky='nsew', padx=15, pady=15)
#--------------------------------------------------------------------------------------------------------
window.mainloop()