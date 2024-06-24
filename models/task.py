from datetime import datetime

class Task:
    """
    Classe que representa uma tarefa.
    """

    def __init__(self, title, description, due_date, priority, category):
        """
        Inicializa uma nova instância da classe Task.
        
        Args:
            title (str): O título da tarefa.
            description (str): A descrição da tarefa.
            due_date (str): A data de vencimento da tarefa.
            priority (str): A prioridade da tarefa (Low, Medium, High).
            category (Category): A categoria da tarefa.
        """
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.category = category
        self.created_at = datetime.now()  # Data e hora de criação da tarefa

    def __str__(self):
        """
        Retorna a representação em string da tarefa.
        
        Returns:
            str: Uma string que representa a tarefa.
        """
        return f"{self.title} - {self.description} - {self.due_date} - {self.priority} - {self.category}"
