from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.main_page),
    path('index/<int:article_id>/',views.article_page,name='article_page'),
    path('index/edit/<int:article_id>/',views.edit_page,name="edit_page"),
    path('index/edit/action',views.edit_action,name='edit_action')
]
