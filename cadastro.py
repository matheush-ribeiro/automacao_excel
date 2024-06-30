from tkinter import *

janela = Tk()
janela.geometry("300x300")
janela.title("CADASTRO")

label = Label (janela, text = "Item 1", font="bold", foreground="green", background="black")
label.grid (column = 0, row = 0)

entrada = Entry (janela, width=10, font="bold", foreground="green", background="black")
entrada.grid(column=1, row=0)

label2 = Label (janela, text = "Item 2", font="bold", foreground="green", background="black")
label2.grid (column=0, row=2)

entrada2 = Entry (janela, width=10, font="bold", foreground="green", background="black")
entrada2.grid(column=1, row=2)

label3 = Label (janela, text = "Item 3", font="bold", foreground="green", background="black")
label3.grid (column=0, row=3)

entrada3 = Entry (janela, width=10, font="bold", foreground="green", background="black")
entrada3.grid (column=1, row=3)

label4 = Label (janela, text = "Item 4", font="bold", foreground="green", background="black")
label4.grid (column=0, row=4)

entrada4 = Entry (janela, width=10, font="bold", foreground="green", background="black")
entrada4.grid (column=1, row=4)

janela.configure(background="black")

btn = Button (janela, text="CADASTRAR", width=10, padx=20, font="bold", background="black", foreground="green")
btn.grid (column=1, row=5)

janela.mainloop()