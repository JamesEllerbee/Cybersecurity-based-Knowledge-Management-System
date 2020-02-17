from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/', views.question, name='question'),
    path('threats/', views.threats, name='threats'),
    path('results/', views.results, name='results'),
    path('answer/', views.answer, name='answer'),
    #path('threats/', views.ThreatListView.as_view(), name='threats'),
    path('threat/<int:pk>', views.ThreatDetailView.as_view(), name='threat-detail'),
]

