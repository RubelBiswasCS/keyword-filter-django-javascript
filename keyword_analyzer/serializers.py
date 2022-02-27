from rest_framework import serializers
from .models import User, SearchHistory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id','username']

class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=SearchHistory
        fields = '__all__'
