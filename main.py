import tkinter as tk
from tkinter import ttk

class InterfaceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface Interativa")
        
        # Label principal
        self.label_instrucao = ttk.Label(
            root, 
            text="Pressione qualquer tecla ou clique no botão",
            font=('Arial', 12)
        )
        self.label_instrucao.pack(pady=20)
        
        # Label para exibir a tecla pressionada
        self.label_tecla = ttk.Label(
            root, 
            text="",
            font=('Arial', 14, 'bold')
        )
        self.label_tecla.pack(pady=10)
        
        # Botão
        self.botao = ttk.Button(
            root, 
            text="Clique Aqui",
            command=self.botao_clicado
        )
        self.botao.pack(pady=20)
        
        # Bind do evento de teclado
        self.root.bind('<Key>', self.tecla_pressionada)
    
    def botao_clicado(self):
        print("Botão foi clicado!")
        
    def tecla_pressionada(self, evento):
        self.label_tecla.config(text=f"Tecla pressionada: {evento.char}")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceApp(root)
    root.mainloop()