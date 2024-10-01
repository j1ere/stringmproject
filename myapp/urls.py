from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name=''),
    path('signup/', views.signup_view, name='signup'),
    path('stringm/', views.stringm, name='stringm'),
]
