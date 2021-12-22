from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="accounts_lgoin"),
    path('signup/', views.signup, name="accounts_signup"),
]
