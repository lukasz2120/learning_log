from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """Temat definiowany przez użytkownika"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Zwraca reprezentacje modelu w postaci ciągu tekstowego"""
        return self.text
    
class Entry(models.Model):
    """Informacje, wpisy odnośnie konkretnego tematu"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Zwaraca reprezentacje modelu w postaci ciągu tesktowego"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"