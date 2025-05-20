from json import JSONEncoder

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Daily, Weekly, Monthly, Yearly, LongTerm, User, Token

@csrf_exempt
def submit_daily(request):
    """user submits daily task here"""

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    Daily.objects.create(user=this_user, title=request.POST['title'], description=request.POST['description'],
                         time_needed=request.POST['time_needed'],)


    return JsonResponse({
        'status': 'success',

    }, encoder=JSONEncoder)

@csrf_exempt
def submit_weakly(request):
    """user submits weakly task here"""

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    Weekly.objects.create(user=this_user, title=request.POST['title'], description=request.POST['description'],
                         time_needed=request.POST['time_needed'],)


    return JsonResponse({
        'status': 'success',

    }, encoder=JSONEncoder)

@csrf_exempt
def submit_monthly(request):
    """user submits monthly task here"""

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    Monthly.objects.create(user=this_user, title=request.POST['title'], description=request.POST['description'],
                         time_needed=request.POST['time_needed'],)


    return JsonResponse({
        'status': 'success',

    }, encoder=JSONEncoder)

@csrf_exempt
def submit_yearly(request):
    """user submits yearly task here"""

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    Yearly.objects.create(user=this_user, title=request.POST['title'], description=request.POST['description'],
                         time_needed=request.POST['time_needed'],)


    return JsonResponse({
        'status': 'success',

    }, encoder=JSONEncoder)

@csrf_exempt
def submit_long(request):
    """user submits long task here"""

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    LongTerm.objects.create(user=this_user, title=request.POST['title'], description=request.POST['description'],
                         time_needed=request.POST['time_needed'],)

    return JsonResponse({
        'status': 'success',

    }, encoder=JSONEncoder)

