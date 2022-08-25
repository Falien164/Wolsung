from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.index2, name='index2'),
    path('all/', views.get_all_characters),
    path('<int:id>/', views.get_character),
]