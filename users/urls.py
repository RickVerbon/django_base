
from django.urls import path
from users import views

urlpatterns = [
    path('register/', views.register_user, name='register-view'),
    path('login/', views.login_user, name='login-view'),
    path('logout/', views.logout_user, name='logout-view'),
]
