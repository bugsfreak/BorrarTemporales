from BorrarTemporales import borrarTemporales
import tkinter as tk
from tkinter import scrolledtext
from threading import Thread


class UI:
    
    def __init__(self,root):
        self.root=root
        root.title("Limpiador de archivos temporales")
        root.geometry("600x400")
        
        self.boton = tk.Button(root, text="Borrar temporales", command=self.iniciar_borrado, bg="#3c7fb1", fg="white", font=("Segoe UI", 12))
        self.boton.pack(pady=10,padx=10)
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, font=("Consolas", 10))
        self.text_area.pack(padx=10, pady=10)
    
    def log(self,mensaje):
        self.text_area.insert(tk.END, mensaje + "\n")
        self.text_area.see(tk.END)
    
    def iniciar_borrado(self):
        self.boton.config(state=tk.DISABLED)
        Thread(target=self.ejecutar_borrado).start()
        
    def ejecutar_borrado(self):
        borrarTemporales(logger=self.log)
        self.log("\nLimpieza completada.")
        self.boton.config(state=tk.NORMAL)
    
    
if __name__ == "__main__":
    root = tk.Tk()
    app = UI(root)
    root.mainloop()