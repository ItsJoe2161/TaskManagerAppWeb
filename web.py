import streamlit as st
import functions

todos = functions.GetTodos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.WriteTodos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

todos_to_remove = []

for todo in todos:
    if st.checkbox(todo, key=todo):
        todos_to_remove.append(todo)

if todos_to_remove:
    for todo in todos_to_remove:
        todos.remove(todo)
        del st.session_state[todo]
    functions.WriteTodos(todos)
    st.rerun()

st.text_input(
    label="Enter here a todo",
    placeholder="Add a new todo...",
    on_change=add_todo,
    key='new_todo'
)
st.session_state