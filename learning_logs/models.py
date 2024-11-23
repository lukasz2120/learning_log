from django.db import models

class Topic(models.Model):
    """Temat definiowany przez użytkownika"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Zwraca reprezentacje modelu w postaci ciągu tekstowego"""
        return self.text
    
class Entry(models.Model):
    """Informacje, wpisy odnośnie konkretnego tematu"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name_plural = 'entries'

        def __str__(self):
            """Zwaraca reprezentacje modelu w postaci ciągu tesktowego"""
            return f"{self.text[:50]}...",