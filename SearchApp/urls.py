from django.urls import path
from . import views
urlpatterns = [
	path('searchQuery/', views.searchQuery, name="searchQuery"),
	path('saveQuery/', views.saveQuery, name="saveQuery"),
	path('editQuery/<int:pk>/', views.editQuery, name="editQuery"),
	path('update/', views.update, name="update"),
]