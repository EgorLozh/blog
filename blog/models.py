from django.db import models

# Create your models here.
# Данные о посте
class Post(models.Model):
    title = models.CharField("Заголовок записи", max_length=100)
    description = models.TextField("Текст записи")
    author = models.CharField("Имя автора", max_length=100)
    date = models.DateField("Дата публекации")
    image = models.ImageField("Изображение", upload_to="image/%Y")


    def __str__(self):
        return f"{self.title}, {self.author}"

    class Meta:
        verbose_name = "Записи"
        verbose_name_plural = "Записи"
