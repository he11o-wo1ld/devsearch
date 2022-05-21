from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>', views.userProfile, name='user-profiles'),
    path('account/', views.userAccount, name="account"),
    path('edit-account/', views.editAccount, name="edit"),
    path('create-skill/', views.createSkill, name="createSkill"),
    path('update-skill/<str:pk>', views.updateSkill, name="updateSkill"),
    path('delete-skill/<str:pk>', views.deleteSkill, name="deleteSkill"),
]
