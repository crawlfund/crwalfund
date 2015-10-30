from django.contrib import admin
from homepage.models import Category,Page,UserProfile

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)
admin.site.register(Page)
admin.site.register(UserProfile)

