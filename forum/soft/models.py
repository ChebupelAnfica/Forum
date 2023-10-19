from django.db import models
from django.utils import timezone


class SoftArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/soft/{self.id}'

    class Meta:
        verbose_name = 'Доски'
        verbose_name_plural = "Тред для soft"