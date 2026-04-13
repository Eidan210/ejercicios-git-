
def agregar_tarea():
    from Modulos_git import tareas
    while True:
        tarea = str(input("Agregue la tarea deseada. ")).capitalize()
        tareas.append(tarea)
        decision = input("¿desea añadir otra tarea? S/N: ").upper()
        if decision == "S":
            print("Repetiras esta funcion")
            continue
        elif decision == "N":
            print("Volveras al menu en breve...")
            return