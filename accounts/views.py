from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout as django_logout
from .forms import SignupForm, LoginForm
from .models import Profile, Follow
