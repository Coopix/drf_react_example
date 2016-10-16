from django.db import models

class Message(models.Model):
    """
    Represents a message on a board.
    """
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=2000)
