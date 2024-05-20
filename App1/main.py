todos = []

while True:
    user_action = input("Type add, show, or exit: ")

    match user_action:
        case 'add':
            todo = input("Enter a ToDo: ")
            todos.append(todo.title())
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break

print('Bye!')




