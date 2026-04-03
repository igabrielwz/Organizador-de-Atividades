from tkinter import *
from tkinter import ttk, messagebox

tarefas = []

def adicionar_tarefa():
    tarefa = entrada.get()
    if tarefa == "":
        messagebox.showwarning("Aviso", "Digite uma tarefa!")
    else:
        tarefas.append(tarefa)
        atualizar_lista()
        entrada.delete(0, END)

def excluir_tarefa():
    try:
        selecionada = lista.curselection()[0]
        tarefas.pop(selecionada)
        atualizar_lista()
    except:
        messagebox.showwarning("Aviso", "Selecione uma tarefa!")

def concluir_tarefa():
    try:
        selecionada = lista.curselection()[0]
        if "✔" in tarefas[selecionada]:
            messagebox.showinfo("Aviso", "Essa tarefa já foi concluída!")
        else:
            tarefas[selecionada] += " ✔"
            atualizar_lista()
    except:
        messagebox.showwarning("Aviso", "Selecione uma tarefa!")

def atualizar_lista():
    lista.delete(0, END)
    for tarefa in tarefas:
        lista.insert(END, tarefa)

root = Tk()
root.title("📚 Organizador de Atividades")
root.geometry("420x450")
root.configure(bg="#1e1e2f")

try:
    root.iconbitmap("livro_novo.ico")
except:
    pass

try:
    icone = PhotoImage(file="livro.png")
    root.iconphoto(True, icone)
except:
    pass


style = ttk.Style()
style.theme_use("clam")

style.configure("TButton",
    font=("Segoe UI", 10),
    padding=6)

style.configure("TLabel",
    background="#1e1e2f",
    foreground="white",
    font=("Segoe UI", 12))

frame = Frame(root, bg="#1e1e2f")
frame.pack(pady=15)

titulo = Label(frame, text="📚 Organizador de Atividades",
    font=("Segoe UI", 16, "bold"),
    bg="#1e1e2f", fg="white")
titulo.pack(pady=10)

entrada = Entry(frame, width=30, font=("Segoe UI", 11))
entrada.pack(pady=10)

btn_frame = Frame(frame, bg="#1e1e2f")
btn_frame.pack(pady=5)

ttk.Button(btn_frame, text="Adicionar", command=adicionar_tarefa).grid(row=0, column=0, padx=5)
ttk.Button(btn_frame, text="Concluir", command=concluir_tarefa).grid(row=0, column=1, padx=5)
ttk.Button(btn_frame, text="Excluir", command=excluir_tarefa).grid(row=0, column=2, padx=5)

lista = Listbox(frame, width=40, height=12,
   font=("Segoe UI", 10),
   bg="#2b2b3c",
   fg="white",
   selectbackground="#4a90e2")
lista.pack(pady=15)

root.mainloop()