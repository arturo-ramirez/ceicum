from django.urls import path
from .views import AlumnoView, AlumnoNew, AlumnoEdit, AlumnoDelete
from alumno import views

urlpatterns = [
    path('alumno/', AlumnoView.as_view(), name='alumno_lista'),
    path('alumno/new', AlumnoNew.as_view(), name='alumno_new'),
    path('alumno/edit/<int:pk>', AlumnoEdit.as_view(), name='alumno_edit'),
    path('alumno/delete/<int:pk>', AlumnoDelete.as_view(), name='alumno_delete'),

    path('alumno/password/', views.codigo, name='password'),
]
