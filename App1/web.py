import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    new_todo_item = st.session_state['new_todo'] + '\n'
    todos.append(new_todo_item)
    functions.write_todos(todos)


st.title("My to-do App")
st.subheader("This is my to-do app")
st.write('this app is to increase your productivity.')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='',
              placeholder='Add new to-do..',
              on_change=add_todo,
              key='new_todo')


