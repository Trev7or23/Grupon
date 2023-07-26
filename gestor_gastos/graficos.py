import tkinter as tk
import tkinter.messagebox as mgx
import pandas as pd

df = pd.read_csv("datos.csv")

ventana = tk.Tk()
ventana.geometry("300x200")
ventana.title("gestor de gastos")

def boton_click():
    print("boton clickeado")
    dinero = tk_dinero.get()
    categoria = tk_categoria.get()
    if "," in dinero:
        mgx.showerror("Error", "no puede poner ',' en 'dinero' reemplazelo por '.'")
        return 
    
    if dinero.isnumeric():
        if categoria == "":
            mgx.showerror("Error", "Debes poner alguna categoria para identificar el gasto")
            return
        dinero = float(dinero)
        mes = tk_mes.get()
        dia = tk_dia.get()
        categoria = tk_categoria.get()
        
        datos = {"dia": [f"{dia}"],
                 "mes": [f"{mes}"],
                 "dinero": [f"{dinero}"],
                 "categoria": [f"{categoria}"]}
        datos = pd.DataFrame(datos)
        global df
        df = pd.concat([df, datos])
        df.to_csv("datos.csv")
        mgx.showinfo("Success", "Los datos han sido agregados con exito")
    else:
        mgx.showerror("Error", "debes poner un numero en la pestaña 'dinero'")
        
tk_mes = tk.Spinbox(ventana, from_=1, to=12)
tk_dinero = tk.Entry(ventana)
tk_categoria = tk.Entry(ventana)
tk_boton = tk.Button(ventana, text="guardar", command=boton_click)

tk.Label(ventana, text="mes: ").pack()
tk_mes.pack()
tk.Label(ventana, text="dia: ").pack()
tk_dia = tk.Spinbox(ventana, from_=1, to=29 if tk_mes == 2 else 31)
tk_dia.pack()
tk.Label(ventana, text="dinero: ").pack()
tk_dinero.pack()
tk.Label(ventana, text="categoria: ").pack()
tk_categoria.pack()
tk_boton.pack()

ventana.mainloop()