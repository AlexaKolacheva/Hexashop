from django.db import models



class Callback(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Feedback(models.Model):
    CHOICES = (
        ('male', 'Мужчина'),
        ('female', 'Женщина')

    )
    text = models.CharField(max_length=500)
    gender = models.CharField(choices=CHOICES, max_length=6)
    name = models.CharField(max_length=20)
    profession = models.CharField(max_length=30)

    def __str__(self):
        return self.name
