from django.contrib import admin
from .models import Products,Order
# Register your models here.


class ProductDisplay(admin.ModelAdmin):

	def change_category_to_default(self,request,queryset):
		queryset.update(category='default')
	change_category_to_default.short_description = 'Default Category'   # we reduced the length and made it simpler to displat it in action list
	list_display = ('title','price','category')
	search_fields = ('category',)
	actions = ('change_category_to_default',)
	fields = ('title', 'price')    # shows only these fields upon clicking them
	list_editable = ('price',)    # this makes the fields editable i,e list_display fields can be edited then and there
admin.site.site_header = "E-commerce site"
admin.site.site_title = "E-commerce"
admin.site.index_title = "E-commerce Management"
admin.site.register(Products,ProductDisplay)
admin.site.register(Order)
