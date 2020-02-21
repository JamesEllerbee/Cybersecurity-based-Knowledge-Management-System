from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/', views.question, name='question'),
    path('threats/', views.threats, name='threats'),
    path('results/', views.results, name='results'),
    path('results/<int:question_id>/answer/', views.answer, name='answer'),
    path('results/submitQuestion/', views.submitQuestion, name='submitQuestion'),
    path('answer/', views.answer, name='answer'),
    path('threat/<int:pk>', views.ThreatDetailView.as_view(), name='threat-detail'),
    path('results/<int:question_id>/answer/submitAnswer', views.submitAnswer, name='submitAnswer'),
]