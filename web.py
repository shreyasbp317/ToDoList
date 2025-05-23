import streamlit as st
import functions

st.title("My Todo App")
st.subheader("This is my Todo App")
st.write("This app is to increase your productivity")

# Load todos
todos = functions.get_todos()

# Handle new todo addition
if "new_todo" in st.session_state and st.session_state["new_todo"].strip():
    new_item = st.session_state["new_todo"].strip() + "\n"
    todos.append(new_item)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""  # Clear after adding

# Display todos
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()  # This works outside callbacks

# Input box (NO on_change callback)
st.text_input(label="Add a new todo", key="new_todo", placeholder="Type and press Enter")

