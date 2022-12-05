from django.contrib import admin
from .models import Anime, Episode, Genre, Type, Watch, Author


admin.site.register(Anime)
admin.site.register(Episode)
admin.site.register(Genre)
admin.site.register(Type)
admin.site.register(Watch)
admin.site.register(Author)