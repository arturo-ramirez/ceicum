from django.urls import path
from .views import CursoView, CursoNew, CursoEdit, CursoDel

urlpatterns = [
    path('curso/', CursoView.as_view(), name='curso_lista'),
    path('curso/new', CursoNew.as_view(), name='curso_new'),
    path('curso/edit/<int:pk>',
         CursoEdit.as_view(), name='curso_edit'),
    path('curso/delete/<int:pk>',
         CursoDel.as_view(), name='curso_delete'),
]
