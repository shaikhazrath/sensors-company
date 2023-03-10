from django.contrib import admin

from .models import *

@admin.register(Usecase)
class UsecaseModelAdmin(admin.ModelAdmin):
	list_display = ['category']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
	list_display = ['category','title']

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
	list_display = ['name','email','created_at']