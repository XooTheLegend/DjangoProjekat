from django.urls import path
from . import views

app_name = 'demo_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('practices/', views.practices, name='practices'),
    path('practice/<int:id>', views.practice, name='practice'),
    path('practice/edit/<int:id>', views.edit, name='edit'),
    path('practice/new/', views.new, name='new')
]