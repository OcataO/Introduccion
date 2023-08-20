from django.db import models

# Create your models here. - Cada vez que se hace un cambio aqui se debe migrar por cmd:
#python manage.py makemigrations blog

class Post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()

    def __str__(self) -> str:
        return self.title
