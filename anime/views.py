from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from .models import Anime, Episode, Genre, Author, Type, Watch
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.views import generic

from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect

@cache_page(60 * 15)
@csrf_protect

def base_view(request):
	return render(request, 'anime/base.html')

def index_view(request):
	return render(request, 'anime/index.html')

def anime_view(request):
	anime_list = Anime.objects.all()
	genre_list = Genre.objects.all()
	latest_anime_list = Anime.objects.order_by('-pub_date')[:4]
	context = {
		'anime_list': anime_list,
		'genre_list': genre_list,
		'latest_anime_list':latest_anime_list,
		}
	return render(request, 'anime/anime.html', context)

def episode_view(request, anime_id):
	anime = get_object_or_404(Anime, pk=anime_id)
	episode = Episode.objects.filter(anime=anime)
	genre = Genre.objects.all()
	context = {
		'anime': anime,
		'episode': episode,
		'genre': genre,
	}
	return render(request, 'anime/episode.html', context)

def watch_view(request, episode_id):
	episode = get_object_or_404(Episode, pk=episode_id)
	watch = Watch.objects.filter(episode=episode)
	context = {
	'episode':episode,
	'watch':watch
	}
	return render(request, 'anime/watch.html', context)

def signup(request):
	if request.method == 'POST':
		uname = request.POST.get('username')
		email = request.POST.get('email')
		pass1 = request.POST.get('password1')
		pass2 = request.POST.get('password2')

		if pass1 != pass2:
			return HttpResponse("Your passwords didn't match!")
		else:

			my_user = User.objects.create_user(uname, email, pass1)
			my_user.save()
			return redirect('/login')


	return render(request, 'anime/signup.html')

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		pass1 = request.POST.get('pass')
		user = authenticate(request, username=username, password=pass1)
		if user is not None:
			dj_login(request, user)
			return redirect('/premium')
		else:
			return HttpResponse('Invalid Queries!')	

	return render(request, 'anime/login.html')

@login_required(login_url='/login')
def premium_view(request):
	anime_list = Anime.objects.all()
	latest_anime_list = Anime.objects.order_by('-pub_date')[:5]
	context = {
		'anime_list': anime_list,
		'latest_anime_list':latest_anime_list,
		}
	return render(request, 'anime/premium.html', context)

@login_required(login_url='/login')
def pre_episode_view(request, anime_id):
	anime = get_object_or_404(Anime, pk=anime_id)
	episode = Episode.objects.filter(anime=anime)
	genre = Genre.objects.all()
	context = {
		'anime': anime,
		'episode': episode,
		'genre': genre,					
	}
	return render(request, 'anime/pre_episode.html', context)

@login_required(login_url='/login')
def pre_watch_view(request, episode_id):
	episode = get_object_or_404(Episode, pk=episode_id)
	watch = Watch.objects.filter(episode=episode)
	context = {
	'episode':episode,
	'watch':watch
	}
	return render(request, 'anime/pre_watch.html', context)

def logout(request):
	dj_logout(request)
	return redirect('/login')

def searched_animes(request):
	if request.method == "POST":
		searched = request.POST['searched']
		anime = Anime.objects.filter(title__contains=searched)
		return render(request, 'anime/searched_animes.html', {
			'searched':searched, 
			'anime':anime, 
			})
	else:
		return render(request, 'anime/searched_animes.html', {})

def maintenance_view(request):
	return render(request, 'anime/maintenance.html')