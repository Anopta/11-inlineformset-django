from django.contrib import admin

# Register your models here.
from .models import *

class OrderInline(admin.StackedInline):
    '''Stacked Inline View for '''
    model = Order
    min_num = 0
    max_num = 3
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['date_created']
    inlines = [ OrderInline]

