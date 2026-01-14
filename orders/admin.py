from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('product', 'quantity', 'size')
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemInline,)
    list_display = (
        'id',
        'full_name',
        'email',
        'order_total',
        'date',
    )
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
