import tkinter as tk

window = tk.Tk()
window.geometry("500x300")
window.title("Parâmetros do robô")
iddaplanilha = tk.Label(text="ID da planilha de base: ")
localfirefox = tk.Label(text="Local do Firefox: ")
pausaparaacompanhamento = tk.Label(text="Pausa para acompanhamento: ")
iddaplanilhaentry = tk.Entry()
localfirefoxentry = tk.Entry()
pausaparaacompanhamentoentry = tk.Entry()
iddaplanilha.pack()
localfirefox.pack()
pausaparaacompanhamento.pack()
iddaplanilhaentry.pack()
localfirefoxentry.pack()
pausaparaacompanhamentoentry.pack()

window.mainloop()