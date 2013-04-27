from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from opencollea.models import Course

@login_required(login_url='/portal/login/')
def home(request):
    dict = {
        "user": request.user,
        "title": "Welcome",
        "content": "Pellentesque dapibus faucibus tortor at ornare. Sed interdum sodales vulputate. Nam egestas cursus est, vitae lacinia ligula convallis et. Suspendisse nec libero justo. Phasellus consectetur convallis sem, nec commodo leo sollicitudin at. Proin ultricies arcu ut ipsum ullamcorper sed placerat tortor porttitor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Duis quis justo in eros molestie viverra et at felis.\n\
        <p/>Nullam tellus dui, semper eu mattis nec, consectetur in sem. Vestibulum malesuada volutpat lorem vitae bibendum. Duis et dui purus. Morbi id ligula nec nibh dignissim adipiscing. Nam sit amet feugiat nisi. Cras vel faucibus turpis. In purus tellus, volutpat at pulvinar id, consectetur at quam. Nullam blandit dolor nisl, sit amet tincidunt orci. Aenean ipsum nulla, volutpat nec condimentum ac, faucibus et dolor. Quisque scelerisque, augue quis egestas rutrum, enim enim tincidunt lorem, ac consectetur odio velit id odio. Aliquam facilisis fermentum vehicula. Nunc in ipsum in ante porttitor porttitor. Donec rutrum ligula elementum magna pharetra eget aliquam lacus tempor. Proin lacus turpis, euismod sed consequat lobortis, hendrerit ut dolor. Quisque non odio at orci dignissim accumsan."
    }
    return render_to_response('home.html', dict)

@login_required(login_url='/portal/login/')
def courses(request):
    dict = {
        "user": request.user,
        "title": "Courses",
        "content": "We are very pleased to bla bla ...",
        'course_list': Course.objects.all(),
    }
    return render_to_response('courses.html', dict)

@login_required(login_url='/portal/login/')
def users(request):
    dict = {
        "user": request.user,
        "title": "Users",
        "content": "Feel free to communicate with OpenCollea's users ..."
    }
    return render_to_response('users.html', dict)

@login_required(login_url='/portal/login/')
def forums(request):
    dict = {
        "user": request.user,
        "title": "Forums",
        "content": "You won't take us alive!"
    }
    return render_to_response('forums.html', dict)
