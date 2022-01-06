from django.urls import path
from . import views
urlpatterns = [
    path('', views.loginUser, name="login"),
	path('signup/', views.signup, name="signup"),
	path('logout/', views.logoutUser, name="logout"),
	path('home/', views.home, name="home"),
]