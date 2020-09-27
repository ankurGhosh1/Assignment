from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
import requests 
from django.contrib.auth.models import User, auth
from .models import Favourites
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import HttpResponse
from django.db import models

# Create your views here.

@csrf_exempt
def signup(requests):
    if requests.method == 'POST':
        username = requests.POST['uname']
        firstname = requests.POST['firstname']
        lastname = requests.POST['lastname']
        email = requests.POST['email']
        password = requests.POST['password']
        user = User(
            username= username, 
            first_name=firstname, 
            last_name=lastname, 
            password=password,
            email= email
            )
        user.set_password(password)
        user.save()
    return JsonResponse({"message": "User Registered"})


@csrf_exempt
def check(requests):
    if requests.method == 'POST':
        email = requests.POST['email']
        if (User.objects.filter(email=email).exists()):
            username = ""
            details = User.objects.filter(email=email).values('username')
            for i in details:
                username = i['username']
            return JsonResponse({"message": 
                                    {"user_id": username, 
                                    "login_type": "signin"}
                                })
        else:
            return JsonResponse({"message": 
                                    {"user_id": "not registered", 
                                    "login_type": "signup"}
                                })


@csrf_exempt
def login(requests):
    if requests.method == 'POST':
        username = requests.POST['uname']
        password = requests.POST['password']
        
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(requests, user)
        return JsonResponse({"message": "login successful"})
    else:
        return JsonResponse({"message": "failed"})


@csrf_exempt
def getdetails(requests):
    if requests.method == 'POST':
        username = requests.POST['uname']
        user = User.objects.filter(username=username).values('email', 'first_name', 'last_name', 'id')
        details = list(user)
        id_num = User.objects.filter(username=username).values('id')
        user_id = id_num[0]['id']
        print(user_id)
        favourites = Favourites.objects.filter(user_id = user_id).values('favourites')
        all_favs = list(favourites)
        print(all_favs)
        all_details = details + all_favs

    return JsonResponse(all_details, safe=False)


@csrf_exempt
def addDetails(requests):
    if requests.method == 'POST':
        username = requests.POST['uname']
        user_id = User.objects.get(username = username)
        favourites = Favourites(
            user = user_id,
            favourites = requests.POST['fav']
        )
        favourites.save()

        all_favourites = Favourites.objects.filter(user_id = user_id).values('favourites')
        print(all_favourites)
        newallfavourites = list(all_favourites)

    return JsonResponse(newallfavourites, safe=False)


@csrf_exempt
def delete(requests):
    if requests.method == 'POST':
        username = requests.POST['uname']
        fav = requests.POST['fav']
        user_id = User.objects.get(username = username)
        remove = Favourites.objects.filter(favourites=fav).delete()
        all_favourites = Favourites.objects.filter(user_id = user_id).values('favourites')
    return JsonResponse({"message": "done"})