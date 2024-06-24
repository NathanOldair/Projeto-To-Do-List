from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, priority, category):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.category = category
        self.created_at = datetime.now()

    def __str__(self):
        return f"{self.title} - {self.description} - {self.due_date} - {self.priority} - {self.category}"