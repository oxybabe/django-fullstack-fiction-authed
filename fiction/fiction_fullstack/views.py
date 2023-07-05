# from django.shortcuts import render
# from rest_framework import APIView
import json
from django.http import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
from .models import Book
from django.views.decorators.http import require_http_methods

# from rest_framework import generics

# Create your views here.

# class BookAPIView(APIView):
#     def get(self, request):
#         data = Book.objects.all()
#         serializer = BookSerializer(data, many=True )
#         return Response(serializer.data)

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
def update_book(request, id):
    if request.method == 'PATCH':
        Book.title = request.PATCH.get('title', Book.title)
        Book.description = request.PATCH.get('description', Book.description)
        Book.save()
        return render(request, 'frontend/index.html', {'id':id})
    else: return HttpResponseNotAllowed(['PATCH'])

        
def add_book(request):
    if request.method == 'POST':
        json_data = request.POST.get()
    return render(request, 'frontend/index.html')

def delete_book(request, id):
    id = id
    if request.method == 'DELETE':
        json_data = request.DELETE.get()
    return render(request, 'frontend/index.html', {'id':id})

# class BookUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer    

        
# https://www.youtube.com/watch?v=K8C2f1_e9VU    