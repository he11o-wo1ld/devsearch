from django.urls import URLPattern, path
from .views import *


urlpatterns = [
    path('', projects, name='projects'),
    
    path('project/<str:pk>', project, name='project'),

    path('create-project/', createProject, name='create_project'),

    path('update-project/<str:pk>', updateProject, name='update_project'),

    path('delete-project/<str:pk>', deleteProject, name='delete_project'),
]
