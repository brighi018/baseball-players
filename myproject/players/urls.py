from django.urls import path
from . import views

app_name = 'players'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('player/<int:pk>/', views.PlayerView.as_view(), name='player'),
    path('team/<int:pk>/', views.TeamView.as_view(), name='team'),
]

# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('player/<int:pk>/', views.PlayerView.as_view(), name='player'),
#     path('player2/<int:pk>/', views.player_view, name='player_view'),
#     path('team/<int:pk>/', views.TeamView.as_view(), name='team'),
#     path('async_view/', views.async_view, name='async_view')
# ]