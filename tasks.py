class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        self.tasks.append({"description": description, "deadline": deadline, "status": "не выполнено"})

    def complete_task(self, description):
        for task in self.tasks:
            if task["description"] == description:
                task["status"] = "выполнено"
                print(f"Задача {task['description']} выполнена.")
                return
        print(f"Задача {description} не найдена.")

    def show_tasks(self):
        print("Список задач")
        for task in self.tasks:
            if task['status'] == "не выполнено":
                print(f"{task['description']} - {task['deadline']}")

t = Task()
t.add_task("Купить молоко", "25.06.2024")
t.add_task("Помыть кота", "25.06.2024")
t.add_task("Помыть посуду", "25.06.2024")

t.show_tasks()

t.complete_task("Помыть посуду")
t.show_tasks()





