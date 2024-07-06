import pickle
import os

# Definición de clase libro y clase usuario
class Libro:
    def __init__(self, titulo, autor, cantidad=1, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad
        self.disponible = disponible

    def __str__(self):
        disponibilidad = "Disponible" if self.disponible else "No disponible"
        return f"{self.titulo} - {self.autor} - Cantidad: {self.cantidad} - {disponibilidad}"

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre}"

# Funciones de la biblioteca
def cargar_datos():
    global libros, usuarios
    if os.path.exists('datos_biblioteca.pkl'):
        with open('datos_biblioteca.pkl', 'rb') as f:
            libros, usuarios = pickle.load(f)
    else:
        libros = {}
        usuarios = {}

def guardar_datos():
    with open('datos_biblioteca.pkl', 'wb') as f:
        pickle.dump((libros, usuarios), f)

def agregar_libro(titulo, autor):
    if titulo in libros:
        libros[titulo].cantidad += 1
    else:
        libros[titulo] = Libro(titulo, autor)

def mostrar_libros():
    for libro in libros.values():
        print(libro)

def prestar_libro(titulo, nombre_usuario):
    if titulo in libros and libros[titulo].disponible:
        if nombre_usuario in usuarios:
            libros[titulo].disponible = False
            libros[titulo].cantidad -= 1
            usuarios[nombre_usuario].libros_prestados.append(titulo)
            print(f"Libro '{titulo}' prestado a '{nombre_usuario}'")
        else:
            print(f"El usuario '{nombre_usuario}' no está registrado.")
    else:
        print(f"El libro '{titulo}' no está disponible.")

def registrar_usuario(nombre):
    if nombre not in usuarios:
        usuarios[nombre] = Usuario(nombre)
        print(f"Usuario '{nombre}' registrado.")
    else:
        print(f"El usuario '{nombre}' ya está registrado.")

def listar_usuarios():
    for usuario in usuarios.values():
        print(usuario)

def listar_libros_de_usuario(nombre_usuario):
    if nombre_usuario in usuarios:
        libros_prestados = usuarios[nombre_usuario].libros_prestados
        if libros_prestados:
            print(f"Libros prestados a '{nombre_usuario}':")
            for titulo in libros_prestados:
                print(f"- {titulo}")
        else:
            print(f"{nombre_usuario} no tiene libros prestados.")
    else:
        print(f"El usuario '{nombre_usuario}' no está registrado.")

def devolver_libro(titulo, nombre_usuario):
    if nombre_usuario in usuarios and titulo in usuarios[nombre_usuario].libros_prestados:
        libros[titulo].disponible = True
        libros[titulo].cantidad += 1
        usuarios[nombre_usuario].libros_prestados.remove(titulo)
        print(f"Libro '{titulo}' devuelto por '{nombre_usuario}'.")
    else:
        print(f"El usuario '{nombre_usuario}' no tiene el libro '{titulo}' prestado.")

# Menú principal
def menu():
    cargar_datos()
    
    while True:
        print("\n=== Biblioteca ===")
        print("1. Agregar Libro")
        print("2. Mostrar Libros")
        print("3. Prestar Libro")
        print("4. Registrar Usuario")
        print("5. Listar Usuarios")
        print("6. Listar Libros de Usuario")
        print("7. Devolver Libro")
        print("8. Guardar y Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            agregar_libro(titulo, autor)
        elif opcion == '2':
            print("\nLibros en la biblioteca:")
            mostrar_libros()
        elif opcion == '3':
            titulo = input("Ingrese el título del libro a prestar: ")
            nombre_usuario = input("Ingrese el nombre del usuario: ")
            prestar_libro(titulo, nombre_usuario)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del usuario a registrar: ")
            registrar_usuario(nombre)
        elif opcion == '5':
            print("\nUsuarios registrados:")
            listar_usuarios()
        elif opcion == '6':
            nombre_usuario = input("Ingrese el nombre del usuario para listar sus libros prestados: ")
            listar_libros_de_usuario(nombre_usuario)
        elif opcion == '7':
            titulo = input("Ingrese el título del libro a devolver: ")
            nombre_usuario = input("Ingrese el nombre del usuario: ")
            devolver_libro(titulo, nombre_usuario)
        elif opcion == '8':
            guardar_datos()
            print("Datos guardados. Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()