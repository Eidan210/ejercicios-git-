
def eliminar_tarea():
    from Modulos_git import tareas
    while True:
        print("Eligió eliminar una tarea")
        print(f"Lista actual: {tareas}")
        
        eliminar_tarea = input("Escriba la tarea que quiere eliminar: ").capitalize()

        if not eliminar_tarea:
            print("No pusiste la tarea que quieres eliminar, inténtalo de nuevo.")
            return

        if eliminar_tarea in tareas:
            tareas.remove(eliminar_tarea)
            print(f"Tarea '{eliminar_tarea}' eliminada correctamente.")
            decision = input("¿desea eliminar otra tarea? S/N ").upper()
            if decision == "S":
                print("se repetira esta funcion")
                continue
            elif decision =="N":
                print ("volveras al menu en breve...")
                return
        else:
            print("Esa tarea no se encontró en la lista.")
            return