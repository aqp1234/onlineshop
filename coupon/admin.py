from django.contrib import admin
from .models import Coupon


# Register your models here.

class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'use_from_date', 'use_to_date', 'amount', 'active']
    list_filter = ['active', 'use_from_date', 'use_to_date']
    search_fields = ['code']


admin.site.register(Coupon, CouponAdmin)
