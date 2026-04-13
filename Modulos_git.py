from agregar import agregar_tarea
from eliminar import eliminar_tarea
from editar import editar_tarea
tareas = []

def menu():
    while True:
        print("""
==============================
        BIENVENID@s
Que opcion desea realizar hoy:

1. agregar tarea
2. editar tarea
3. eliminar tarea
4. salir...
==============================""")

        opcion = int(input("que opcion desea elegir. "))
        if opcion <= 0 and opcion >= 5:
            print("opcion no valida, intente denuevo")
            continue
        elif opcion == 1:
            agregar_tarea()
        elif opcion == 2:
            editar_tarea()
        elif opcion == 3:
            eliminar_tarea()
        elif opcion == 4:
            print("saliendo...")
            break
        else:
            print("error")
            break
        
if __name__ == "__main__":
    menu()
