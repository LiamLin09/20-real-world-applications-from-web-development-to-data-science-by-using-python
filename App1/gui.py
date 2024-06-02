import functions
import FreeSimpleGUI as sg
import time

sg.theme('GreenMono')

clock = sg.Text('', key='clock')
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip="Enter to-do activity", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos', 
                      enable_events=True,
                      size=[40, 10])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]
window = sg.Window('My to-do APP',
                   layout=layout,
                   font=('Helvetica', 15))
while True:
    event, values = window.read(timeout=1000)
    window['clock'].update(value=time.strftime("%b %d %Y, %H:%M:%S"))
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)

            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)

                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 15))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)

                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 15))
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()