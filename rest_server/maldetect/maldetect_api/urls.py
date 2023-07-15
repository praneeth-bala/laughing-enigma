# todo/todo_api/urls.py : API urls.py
from django.urls import path
from .views import (
    XMLApiView,
)

urlpatterns = [
    path('api', XMLApiView.as_view()),
]