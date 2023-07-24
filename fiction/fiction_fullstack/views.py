# from django.shortcuts import render
# from rest_framework import APIView
import genericpath
from urllib import request
from django.http import HttpResponseNotAllowed
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
from .models import Book
from urllib.request import urlopen

# import urllib.request as urllib

from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from rest_framework import generics

# Create your views here.

# class BookAPIView(APIView):
#     def get(self, request):
#         data = Book.objects.all()
#         serializer = BookSerializer(data, many=True )
#         return Response(serializer.data)

class BookViewSet(ModelViewSet):
    model = Book
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

# user = authenticate(urllib.request, username='elia', password='password123')



# login(request, user)
# logout(request)

# librarians_group = Group.objects.create(name="Librarians")
# book_content_type = ContentType.objects.get(app_label="auth", model='book')
# add_permission = Permission.objects.get(codename="add_book", name="can add book", content_type=book_content_type)
# change_permission = Permission.objects.get(codename="change_book", name="can change book",  content_type=book_content_type)
# delete_permission = Permission.objects.get(codename="delete_book", name="can delete book",  content_type=book_content_type)
# librarians_group.permissions.add(add_permission, change_permission, delete_permission)
# librarians_group.save()

# user = User.objects.get(username='elia')
# user.groups.add(librarians_group)

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer

# class BookUpdateAPIView(genericpath.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer    

        
# https://www.youtube.com/watch?v=K8C2f1_e9VU    