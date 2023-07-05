from django.db import models
from django.apps import apps
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField(max_length=100)

def create_group_and_permissions():
    librarians_group, created = Group.objects.get_or_create(name="Librarians")

    Book = apps.get_model('fiction_fullstack', 'Book')  # Replace 'yourappname' with the name of your application
    book_content_type = ContentType.objects.get_for_model(Book)

    add_permission,  = Permission.objects.get_or_create(codename="add_book", name="can add book", content_type=book_content_type)
    change_permission,  = Permission.objects.get_or_create(codename="change_book", name="can change book",  content_type=book_content_type)
    delete_permission,  = Permission.objects.get_or_create(codename="delete_book", name="can delete book",  content_type=book_content_type)

    librarians_group.permissions.add(add_permission, change_permission, delete_permission)

    user = User.objects.get(username='elia')
    user.groups.add(librarians_group)