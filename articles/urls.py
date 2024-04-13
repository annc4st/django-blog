
from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path('', views.article_list, name="article_list" ),
    path('create/', views.article_create, name="create"),
    path("<int:article_id>/", views.article_detail, name="article_detail"),
    
]