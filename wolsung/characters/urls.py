from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.add_character),
    path('all/', views.get_all_characters),
    path('<int:id>/', views.get_character),
]