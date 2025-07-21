# Panel simple de tareas para POO
# Hecho por Bryan Molina

class Tarea:
    def __init__(self, nombre, estado="Pendiente"):
        self.nombre = nombre
        self.estado = estado

    def mostrar(self):
        print(f"{self.nombre} - {self.estado}")

# Lista donde voy a guardar mis tareas
lista_tareas = [
    Tarea("Repasar clases"),
    Tarea("Entrega proyecto final", "En proceso"),
    Tarea("Estudiar examen", "Pendiente")
]

def ver_tareas():
    print("\n--- MIS TAREAS ---")
    if len(lista_tareas) == 0:
        print("No hay tareas por ahora.")
    else:
        for i, t in enumerate(lista_tareas):
            print(f"{i+1}. ", end="")
            t.mostrar()

def agregar():
    n = input("Nombre de la nueva tarea: ")
    lista_tareas.append(Tarea(n))
    print("Tarea añadida.")

def cambiar_estado():
    ver_tareas()
    try:
        i = int(input("Número de tarea a cambiar: ")) - 1
        if i >= 0 and i < len(lista_tareas):
            nuevo = input("Nuevo estado: ")
            lista_tareas[i].estado = nuevo
            print("Estado cambiado.")
        else:
            print("Tarea no encontrada.")
    except:
        print("Error al ingresar el número.")

def menu():
    while True:
        print("\n1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Cambiar estado")
        print("4. Salir")
        opc = input("Opción: ")

        if opc == "1":
            ver_tareas()
        elif opc == "2":
            agregar()
        elif opc == "3":
            cambiar_estado()
        elif opc == "4":
            print("Adiós :)")
            break
        else:
            print("Opción no válida")

menu()