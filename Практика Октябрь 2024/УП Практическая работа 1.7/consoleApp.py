import json
from datetime import datetime, timedelta

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d')

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date.strftime('%Y-%m-%d')
        }

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                tasks_data = json.load(file)
                return [Task(**task) for task in tasks_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file)

    def add_task(self, title, description, due_date):
        self.tasks.append(Task(title, description, due_date))
        self.save_tasks()

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]
        self.save_tasks()

    def edit_task(self, title, new_title, new_description, new_due_date):
        for task in self.tasks:
            if task.title == title:
                task.title = new_title
                task.description = new_description
                task.due_date = datetime.strptime(new_due_date, '%Y-%m-%d')
                break
        self.save_tasks()

    def get_tasks_for_today(self):
        today = datetime.now().date()
        return [task for task in self.tasks if task.due_date.date() == today]

    def get_tasks_for_tomorrow(self):
        tomorrow = (datetime.now() + timedelta(days=1)).date()
        return [task for task in self.tasks if task.due_date.date() == tomorrow]

    def get_tasks_for_week(self):
        week_start = datetime.now().date()
        week_end = week_start + timedelta(days=7)
        return [task for task in self.tasks if week_start <= task.due_date.date() <= week_end]

    def get_all_tasks(self):
        return self.tasks

    def get_pending_tasks(self):
        return [task for task in self.tasks if task.due_date >= datetime.now()]

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.due_date < datetime.now()]

def main():
    manager = TaskManager()
    while True:
        action = input("Введите действие (add, remove, edit, view, exit): ").strip().lower()
        if action == 'add':
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            due_date = input("Введите дату выполнения (YYYY-MM-DD): ")
            manager.add_task(title, description, due_date)
        elif action == 'remove':
            title = input("Введите название задачи для удаления: ")
            manager.remove_task(title)
        elif action == 'edit':
            title = input("Введите название задачи для редактирования: ")
            new_title = input("Введите новое название задачи: ")
            new_description = input("Введите новое описание задачи: ")
            new_due_date = input("Введите новую дату выполнения (YYYY-MM-DD): ")
            manager.edit_task(title, new_title, new_description, new_due_date)
        elif action == 'view':
            view_action = input("Что вы хотите просмотреть? (today, tomorrow, week, all, pending, completed): ").strip().lower()
            if view_action == 'today':
                tasks = manager.get_tasks_for_today()
            elif view_action == 'tomorrow':
                tasks = manager.get_tasks_for_tomorrow()
            elif view_action == 'week':
                tasks = manager.get_tasks_for_week()
            elif view_action == 'all':
                tasks = manager.get_all_tasks()
            elif view_action == 'pending':
                tasks = manager.get_pending_tasks()
            elif view_action == 'completed':
                tasks = manager.get_completed_tasks()
            else:
                print("Неверный ввод.")
                continue
            
            for task in tasks:
                print(f"{task.title} - {task.description} (до {task.due_date.strftime('%Y-%m-%d')})")
        elif action == 'exit':
            break
        else:
            print("Неверный ввод.")

if __name__ == "__main__":
    main()
