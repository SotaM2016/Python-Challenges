import tkinter

window = tkinter.Tk()
window.wm_title("Miles to KM Converter")
def convert(event):
    try:
        miles = int(tbox.get())
        km.configure(text="Answer: "+ str(miles*1.6093))
    except ValueError:
        km.configure(text="Please enter a valid decimal!")
    return

label = tkinter.Label(window, text="Miles to Kilometre Converter")
label.pack()
tbox = tkinter.Entry(window)
tbox.bind("<Return>", convert)
tbox.pack()
km = tkinter.Label(window, text="Answer: - Unknown -")
km.pack()
window.mainloop()