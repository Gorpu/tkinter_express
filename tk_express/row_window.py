import tkinter as tk
from tk_express import TkExpress as tkes


# Cria a janela
root = tk.Tk()
root.geometry("500x300")

# Cria instâncias dos labels
row_labels = [
    tkes.TextLabel(context=root, title="R1"),
    tkes.TextLabel(context=root, title="R2"),
    tkes.TextLabel(context=root, title="R3"),
]

col_labels = [
    tkes.TextLabel(context=root, title="C1"),
    tkes.TextLabel(context=root, title="C2"),
    tkes.TextLabel(context=root, title="C3"),
]

# Organiza os labels
tkes.Grid_Components(root, row_labels, start_row=0, start_column=0, horizontal=True)   # linha
tkes.Grid_Components(root, col_labels, start_row=1, start_column=1, horizontal=False)  # coluna

root.mainloop()
