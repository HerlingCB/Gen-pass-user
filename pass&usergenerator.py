import tkinter as tk
import string
import random

def generador_contraseña():
    def animar_ruleta():
        nonlocal ruleta_index
        ruleta_frames = ['|', '/', '-', '\\']
        if ruleta_index < len(ruleta_frames):
            ruleta_label.config(text=ruleta_frames[ruleta_index])
            ruleta_index += 1
            ventana_contraseña.after(100, animar_ruleta)
        else:
            # Generar la contraseña
            try:
                longitud = int(entry_longitud.get())
                if longitud < 1:
                    entry_contraseña.config(state='normal')
                    entry_contraseña.delete(0, tk.END)
                    entry_contraseña.insert(0, "Longitud debe ser mayor a 0")
                    entry_contraseña.config(state='readonly')
                    return

                caracteres = string.ascii_letters + string.digits + string.punctuation
                contraseña = "".join(random.choice(caracteres) for i in range(longitud))

                entry_contraseña.config(state='normal')
                entry_contraseña.delete(0, tk.END)
                entry_contraseña.insert(0, contraseña)
                entry_contraseña.config(state='readonly')
                ruleta_label.config(text='Listo!')
            except ValueError:
                entry_contraseña.config(state='normal')
                entry_contraseña.delete(0, tk.END)
                entry_contraseña.insert(0, "Introduce un número válido")
                entry_contraseña.config(state='readonly')

    global ruleta_label
    ruleta_index = 0
    animar_ruleta()

def copiar_contraseña():
    ventana_contraseña.clipboard_clear()
    ventana_contraseña.clipboard_append(entry_contraseña.get())
    ventana_contraseña.update()

def abrir_generador_contraseña():
    global ventana_contraseña, ruleta_label

    ventana_contraseña = tk.Toplevel()
    ventana_contraseña.title("Generador de Contraseñas")
    ventana_contraseña.geometry("400x250")

    # Contraseña
    label_longitud = tk.Label(ventana_contraseña, text="Ingrese el tamaño de la contraseña:")
    label_longitud.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    # Validación para solo números
    validacion_numeros = (ventana_contraseña.register(lambda s: s.isdigit() or s == ""), '%P')
    global entry_longitud
    entry_longitud = tk.Entry(ventana_contraseña, validate='key', validatecommand=validacion_numeros)
    entry_longitud.grid(row=0, column=1, padx=10, pady=10)

    label_contraseña = tk.Label(ventana_contraseña, text="La contraseña es:")
    label_contraseña.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    global entry_contraseña
    entry_contraseña = tk.Entry(ventana_contraseña, width=40)
    entry_contraseña.grid(row=1, column=1, padx=10, pady=10)
    entry_contraseña.config(state='readonly')

    ruleta_label = tk.Label(ventana_contraseña, text='', font=('Courier', 24))
    ruleta_label.grid(row=2, column=1, padx=10, pady=10)

    boton_generar_contraseña = tk.Button(ventana_contraseña, text="Generar Contraseña", command=generador_contraseña)
    boton_generar_contraseña.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    boton_copiar_contraseña = tk.Button(ventana_contraseña, text="Copiar Contraseña", command=copiar_contraseña)
    boton_copiar_contraseña.grid(row=3, column=1, padx=10, pady=10, sticky="w")

def copiar_usuario():
    ventana_usuario.clipboard_clear()
    ventana_usuario.clipboard_append(entry_usuario.get())
    ventana_usuario.update()

def generador_usuario():
    def animar_ruleta_usuario():
        nonlocal ruleta_index_usuario
        ruleta_frames = ['|', '/', '-', '\\']
        if ruleta_index_usuario < len(ruleta_frames):
            ruleta_label_usuario.config(text=ruleta_frames[ruleta_index_usuario])
            ruleta_index_usuario += 1
            ventana_usuario.after(100, animar_ruleta_usuario)
        else:
            # Generar el usuario
            nombre_base = entry_nombre_base.get()
            if not nombre_base:
                entry_usuario.config(state='normal')
                entry_usuario.delete(0, tk.END)
                entry_usuario.insert(0, "Introduce un nombre base")
                entry_usuario.config(state='readonly')
                return

            nombre_modificado = modificar_nombre(nombre_base)
            sufijo = "".join(random.choice(string.digits) for i in range(4))
            usuario = f"{nombre_modificado}{sufijo}"

            entry_usuario.config(state='normal')
            entry_usuario.delete(0, tk.END)
            entry_usuario.insert(0, usuario)
            entry_usuario.config(state='readonly')
            ruleta_label_usuario.config(text='Listo!')

    global ruleta_label_usuario
    ruleta_index_usuario = 0
    animar_ruleta_usuario()

def modificar_nombre(nombre):
    caracteres = {
        'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'
    }
    nombre_modificado = []
    for char in nombre:
        if char in caracteres and random.choice([True, False]):
            nombre_modificado.append(caracteres[char])
        else:
            nombre_modificado.append(char)
    return ''.join(nombre_modificado)

def abrir_generador_usuario():
    global ventana_usuario, ruleta_label_usuario

    ventana_usuario = tk.Toplevel()
    ventana_usuario.title("Generador de Usuarios")
    ventana_usuario.geometry("420x250")

    # Usuario
    label_nombre_base = tk.Label(ventana_usuario, text="Ingrese el nombre base para el usuario:")
    label_nombre_base.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    # Validación para solo letras
    validacion_letras = (ventana_usuario.register(lambda s: s.isalpha() or s == ""), '%P')
    global entry_nombre_base
    entry_nombre_base = tk.Entry(ventana_usuario, validate='key', validatecommand=validacion_letras)
    entry_nombre_base.grid(row=0, column=1, padx=10, pady=10)

    label_usuario = tk.Label(ventana_usuario, text="El usuario es:")
    label_usuario.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    global entry_usuario
    entry_usuario = tk.Entry(ventana_usuario, width=40)
    entry_usuario.grid(row=1, column=1, padx=10, pady=10)
    entry_usuario.config(state='readonly')

    ruleta_label_usuario = tk.Label(ventana_usuario, text='', font=('Courier', 24))
    ruleta_label_usuario.grid(row=2, column=1, padx=10, pady=10)

    boton_generar_usuario = tk.Button(ventana_usuario, text="Generar Usuario", command=generador_usuario)
    boton_generar_usuario.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    boton_copiar_usuario = tk.Button(ventana_usuario, text="Copiar Usuario", command=copiar_usuario)
    boton_copiar_usuario.grid(row=3, column=1, padx=10, pady=10, sticky="w")

def abrir_ventana_principal():
    ventana_principal = tk.Tk()
    ventana_principal.title("Menú Principal")
    ventana_principal.geometry("400x150")

    boton_contraseña = tk.Button(ventana_principal, text="Generador de Contraseñas", command=abrir_generador_contraseña)
    boton_contraseña.pack(pady=20)

    boton_usuario = tk.Button(ventana_principal, text="Generador de Usuarios", command=abrir_generador_usuario)
    boton_usuario.pack(pady=20)

    ventana_principal.mainloop()

abrir_ventana_principal()


#HerlingCB