todos = []

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a ToDo: ")
            todos.append(todo)
        case 'show' | 'display':
            for index, item in enumerate(todos):
                print(f"{index + 1} -{item}")
        case 'exit':
            break
        case 'edit':
            number = input("Number of the ToDo to edit: ")
            existing_todo = todos[int(number) - 1]
            new_todo = input("Enter a new ToDo: ")
            todos[int(number) - 1] = new_todo
        case 'complete':
             number2 = int(input("Number of the ToDo to complete: "))
             todos.pop(number2 - 1)
        case whatever:
            print('You entered an unknown command!!')

print('Bye!')




