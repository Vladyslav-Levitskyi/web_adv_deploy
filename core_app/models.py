from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='first_name')
    last_name = models.CharField(max_length=50, verbose_name='last_name')
    email = models.EmailField(max_length=70, verbose_name='email')

    def __str__(self):
        return f"{self.first_name} \n {self.last_name} \n {self.email}"

