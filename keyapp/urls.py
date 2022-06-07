from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup),
    path('add/', views.add_book),
    path('delete/<int:id>', views.delete_book),
    path('edit/<int:id>', views.change_book),
    path('logout/', views.Signout),
    path('library', views.StudentView)
]
