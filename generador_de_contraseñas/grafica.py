import random
import tkinter as tk

def generar_password():
    longitud = int(longitud_entry.get())
    mayusculas = True if mayusculas_var.get() == 1 else False
    numeros = True if numeros_var.get() == 1 else False
    simbolos = True if simbolos_var.get() == 1 else False
    caracteres_permitidos = caracteres(mayusculas, numeros, simbolos)
    password = password_generador(caracteres_permitidos, longitud)
    password_label.config(text=password)

def longitud():
    longitud = 0
    while longitud < 8 or longitud > 16:
        longitud = int(input("elija una longitud de 8 a 16 "))
    return longitud

def caracteres(mayusculas, numeros, simbolos):
    caracteres = "abcdefghijklmnopqrstuvwxyz"
    if mayusculas:
        caracteres += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if numeros:
        caracteres += "0123456789"
    if simbolos:
        caracteres += "!@#$%^&*()_+{}[]<>?/\\|-="

    return caracteres

def password_generador(caracteres_permitidos, longitud):
    password = ""
    for i in range(longitud):
        rd = random.randint(0, len(caracteres_permitidos) - 1)
        password += caracteres_permitidos[rd]
    return password

# Crear ventana
ventana = tk.Tk()
ventana.title("Generador de contraseñas")
ventana.geometry("400x300")

# Crear entrada de longitud
longitud_label = tk.Label(ventana, text="Longitud:")
longitud_label.pack()
longitud_entry = tk.Entry(ventana)
longitud_entry.pack()

# Crear opciones
opciones_frame = tk.Frame(ventana)
opciones_frame.pack()

mayusculas_var = tk.IntVar()
mayusculas_checkbutton = tk.Checkbutton(opciones_frame, text="Mayúsculas", variable=mayusculas_var)
mayusculas_checkbutton.pack(side="left")

numeros_var = tk.IntVar()
numeros_checkbutton = tk.Checkbutton(opciones_frame, text="Números", variable=numeros_var)
numeros_checkbutton.pack(side="left")

simbolos_var = tk.IntVar()
simbolos_checkbutton = tk.Checkbutton(opciones_frame, text="Símbolos", variable=simbolos_var)
simbolos_checkbutton.pack(side="left")

# Crear botón para generar contraseña
generar_button = tk.Button(ventana, text="Generar contraseña", command=generar_password)
generar_button.pack()

# Crear etiqueta para mostrar la contraseña generada
password_label = tk.Label(ventana, text="")
password_label.pack()

ventana.mainloop()