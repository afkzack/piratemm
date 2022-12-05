from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'anime'

urlpatterns = [
	path('', views.index_view, name='index'),
	path('anime/', views.anime_view, name='anime'),
	path('anime/<int:anime_id>/', views.episode_view, name='episode'),
	path('anime/<int:episode_id>/watch/', views.watch_view, name='watch'),
	path('signup/', views.signup, name='signup'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
	path('premium/', views.premium_view, name='premium'),
	path('premium/<int:anime_id>/', views.pre_episode_view, name='pre_episode'),
	path('premium/<int:episode_id>/watch/', views.pre_watch_view, name='pre_watch'),
	path('searched_animes/', views.searched_animes, name='searched_animes'),
	path('maintenance/', views.maintenance_view, name='maintenance'),
]