from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from .models import User

# TODO Create views
"""
View: /leaderboard
View: /leaderboard/{country_iso_code}
View: /score/submit
View: /user/profile/{user_guid}
View: /user/create
"""


# Redirect base domain requests to /leaderboard
def redirect_view(request):
    return redirect('/leaderboard')


# Default View [/leaderboard]
def leaderboard_view(request):
    return HttpResponse("<h1 style='color:maroon'>Django Project Boilerplate</h1><hr><h3>This is the default HTTP response for development purposes.</h3>")
