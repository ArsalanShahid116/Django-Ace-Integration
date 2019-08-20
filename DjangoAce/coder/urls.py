from django.urls import path
from .views import (
        code_list, 
        code_detail, 
        CodeCreate, 
        CodeUpdate,
        CodeDelete)
from django.contrib.auth import views as auth_views

app_name = 'coder'

urlpatterns = [
        path('', code_list.as_view(), name='code_list'),
        path('<int:id>/',
            code_detail.as_view(),
            name='code_detail'),
        path('create/', CodeCreate.as_view(), name='code_create'),
        path('<int:id>/update/', CodeUpdate.as_view(), name='code_update'),
        path('<int:id>/delete/', CodeDelete.as_view(), name='code_delete'),
        ]


