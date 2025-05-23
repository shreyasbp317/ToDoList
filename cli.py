import functions
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("it is",now)

while True:
    user_action = input("enter show or add or complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = user_action[4:]

        todos = functions.get_todos('todos.txt')

        todos.append(todo)

        todos.append(todo + "\n")

        functions.write_todos("todos.txt", todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()


        for index,item in enumerate(todos):
            row = f"{index+1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:

            number = int(input("enter the number of todos"))
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("enter the new todo")
            todos[number] = new_todo + '\n'

            functions.write_todos("todos.txt", todos)
        except ValueError:
            print("your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:


            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            functions.write_todos("todos.txt", todos)

            message = f"todo{todo_to_remove}is removed from the list."
            print(message)
        except IndexError:
            print("there is no item with that number:")
            continue
    elif user_action.startswith("exit"):

        break
    else:
        print("invalid command")

print("bye")
