from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image= models.ImageField(upload_to='courses/%Y/%m', null=True)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

