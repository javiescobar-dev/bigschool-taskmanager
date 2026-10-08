from task_manager import TaskManager
from ai_service import create_simple_tasks

def print_menu():
        print("\n --- Gestor de tareas inteligente ---")
        print("1. Añadir tarea")
        print("2. Añadir tarea compleja (con IA)")
        print("3. Listar tareas")
        print("4. Completar tarea")
        print("5. Eliminar tarea")
        print("6. Salir")


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
                description = input("Introduce la descripción de la tarea compleja: ")
                subtasks = create_simple_tasks(description)
                for subtask in subtasks:
                    if not subtask.startswith("Error:"):
                        task_mgr.add_task(subtask)
                    else:
                        print(subtask)
                        break
            case "3":
                task_mgr.list_tasks()
            case "4":
                id = validate_int(input("Introduce el número de la tarea a completar: "))
                if id is not None:
                    task_mgr.complete_task(id)
            case "5":
                id = validate_int(input("Introduce el número de la tarea a eliminar: "))
                if id is not None:
                    task_mgr.delete_task(id)
            case "6":
                print("Saliendo...")
                break
            case _:
                print("La opción seleccionada no es válida. Selecciona otra")

if __name__ == "__main__":
    main()
