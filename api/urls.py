from .views import *
from django.urls import path

urlpatterns = [
  path('', getRoutes, name="routes"),
  path('notes/', getNotes, name="notes"),
  path('notes/create/', createNote, name="create-note"),
  path('notes/<str:pk>/', getNote, name="note"),
  path('notes/<str:pk>/update/', updateNote, name="update-note"),
  path('notes/<str:pk>/delete/', deleteNote, name="delete-note"),

]