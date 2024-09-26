class ToDoList:
    def __init__(self):
        self.tasks = []

    def andar_task(self, task):
        self.tasks.append(task)
        print("Added task: %s" % task)

    def gaib_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Removed task: %s" % task)
        else:
            print("Task not found.")

    def view_tasks(self):
        print("To-Do List:")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")


todo = ToDoList()
todo.andar_task("Learn Python with hassan")
todo.andar_task("Build a project with hassan")
todo.view_tasks()
todo.gaib_task("Learn Python with Master Hassan")
todo.view_tasks()
