from django.urls import path
from user.views import *


urlpatterns = [
    path('update/', update_custom_user, name='update_user'),
    path('current/', get_current_user, name='current_user'),
    path('create/', create_custom_user, name='create_user'),
]