from django.urls import path
from . import views

urlpatterns = [
    path('subject/<subject>', views.dynamic_endpoint, name='dynamic_endpoint'),
]
