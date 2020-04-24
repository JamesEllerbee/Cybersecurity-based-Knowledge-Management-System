from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/', views.question, name='question'),
    path('threats/', views.threats, name='threats'),
    path('threats/submitThreat/<str:assetName>', views.submitThreat, name='submitThreat'),
    path('threats/submitTreat/<str:theAssetName>/submitSuccess', views.addNewThreat, name='threatSubmitResult'),
    path('results/', views.results, name='results'),
    path('results/<int:question_id>/answer/', views.answer, name='answer'),
    path('results/answer/<int:question_id>/submitSuccess/', views.addNewAnswer, name='submitAnswer'),
    path('results/submitQuestion/', views.submitQuestion, name='submitQuestion'),
    path('answer/', views.answer, name='answer'),
    #path('threats/', views.ThreatListView.as_view(), name='threats'),
    path('threat/<int:threatId>', views.threatDetail, name='threat-detail'),
    path('results/vote/answer/<int:answer_id>/<str:scoreChange>', views.updateScore, name ='updateScore'),
]