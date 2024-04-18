from django.urls import path, include
from . import views

app_name = 'pdfhub'

urlpatterns = [
    path('', views.home, name='home_view'),
    path('login/', views.login, name='login_view'),
    path('register/', views.register, name='register_view'),
    path('fetch_answer/', views.fetch_answer, name='fetch_answer'),
]
