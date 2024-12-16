import tkinter as tk
from tkinter import messagebox
from constants import style
from database import saldo, username, password



#Crear la ventana de bienvenida

class login(tk.Frame):
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.home_backg)
        self.controller = controller
        self.init_widgets_login()

    def check_login(self):
        user_ingresado = str(self.entry_user.get())
        password_ingresado = str(self.entry_password.get())

        # Validar credenciales
        if user_ingresado == username and password_ingresado == password:
            self.controller.show_frame(home)
        elif user_ingresado == username and password_ingresado != password:
            messagebox.showinfo("Error", "La contraseña ingresada no es correcta.")
        elif user_ingresado != username and password_ingresado == password:
            messagebox.showinfo("Error", "El usuario ingresado no es correcto.")
        else:
            messagebox.showinfo("Error", "La contraseña/usuario ingresado no es correcto.")

    def init_widgets_login(self):
        # Etiqueta de bienvenida
        tk.Label(
            self,
            text="Bienvenido a la Banca Móvil de Station Square",
            justify=tk.CENTER,
            **style.text_saldo
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=11,
        )

        # Etiqueta y entrada de usuario
        tk.Label(
            self,
            text="Usuario:",
            justify=tk.LEFT,
            **style.text_saldo
        ).pack(
            side=tk.TOP,
            anchor=tk.W,
            padx=22,
            pady=5,
        )
        self.entry_user = tk.Entry(self, font=('Arial', 15), width=5)
        self.entry_user.pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=5,
        )

        # Etiqueta y entrada de contraseña
        tk.Label(
            self,
            text="Contraseña:",
            justify=tk.LEFT,
            **style.text_saldo
        ).pack(
            side=tk.TOP,
            anchor=tk.W,
            padx=22,
            pady=5,
        )
        self.entry_password = tk.Entry(self, font=('Arial', 15), show="*")
        self.entry_password.pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=5,
        )

        # Crear un Frame para el botón y colocarlo al fondo
        button_frame = tk.Frame(self, bg=style.home_backg)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=15)

        tk.Button(
            button_frame,
            width=30,
            text="Login",
            command=lambda: self.check_login(),
            **style.text_style
        ).pack(
            side=tk.BOTTOM,
            padx=15,
            pady=5,
        )



#Crear la pantalla de menú principal
class home(tk.Frame):
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.home_backg)
        self.controller = controller
        self.init_widgets_home()
        
    #Definir el método para depositar
    def jump_to_deposit(self):
        self.controller.show_frame(deposit)
    
    #Definir el método para retirar
    def jump_to_withdraw(self):
        self.controller.show_frame(withdraw)
        
    #Colocar los widgets en el frame del menú principal    
    def init_widgets_home(self):
        self.label_saldo=tk.Label(
            self,
            text=f"Su Saldo :{saldo:.2f}",
            justify=tk.CENTER,
            **style.text_saldo
            )
        self.label_saldo.pack(
                side=tk.TOP,
                fill=tk.X,
                expand=True,
                padx=22,
                pady=11,
            )
            
        #Widget para ir al menú de Retiro
        tk.Button(
            self,
            width=30,
            text="Retirar",
            command=lambda: self.jump_to_withdraw(),
            justify=tk.CENTER,
            **style.text_style
            ).pack(
                side=tk.TOP,
                expand=True,
                padx=22,
                pady=11,
            )        
            
        tk.Button(
            self,
            width=30,
            text="Depositar",
            command= lambda: self.jump_to_deposit(),
            justify=tk.CENTER,
            **style.text_style
            ).pack(
                side=tk.TOP,
                
                expand=True,
                padx=22,
                pady=11,
            )        
            
    # Método para actualizar dinámicamente el saldo
    def update_saldo(self):
        self.label_saldo.config(text=f"Saldo actual: ${saldo:.2f}")

