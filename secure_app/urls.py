from django.urls import path,re_path
from . import views

urlpatterns = [
    path('list/', views.object_list, name='object_list'),
    re_path('(?P<pk>\d+)/', views.object_detail, name='detail'),
    re_path('<int:object_id>/change/', views.object_change, name='object_change'),
    re_path('object/<int:object_id>/delete/', views.object_delete, name='object_delete'),
]

