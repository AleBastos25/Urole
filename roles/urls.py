from django.urls import path

from . import views

app_name = 'roles'
urlpatterns = [
    path('', views.list_roles, name='index'),
    path('search/', views.search_roles, name='search'), 
    path('create/', views.create_role, name='create'),
    path('<int:role_id>/', views.detail_role, name='detail'),
    path('update/<int:role_id>/', views.update_role, name='update'),
    path('delete/<int:role_id>/', views.delete_role, name='delete'),
    path('<int:role_id>/comment/', views.create_comment, name='comment'),
    path('lists/', views.ListListView.as_view(), name='lists'),
    path('lists/create', views.ListCreateView.as_view(), name='create-list'),
]