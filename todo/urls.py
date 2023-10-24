from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.TodoList.as_view(), name='todo-list'),
    path('todo/novo/', views.TodoCreate.as_view(), name='todo-create'),
    path('todo/edit/<int:pk>/', views.TodoEdit.as_view(), name='todo-edit'),
    path('todo/delete/<int:pk>', views.TodoDelete.as_view(), name='todo-delete')
]