# Crear la pantalla de depósito
class deposit(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.home_backg)
        self.controller = controller
        self.init_widgets_deposit()

    # Definir el método para regresar al menú principal
    def jump_to_home(self):
        self.controller.show_frame(home)

    # Definir el método para realizar un depósito
    def depositar(self):
        try:
            # Obtener el monto ingresado
            monto_ingresado = float(self.entry_deposit.get())
            if monto_ingresado <= 0:
                raise ValueError("El monto a depositar debe ser positivo.")

            global saldo  # Usa la variable global 'saldo'
            saldo += monto_ingresado  # Actualiza el saldo

            # Mostrar mensaje de éxito
            messagebox.showinfo(
                "Depósito Exitoso",
                f"Has depositado ${monto_ingresado:.2f}. Tu nuevo saldo es: ${saldo:.2f}",
            )
            self.label_saldo.config(text=f"Su Saldo :{saldo:.2f}")
            self.entry_deposit.delete(0, tk.END)  # Limpia la entrada

        except ValueError as e:
            # Mostrar error específico
            messagebox.showerror("Error", "Por favor, ingrese sólo números.")
        except Exception:
            # Mostrar error genérico
            messagebox.showerror("Error", "Por favor ingresa un monto válido.")

    # Colocar los widgets en el frame de la clase depósito
    def init_widgets_deposit(self):
        self.label_saldo=tk.Label(
            self,
            text=f"Su Saldo :{saldo:.2f}",
            justify=tk.CENTER,
            **style.text_saldo
        )
        self.label_saldo.pack(
            side=tk.TOP,
            fill=tk.X,
            expand=True,
            padx=22,
            pady=11,
        )

        tk.Label(
            self,
            text="Ingrese el monto a depositar: ",
            justify=tk.CENTER,
            **style.text_style
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            expand=True,
            padx=22,
            pady=11,
        )

        # Guardar entry_deposit como atributo de la instancia
        self.entry_deposit = tk.Entry(self, font=('Arial', 15))
        self.entry_deposit.pack(side=tk.TOP, fill=tk.X, expand=True, padx=22, pady=11)

        tk.Button(
            self,
            text="Cancelar",
            command=lambda: self.jump_to_home(),
            justify=tk.LEFT,
            **style.text_style
        ).pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,
            padx=22,
            pady=11,
        )

        tk.Button(
            self,
            text="Aceptar",
            command=self.depositar,  # Llama directamente a self.depositar
            justify=tk.RIGHT,
            **style.text_style
        ).pack(
            side=tk.RIGHT,
            fill=tk.X,
            expand=True,
            padx=22,
            pady=11,
        )

       # Método para actualizar dinámicamente el saldo
    def update_saldo(self):
        self.label_saldo.config(text=f"Saldo actual: ${saldo:.2f}")
        

#Crear la pantalla de retiro
class withdraw(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.home_backg)
        self.controller = controller
        self.init_widgets_deposit()

    # Definir el método para regresar al menú principal
    def jump_to_home(self):
        self.controller.show_frame(home)

    # Definir el método para realizar un retiro
    def retirar(self):
        try:
            global saldo  # Usa la variable global 'saldo'
            # Obtener el monto ingresado
            monto_ingresado = float(self.entry_deposit.get())
            if monto_ingresado <= 0:
                raise ValueError("El monto a retirar debe ser positivo.")
            elif monto_ingresado > saldo:
                raise ValueError("Fondos insuficientes.")
            elif monto_ingresado > 0 and monto_ingresado < saldo:
                saldo -= monto_ingresado  # Actualiza el saldo
                # Mostrar mensaje de éxito
                messagebox.showinfo(
                "Retiro Exitoso",
                f"Has retirado ${monto_ingresado:.2f}. Tu nuevo saldo es: ${saldo:.2f}",
            )
            self.label_saldo.config(text=f"Su Saldo :{saldo:.2f}")
            self.entry_deposit.delete(0, tk.END)  # Limpia la entrada

        
        except Exception:
            # Mostrar error genérico
            messagebox.showerror("Error", "Por favor ingresa un monto válido.")

    # Colocar los widgets en el frame de la clase depósito
    def init_widgets_deposit(self):
        self.label_saldo=tk.Label(
            self,
            text=f"Su Saldo :{saldo:.2f}",
            justify=tk.CENTER,
            **style.text_saldo
        )
        self.label_saldo.pack(
            side=tk.TOP,
            fill=tk.X,
            expand=True,
            padx=22,
            pady=11,
        )

        tk.Label(
            self,
            text="Ingrese el monto a retirar: ",
            justify=tk.CENTER,
            **style.text_style
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            expand=True,
            padx=22,
            pady=11,
        )

        # Guardar entry_deposit como atributo de la instancia
        self.entry_deposit = tk.Entry(self, font=('Arial', 15))
        self.entry_deposit.pack(side=tk.TOP, fill=tk.X, expand=True, padx=22, pady=11)

        tk.Button(
            self,
            text="Cancelar",
            command=lambda: self.jump_to_home(),
            justify=tk.LEFT,
            **style.text_style
        ).pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,
            padx=22,
            pady=11,
        )

        tk.Button(
            self,
            text="Aceptar",
            command=self.retirar,  # Llama directamente a self.depositar
            justify=tk.RIGHT,
            **style.text_style
        ).pack(
            side=tk.RIGHT,
            fill=tk.X,
            expand=True,
            padx=22,
            pady=11,
        )

       # Método para actualizar dinámicamente el saldo
    def update_saldo(self):
        self.label_saldo.config(text=f"Saldo actual: ${saldo:.2f}")
