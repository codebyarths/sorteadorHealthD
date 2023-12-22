import os
import sys
import tkinter as tk
from tkinter import messagebox  # Importando especificamente a função messagebox
import random

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def sortear_com_contagem():
    resultado.pack_forget()  # Remover o resultado anterior, se estiver sendo exibido
    try:
        def atualizar_contagem(segundos):
            if segundos > 0:
                contagem.config(text=f"Contagem: {segundos}", fg="#000", font=("Arial", 40, "bold"))
                root.after(1000, lambda: atualizar_contagem(segundos - 1))
            else:
                numero_sorteado = random.randint(1, 824)
                resultado.config(text=f"O número sorteado é: {numero_sorteado}", fg="#000", font=("Arial", 30, "bold"))
                resultado.pack(pady=20)  # Posicionamento com espaço menor
                contagem.pack_forget()  # Remover a contagem

        contagem.pack(pady=10)
        atualizar_contagem(5)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

img_path = resource_path("logo_samel.png")

root = tk.Tk()
bgimg = tk.PhotoImage(file=img_path)

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

resultado = tk.Label(root, font=("Arial", 30, "bold"), fg="#000", anchor="n")
sortear_button = tk.Button(root, text="Sortear", command=sortear_com_contagem, font=fonte_sortear, bg=cor_botao, fg=cor_botao_texto, relief=tk.RAISED)
sortear_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

root.mainloop()
