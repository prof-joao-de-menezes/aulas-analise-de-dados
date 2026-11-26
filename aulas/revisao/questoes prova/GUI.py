# MONTANDO GUI
import tkinter as tk

janela = tk.Tk()
janela.title("JANELA DE EXEMPLO DE UTILIZAÇÃO DE GUI")
janela.geometry("1000x500")

tk.Label(janela, text="Esperado valor de variável").pack(pady=(12, 4))

janela.mainloop()