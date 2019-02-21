#importing admin fucntion and info from book class

from django.contrib import admin
from .models import Book

# Register your models here.
admin.site.register(Book)