from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Avg

from .forms import RegisterForm
from .models import Profile

from skills.models import Skill
from requests.models import ServiceRequest, Review


# 🏠 Home Page
def home(request):
    return render(request, 'accounts/home.html')


# 📝 Signup
def signup(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = RegisterForm()

    return render(
        request,
        'accounts/signup.html',
        {'form': form}
    )


# 🔐 Login
def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/')

        else:

            return render(
                request,
                'accounts/login.html',
                {
                    'error':
                    'Invalid username or password'
                }
            )

    return render(
        request,
        'accounts/login.html'
    )


# 🚪 Logout
def user_logout(request):

    logout(request)

    return redirect('/')


# 👤 My Profile
@login_required
def profile(request):

    profile = request.user.profile

    if request.method == 'POST':

        profile.bio = request.POST.get('bio')

        profile.skills_offered = request.POST.get(
            'skills_offered'
        )

        profile.skills_needed = request.POST.get(
            'skills_needed'
        )

        # profile image
        if request.FILES.get('profile_picture'):

            profile.profile_picture = request.FILES.get(
                'profile_picture'
            )

        profile.save()

        return redirect('/profile/')

    return render(
        request,
        'accounts/profile.html',
        {'profile': profile}
    )


# 📊 Dashboard
@login_required
def dashboard(request):

    my_skills = Skill.objects.filter(
        user=request.user
    )

    sent_requests = ServiceRequest.objects.filter(
        sender=request.user
    )

    received_requests = ServiceRequest.objects.filter(
        receiver=request.user
    )

    reviews = Review.objects.filter(
        reviewed_user=request.user
    )

    average_rating = reviews.aggregate(
        Avg('rating')
    )['rating__avg']

    return render(
        request,
        'accounts/dashboard.html',
        {
            'my_skills': my_skills,
            'sent_requests': sent_requests,
            'received_requests': received_requests,
            'reviews': reviews,
            'average_rating': average_rating,
        }
    )


# 🌍 PUBLIC PROFILE
def public_profile(request, username):

    user = get_object_or_404(
        User,
        username=username
    )

    profile = user.profile

    skills = Skill.objects.filter(
        user=user
    )

    reviews = Review.objects.filter(
        reviewed_user=user
    )

    average_rating = reviews.aggregate(
        Avg('rating')
    )['rating__avg']

    return render(
        request,
        'accounts/public_profile.html',
        {
            'profile_user': user,
            'profile': profile,
            'skills': skills,
            'reviews': reviews,
            'average_rating': average_rating,
        }
    )