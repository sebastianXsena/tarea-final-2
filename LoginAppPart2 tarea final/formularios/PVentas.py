import json
import tkinter as tk
import webbrowser
from tkinter import messagebox, ttk

from PIL import Image, ImageTk

import util.generic as utl


class PVentas(tk.Tk):        
    def __init__(self, name="", username="", email=""):
        self.name = name
        self.username = username
        self.email = email
        self.tipo_action ="Guardar"
        self.tipo_user = ""
        super().__init__()
        self.title("Panel Administrativo")
        self.resizable(False, False)
        # Obtener las dimensiones de la pantalla
        self.ancho_pantalla = self.winfo_screenwidth() #método para obtener Ancho
        self.alto_pantalla = self.winfo_screenheight() #método para obtener Alto

        # Establecer el tamaño completo de la ventana
        self.geometry(f"{self.ancho_pantalla}x{self.alto_pantalla}")
        
        menubar = tk.Menu(self)                  
        menuuser = tk.Menu(menubar, tearoff=0)
        menuuser.add_command(label="Administracion de Clientes", command=self.main_clientes)  
        menubar.add_cascade(label="Clientes", menu=menuuser)
        
        menuuser = tk.Menu(menubar, tearoff=0)
        menuuser.add_command(label="Administracion de Categorias", command=self.main_categorias)  
        menubar.add_cascade(label="Categorias", menu=menuuser)
        
        menuuser = tk.Menu(menubar, tearoff=0)
        menuuser.add_command(label="Administracion de Productos", command=self.main_productos)  
        menubar.add_cascade(label="Productos", menu=menuuser)
        
        menuuser = tk.Menu(menubar, tearoff=0)
        menuuser.add_command(label="Administracion de Ventas", command=self.main_ventas)  
        menubar.add_cascade(label="Ventas", menu=menuuser)
        self.config(menu=menubar)
        
        self.user_ifo = tk.Label(self, bd=0, relief=tk.SOLID, width=200)
        self.user_ifo.pack(side=tk.LEFT, fill="y")
        titulo = tk.Label(self.user_ifo, text="PANEL ADMINISTRATIVO", font=("Arial", 25))
        titulo.pack(padx=20, pady=4)
        
        self.userimg = utl.leer_imagen(r"C:\\Users\\Biblioteca\\Desktop\\LoginAppPart2\\userinfo.png",(128,128))
        self.imgfacebook = utl.leer_imagen(r"C:\\Users\\Biblioteca\\Desktop\\LoginAppPart2\\face.png",(128,128))
        self.imglinkedin = utl.leer_imagen(r"C:\\Users\\Biblioteca\\Desktop\\LoginAppPart2\\linkedin.png",(128,128))
        self.imgwebsite = utl.leer_imagen(r"C:\\Users\\Biblioteca\\Desktop\\LoginAppPart2\\website.png",(128,128))
        self.imglogout = utl.leer_imagen(r"C:\\Users\\Biblioteca\\Desktop\\LoginAppPart2\\logout.png",(128,128))
        
        tk.Label(self.user_ifo, image=self.userimg).pack(padx=30, pady=4)
        tk.Label(self.user_ifo, image=self.name, font=('arial',15)).pack(padx=30, pady=4)
        tk.Label(self.user_ifo, image=self.email, font=('arial',12)).pack(padx=30, pady=4)
        
    
    def main_usuarios(self):
        pass

    def main_clientes(self):
        pass

    def main_categorias(self):
        pass

    def main_productos(self):
        pass

    def main_ventas(self):
        pass