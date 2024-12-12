from django.contrib.auth.models import User
from django.shortcuts import render

from createppt.models import PPT


def index(request):

    user_count = User.objects.count()
    ppt_count = PPT.objects.count()

    context = {
        'user_count': user_count,
        'ppt_count': ppt_count,
    }

    return render(request, 'Mentor/about.html', context)
