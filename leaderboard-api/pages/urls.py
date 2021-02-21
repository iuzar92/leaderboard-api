from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.redirect_view),
    url(r'^leaderboard$', views.leaderboard_view),
    
    # TODO Add urls for views
]