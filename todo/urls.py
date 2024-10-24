
from django.urls import path
from todo import views

urlpatterns = [
    path('',views.todo_list , name="todo_list"),
    path('create',views.create_todo ,name="create_todo"),
    path('completed/<int:todo_id>',views.complete_todo ,name="complete_todo"),
    path('deleted/<int:todo_id>',views.delete_todo ,name="delete_todo"),
    
]
