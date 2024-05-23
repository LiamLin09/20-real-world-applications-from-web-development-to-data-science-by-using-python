while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo= input("Enter a ToDo: ") + '\n'

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1} -{item}")
        case 'exit':
            break
        case 'edit':
            number = int(input("Number of the ToDo to edit: "))
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter a new ToDo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        # after complete, it will remove from the todo list.
        case 'complete':
             number2 = int(input("Number of the ToDo to complete: "))

             with open('todos.txt', 'r') as file:
                 todos = file.readlines()

             index = number2 - 1
             todo_to_remove = todos[index].strip('\n')
             todos.pop(index)

             with open('todos.txt', 'w') as file:
                 file.writelines(todos)

             message = f"ToDo {todo_to_remove} was removed from the list."
             print(message)

        case whatever:
            print('You entered an unknown command!!')

print('Bye!')