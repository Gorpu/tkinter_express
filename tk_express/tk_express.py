import tkinter as tk
import os, sys


## mesclar ao binario
def add_bin(path: str) -> str:
    """
    Retorna o caminho correto para recursos (imagens, ícones) 
    quando executado como script ou como exe PyInstaller.
    """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, path)

class TkExpress():
    def __init__(self):
        pass
    
    class TextLabel():
        def __init__(self, context: tk.Tk, title="", row=0, column=0, color_bg="#ffffff"):
            self.context = context
            self.labelComp = tk.Label(
            self.context, 
            bg=color_bg, 
            fg="#000000",
            text=title)
            self.labelComp.grid(row=row, column=column)
    
    class CheckBox():
        def __init__(self):
            pass
    
        def call(context: tk.Tk, title: str,row: int, column:int, value: tk.BooleanVar, color_bg="#FFFFFF"):
            def pressed():
                print(value.get())

            checkbox = tk.Checkbutton(
                context,
                text=title, 
                variable=value,
                offvalue=0,
                bg=color_bg,
                command=pressed)
            checkbox.grid(row=row, column=column)
            return value
        
    class InputText():
        def __init__(self, context: tk.Tk, width:int, row: int, column:int, size_return=25):
            # Função de validação: permite digitar até 20 caracteres
            def limitar_caracteres(texto):
                return len(texto) <= size_return

            # Registra a função de validação no Tkinter
            validar = context.register(limitar_caracteres)

            # Cria o campo de entrada com validação
            input_text = tk.Entry(context, width=width, validate="key",validatecommand=(validar, "%P"))
            input_text.grid(row=row, column=column)
            return input_text
    
    class ActionButton():
        def __init__(self, context: tk.Tk, text: str, command: callable, row: int, column: int):
            action_button = tk.Button(context, text=text, command=command)
            action_button.grid(row=row, column=column)
        
    class Dialog():
        def __init__(self, mensage: str, title="Alert", dialog_error=False,geometry="250x120", resizable=False, command=None, button_title="Ok"):
            icon_win = add_bin("tk_express/assets/erro_icon_win.ico")  if dialog_error else add_bin("domain/lib/tkExpress/assets/sucess_icon_win.ico")
        
            dialog_comp = tk.Tk()
            dialog_comp.title(title)
            dialog_comp.iconbitmap(icon_win)
            dialog_comp.geometry(geometry)
            dialog_comp.resizable(width=resizable, height=resizable)

            dialog_comp.grid_columnconfigure(0, weight=1)
            dialog_comp.grid_rowconfigure(0, weight=1)
            dialog_comp.grid_rowconfigure(1, weight=1)

            label = tk.Label(dialog_comp, text=mensage)
            label.grid(row=0, column=0, sticky="nsew", pady=10)

            if command == None:
                command = dialog_comp.destroy
            TkExpress.ActionButton(dialog_comp, button_title, row=1, column=0, command=command)
            dialog_comp.mainloop()
    
    class Grid_Components():
        def __init__(self, context: tk.Tk, components: list, start_row=0, start_column=0, horizontal=True):
            """
            Organiza uma lista de TextLabel no grid.
            horizontal=True -> coloca em linha
            horizontal=False -> coloca em coluna
            """
            for i, component in enumerate(components):
                if isinstance(component, TkExpress.TextLabel):
                    if horizontal:
                        component.labelComp.grid(row=start_row, column=start_column + i)
                    else:
                        component.labelComp.grid(row=start_row + i, column=start_column)


