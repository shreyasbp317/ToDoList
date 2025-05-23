from cProfile import label

import FreeSimpleGUI as sg
import functions
import time

sg.theme("name of the theme")

clock = sg.Text('', key='clock')
label = sg.Text("Text in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key = "todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values = functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("edit")
complete_button = sg.Button("complete")
exit_button = sg.Button("exit")

button_labels = ["close","apply"]

layout = []
for bl in button_labels:
    layout.append([sg.Button(bl)])
[[sg.Button("close")], [sg.Button("apply")]]
layout = [[clock],[label],[input_box, add_button],[list_box, edit_button, complete_button],[exit_button]]

window = sg.Window('My to do-app',
                   layout=layout,
                   font=('Helvetica',20))
while True:
    event,values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:

                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("please select an item first.", font=("helvetica",20))

        case "complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("please select an item first.", font=("helvetica", 20))

        case "exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])


        case sg.WIN_CLOSED:

             break

window.close()