from django.urls import path
from mysite.views import home, add_todo, delete_todo, edit_todo 
# importing functions from views.py

urlpatterns = [
    path('', home, name='home'), # End point (By Default First url when user visit on the website)
    path('add_todo/', add_todo, name='add_todo'),
    path('delete_todo/<int:todo_id>', delete_todo, name='delete_todo'),
    path('edit_todo/<int:todo_id>', edit_todo, name='edit_todo'),
]