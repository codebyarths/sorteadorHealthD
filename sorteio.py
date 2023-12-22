import tkinter as tk
from tkinter import messagebox
import random


def sortear_com_contagem():
    def mostrar_numero(numero_sorteado):
        messagebox.showinfo("Sorteado é:", f'O número sorteado é: {numero_sorteado}')

    try:
        def atualizar_contagem(segundos):
            if segundos > 0:
                contagem.config(text=f"Contagem: {segundos}", fg="#000")
                root.after(1000, lambda: atualizar_contagem(segundos - 1))
            else:
                numero_sorteado = random.randint(1, 824) 
                mostrar_numero(numero_sorteado)
                contagem.pack_forget()

        contagem.pack(pady=10)
        atualizar_contagem(5)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")


def centralizar(widget):
    widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root = tk.Tk()
bgimg = tk.PhotoImage(file="logo_samel.png")

limg = tk.Label(root, image=bgimg)
limg.place(x=0, y=0, relwidth=1, relheight=1)

root.title("Sorteador")
root.geometry("700x500")
root.configure(bg="#fff")

fonte = ("Arial", 24)
fonte_sortear =("Arial", 14)
cor_texto = "#000"
cor_botao = "#246147"
cor_botao_texto = "white"

contagem = tk.Label(root, text="Contagem: ", font=fonte, fg=cor_texto)
contagem.pack(pady=10)

sortear_button = tk.Button(root, text="Sortear", command=sortear_com_contagem, font=fonte_sortear, bg=cor_botao, fg=cor_botao_texto, relief=tk.RAISED)
sortear_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

root.mainloop()
