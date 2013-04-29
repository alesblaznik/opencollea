from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from opencollea.models import Course


def login(request):
    dict = {
        "redirectTo": request.GET.get('next', '/')
    }
    return render_to_response('login.html', dict)


@login_required
def home(request):
    dict = {
        "user": request.user,
        "title": "Welcome",
        "content": "Vestibulum malesuada volutpat lorem vitae bibendum."
    }
    return render_to_response('home.html', dict)


@login_required
def courses(request):
    dict = {
        "user": request.user,
        "title": "Courses",
        "content": "We are very pleased to bla bla ...",
        'course_list': Course.objects.all(),
    }
    return render_to_response('courses.html', dict)


@login_required
def users(request):
    dict = {
        "user": request.user,
        "title": "Users",
        "content": "Feel free to communicate with OpenCollea's users ..."
    }
    return render_to_response('users.html', dict)


@login_required
def forums(request):
    dict = {
        "user": request.user,
        "title": "Forums",
        "content": "You won't take us alive!"
    }
    return render_to_response('forums.html', dict)
