from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.homepage, name="home"),
    path("home", views.homepage, name="home"),
    path("home/", views.homepage, name="home"),
    path("words_list", views.words_listpage, name="wlist"),
    path("words_list/", views.words_listpage, name="wlist"),
    path("add_word", views.add_wordpage, name="aword"),
    path("add_word/", views.add_wordpage, name="aword"),
]