def get_todos(filepath='todos.txt'):
    """
    read a text file and return the list of to-do item.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todos.txt'):
    """
    write the to-do items list in the text file.
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)