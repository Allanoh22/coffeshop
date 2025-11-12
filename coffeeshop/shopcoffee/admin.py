from django.contrib import admin
from .models import MenuItem, Order, OrderItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name',)
    list_filter = ('category',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'created_at')
    list_filter = ('status',)
    date_hierarchy = ('created_at')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'menu_item', 'quantity')

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)

