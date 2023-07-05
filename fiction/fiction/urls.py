"""
URL configuration for fiction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import URLPattern, path, include
from rest_framework import routers

from fiction_fullstack.views import BookViewSet, delete_book, update_book, add_book



router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

URLPattern

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
    path('books/<int:id>', delete_book, name="delete_book"), 
    path('books/', add_book, name="add_book"),
    path('books/update/<int:id>/', update_book, name="update_book"), 
    

]
