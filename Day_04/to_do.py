to_do_list = []

while True:
    print("\n1. Add Task\n2. Edit Task\n3. Delete Task\n4. Exit")

    try:
        option = int(input("Select an option: "))
    except ValueError:
        print("Option invalide")
        continue

    if option == 1:
        task = input("Enter task: ")
        to_do_list.append(task)
        print("Task added successfully.")

    elif option == 2:
        if not to_do_list:
            print("La liste est vide")
            continue

        try:
            i = int(input("Enter task index to edit: "))
            to_do_list[i] = input("Enter new task: ")
            print("Task edited successfully.")
        except ValueError:
            print("Ce n'est pas un index valide")
        except IndexError:
            print("Index hors limites")

    elif option == 3:
        if not to_do_list:
            print("La liste est vide")
            continue

        try:
            i = int(input("Enter task index to delete: "))
            to_do_list.pop(i)
            print("Task deleted successfully.")
        except ValueError:
            print("Ce n'est pas un index valide")
        except IndexError:
            print("Index hors limites")

    elif option == 4:
        break

    else:
        print("Option not available")
