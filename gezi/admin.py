from django.contrib import admin

# Register your models here.
from gezi.models import Category, Gezi, Images
class GeziImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
class GeziAdmin(admin.ModelAdmin):
    list_display = ['city','title','category','image_tag', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status','category']
    inlines = [GeziImageInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'gezi','image']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Gezi,GeziAdmin)
admin.site.register(Images,ImagesAdmin)