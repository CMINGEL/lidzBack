from django.urls import path
from . import views 

urlpatterns = [
    path('clients/', views.ClientView.as_view()),
    path('clients/<int:pk>/', views.ClientView.as_view()),
    path('debts/', views.DebtView.as_view()),
    path('messages/', views.MessaggeView.as_view()),
    path('messages/<int:pk>/', views.MessaggeView.as_view()),
]

