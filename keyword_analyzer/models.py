from django.db import models
from django.contrib.auth.models import User

class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    search_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Search History'
        verbose_name_plural='Search Histories'

    def __str__(self):
        obj_name = str(self.user)
        return obj_name


class Keyword(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=1)
    search_history = models.ManyToManyField(SearchHistory)
    class Meta:
        verbose_name='Keyword'
        verbose_name_plural='Keywords'

    def __str__(self):
        obj_name = self.name
        return obj_name



