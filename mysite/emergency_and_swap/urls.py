from django.urls import path
form .import views

urlpatterns =[
path('emergency/submit/<int:token_id>/', views.submit_emergency_view, name='submit_emergency'),
    ]