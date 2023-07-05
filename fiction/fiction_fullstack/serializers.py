# from rest_framework import serializers

# class BookSerializer(serializers.Serializer):
#     title=serializers.CharField(label="Enter Book Title")
#     author=serializers.CharField(label="Enter Book Author")
#     description=serializers.TextField(label="Enter Book Description")

from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
