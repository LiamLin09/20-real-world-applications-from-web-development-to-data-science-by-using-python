todos = []

while True:
    user_action = input("Type add, show, edit, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a ToDo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case 'edit':
            number = input("Number of the ToDo to edit: ")
            existing_todo = todos[int(number) - 1]
            new_todo = input("Enter a new ToDo: ")
            todos[int(number) - 1] = new_todo
        case whatever:
            print('You entered an unknown command!!')

print('Bye!')




