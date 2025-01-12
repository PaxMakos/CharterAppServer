from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


@require_http_methods(["POST"])
@csrf_exempt
def loginToApp(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
    except KeyError:
        return JsonResponse({'status': 'error', 'message': 'Missing username or password'})

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid username or password'})


@require_http_methods(["POST"])
@csrf_exempt
def logoutFromApp(request):
    try:
        logout(request)
        return JsonResponse({'status': 'success'})
    except:
        return JsonResponse({'status': 'error', 'message': 'Logout failed'})


@require_http_methods(["POST"])
@csrf_exempt
def register(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
    except KeyError:
        return JsonResponse({'status': 'error', 'message': 'Missing username or password'})

    try:
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return JsonResponse({'status': 'success'})
    except ValidationError:
        return JsonResponse({'status': 'error', 'message': 'Invalid username or password'})
    except:
        return JsonResponse({'status': 'error', 'message': 'Registration failed'})