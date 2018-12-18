from django.contrib import admin
from .models import YtArticle

#注册类，在admin登录时展示用，不加这个admin.site.register(YtArticle)则只展示title（models中__str__方法给出的）
class YtArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pubtime','content') #展示字段
    list_filter = ('pubtime',) #过滤器，参数必须是元祖或列表
    
admin.site.register(YtArticle,YtArticleAdmin)