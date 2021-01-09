import tkinter

window = tkinter.Tk()
window.minsize(width=250, height=25)
window.config(padx=20, pady=10)

def button_on_click():
    value = int(int(textbox.get()) * 1.60934)
    label3.config(text=value)


textbox = tkinter.Entry(width=10)
textbox.grid(row=0, column=1)

label1 = tkinter.Label(text="Miles")
label1.grid(row=0,column=2)

label2 = tkinter.Label(text="is equal to")
label2.grid(row=1,column=0)

label3 = tkinter.Label(text="0")
label3.grid(row=1,column=1)

label4 = tkinter.Label(text="Km")
label4.grid(row=1,column=2)

button = tkinter.Button(text="Calculate", command=button_on_click)
button.grid(row=2, column=1)
window.mainloop()