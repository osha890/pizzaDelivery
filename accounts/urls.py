from django.urls import path, include

from .views import home, signup

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
]
