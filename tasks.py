class Task():

    def __init__(self, id, description, deadline, status="Не выполнено"):
        self.id = id
        self.description = description
        self.deadline = deadline
        self.status = status

class TasksMenedger():
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_done(self, description):
        for task in self.tasks:
            if task.description == description:
                task.status = "выполнено"

    def get_current_tasks(self):
        current_tasks = [task for task in self.tasks if task.status == "не выполнено"]
        for task in current_tasks:
            print(f"Описание задачи: {task.description}, Срок выполнения: {task.deadline}, Статус: {task.status}")

task_manager = TasksMenedger()

task_manager.add_task("Прозвонить клиентов", "15.05.2024")
task_manager.add_task("Подготовить отчет", "15.05.2024")

task_manager.mark_task_done("Прозвонить клиентов")

print("Текущие задачи:")
task_manager.get_current_tasks()


