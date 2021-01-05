from django.contrib import admin
from .models import Articles
# Register your models here.
def show_login_name(modeladmin,request,queryset):
    print(request.user.username)
class ArticleAdmin(admin.ModelAdmin):
    actions = [show_login_name]
    # fileds=("title","author","content")
    exclude = ('visited',)
    list_display = ("title","author","img","abstract","content","visited","created_at","modified_at")
    search_fields = ('title',)
    # list_filter = ('created_at')
    list_filter = ("created_at",)

show_login_name.short_description = "打印当前登陆的用户"
admin.site.register(Articles,ArticleAdmin)