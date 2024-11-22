from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models import Boat


@require_http_methods(["GET"])
@csrf_exempt
def getBoatsByPort(request):
    portName = request.GET.get("portName")
    boats = Boat.objects.filter(motherPort__name=portName)
    boatsNames = [boat.name for boat in boats]
    return JsonResponse(boatsNames, safe=False)


@require_http_methods(["GET"])
@csrf_exempt
def getBoatsByCompany(request):
    companyName = request.GET.get("companyName")
    boats = Boat.objects.filter(company=companyName)
    boatsNames = [boat.name for boat in boats]
    return JsonResponse(boatsNames, safe=False)


@require_http_methods(["GET"])
@csrf_exempt
def getBoat(request):
    boatName = request.GET.get("boatName")
    boat = Boat.objects.get(name=boatName)
    return JsonResponse(boat.__dict__, safe=False)