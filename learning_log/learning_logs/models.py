from django.db import models

# Create your models here.

class Topic(models.Model):
    """Um assunto sobre o quaal o usuario esta aprendendo"""
    text=models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma reprensenstacao em string do modelo"""
        return self.text