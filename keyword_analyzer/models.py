
from django.db import models
from django.contrib.auth.models import User

class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    keyword = models.CharField(max_length=100)
    search_date = models.DateTimeField(auto_now_add=True)
