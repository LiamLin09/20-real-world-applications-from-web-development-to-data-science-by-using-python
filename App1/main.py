while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:] + '\n'
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        todos.append(todo)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1} -{item}")

    elif 'exit' in user_action:
        break

    elif 'edit' in user_action:
        number = int(user_action[5:])
        number = number - 1
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        new_todo = input("Enter a new ToDo: ")
        todos[number] = new_todo + '\n'
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    # after complete, it will remove from the todo list.
    elif 'complete' in user_action:
         number = int(user_action[9:])
         with open('todos.txt', 'r') as file:
             todos = file.readlines()
         index = number - 1
         todo_to_remove = todos[index].strip('\n')
         todos.pop(index)
         with open('todos.txt', 'w') as file:
             file.writelines(todos)
         message = f"ToDo {todo_to_remove} was removed from the list."
         print(message)

    else:
        print('Sorry, Command is not valid!!!')


print('Bye!')