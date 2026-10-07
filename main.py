from task_manager import TaskManager

def print_menu():
        print("\n --- Gestor de tareas inteligente ---")
        print("1. Añadir tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")


def validate_int(input_str):
    try:
        return int(input_str)
    except ValueError:
        print("Por favor, introduce un número válido.")
        return None


def main():

    task_mgr = TaskManager()

    while True:

        print_menu()
        choice = input("Elige una opción: ")

        match choice:
            case "1":
                description = input("Introduce la descripción de la tarea: ")
                task_mgr.add_task(description)
            case "2":
                task_mgr.list_tasks()
            case "3":
                id = validate_int(input("Introduce el número de la tarea a completar: "))
                if id is not None:
                    task_mgr.complete_task(id)
            case "4":
                id = validate_int(input("Introduce el número de la tarea a eliminar: "))
                if id is not None:
                    task_mgr.delete_task(id)
            case "5":
                print("Saliendo...")
                break
            case _:
                print("La opción seleccionada no es válida. Selecciona otra")

if __name__ == "__main__":
    main()
