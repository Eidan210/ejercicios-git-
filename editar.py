
def editar_tarea():
    from Modulos_git import tareas
    while True:
        posicion = 0
        print("Eligio editar una tarea")
        print(tareas)
        editar_tarea = input("Escriba la tarea que quiere editar: ").strip().capitalize()
        posicion = (tareas.index(editar_tarea))
        tarea_editada = input("ingrese la tarea ya editada: ").strip().capitalize()
        tareas[posicion] = tarea_editada
        if not editar_tarea or not tarea_editada:
            print("no pusiste la tarea que quieres editar o la tarea ya editada,intentalo denuevo")
            continue
        else:
            print("Se realizo correctamente el cambio, volveras al menu...")
            return