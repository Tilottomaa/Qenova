from django.urls import path
from . import views

urlpatterns = [

    path('users/', views.user_list, name='user_list'),

    path('upload/', views.user_upload, name='user_upload'),
    path('update/<int:pk>/', views.update_user, name='update_user'),

    path('delete/<int:pk>/', views.delete_user, name='delete_user'),
    path('login/', views.login_user, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout'),
path(
    'organization/register/',views.organization_register,name='organization_register'
),

path(
    'organization/login/',views.organization_login,name='organization_login'
),

path(
    'organization/dashboard/',views.organization_dashboard,name='organization_dashboard'
),
path(
    'organization/logout/',
    views.organization_logout,
    name='organization_logout'
),

]