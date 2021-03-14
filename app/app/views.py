from django.http import JsonResponse


def index(request):
    data = {"data": "Welcome to my udacity cloud devops capstone backend environment!"}
    return JsonResponse(data)


def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)
