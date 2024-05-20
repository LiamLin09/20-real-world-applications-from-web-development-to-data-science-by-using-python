user_prompt = "Plz enter a ToDo: "

todos = []

while True:
    todo = input(user_prompt)
    todo1 = todo.title()
    todos.append(todo1)
    print(todos)


