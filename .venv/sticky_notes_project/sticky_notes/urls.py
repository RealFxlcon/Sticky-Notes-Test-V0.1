from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),  # URL pattern for listing notes
    path('note/new/', views.note_create, name='note_create'),  # URL pattern for creating a new note
    path('note/<int:pk>/edit/', views.note_edit, name='note_edit'),  # URL pattern for editing a note
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),  # URL pattern for deleting a note
]