from tkinter import*
from tkinter import ttk
import speech_recognition as sr
root = Tk()
root.geometry("500x500")
root.config(bg = '#F2CCC3')

label = Label(root, text = "LANGUAGE TRANCELATER", font = 'areal 20', bg = '#e3fc03')
label.place(relx = 0.5, rely = 0.1, anchor =CENTER)

input_label = Label(root, text = "Enter Text", bg = '#F2CCC3', font = 'areal 15')
input_label.place(relx = 0.03, rely = 0.3, anchor =W)

output_label = Label(root, text = "Output", bg = '#F2CCC3', font = 'areal 15')
output_label.place(relx = 0.6, rely = 0.3, anchor =W)

input_text = Text(root,width = 60, height = 15, wrap = WORD, pady=5, padx = 5)
input_text.place(relx = 0.02, rely = 0.5, anchor = W)

output_text = Text(root,width = 60, height = 15, wrap = WORD, pady=5, padx = 5)
output_text.place(relx = 0.6, rely = 0.5, anchor = W)

translate = Button(root, text = "Translate", bg='#03e8fc', font = 'areal 15')
translate.place(relx = 0.5, rely = 0.8, anchor = CENTER)

lano_list = ["English","Hindi","Japanese"]
lano_dropdown = ttk.Combobox(root,state = "readonly",values = lano_list, justify ="right")
lano_dropdown.place(relx = 0.1, rely = 0.3, anchor =W)

lani_list = ["English","Hindi","Japanese"]
lani_dropdown = ttk.Combobox(root,state = "readonly",values = lani_list, justify ="right")
lani_dropdown.place(relx = 0.75, rely = 0.3, anchor =E)





root.mainloop()