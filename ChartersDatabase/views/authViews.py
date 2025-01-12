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


@require_http_methods(["GET"])
@csrf_exempt
def getUser(request):
    try:
        user = request.user
        return JsonResponse({'status': 'success', 'username': user.username, 'email': user.email})
    except:
        return JsonResponse({'status': 'error', 'message': 'User not found'})


@require_http_methods(["POST"])
@csrf_exempt
def changePassword(request):
    try:
        oldPassword = request.POST['oldPassword']
        newPassword = request.POST['newPassword']
    except KeyError:
        return JsonResponse({'status': 'error', 'message': 'Missing old or new password'})

    user = request.user
    if user.check_password(oldPassword):
        user.set_password(newPassword)
        user.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid old password'})


@require_http_methods(["POST"])
@csrf_exempt
def changeEmail(request):
    try:
        newEmail = request.POST['newEmail']
    except KeyError:
        return JsonResponse({'status': 'error', 'message': 'Missing new email'})

    user = request.user
    user.email = newEmail
    user.save()
    return JsonResponse({'status': 'success'})