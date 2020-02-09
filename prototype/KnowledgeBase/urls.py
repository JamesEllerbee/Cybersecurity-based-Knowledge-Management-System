from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/', views.question, name='question'),
    path('threats/', views.threats, name='threats'),
    path('answer/', views.answer, name='answer'),
]

