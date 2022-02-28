from ast import keyword
from rest_framework import serializers
from .models import User, SearchHistory, Keyword

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id','username']

class SearchHistorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model=SearchHistory
        fields = '__all__'

class KeywordSerializer(serializers.ModelSerializer):
    search_history = SearchHistorySerializer(many=True)
    class Meta:
        model=Keyword
        fields = ['name','count','search_history']


        
