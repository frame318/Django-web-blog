from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/<int:id>', views.view, name='view'),
]
