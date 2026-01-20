FILEPATH = 'todos.txt'


# READ LINES ------------------------------------------------------------------
def GetTodos(TodosFilePath = FILEPATH):
    """
    read a text file and return the list of to-do items.
    """
    with open(TodosFilePath, 'r') as FileLocal:
        TodosLocal = FileLocal.readlines()
    return TodosLocal


# WRITE LINES -----------------------------------------------------------------
def WriteTodos(TodosArg, TodosFilePath = FILEPATH):
    """
    Write a to-do items list in the text file.
    """
    with open(TodosFilePath, 'w') as file:
        file.writelines(TodosArg)


if __name__ == "__main__":
    print('hello from functions')