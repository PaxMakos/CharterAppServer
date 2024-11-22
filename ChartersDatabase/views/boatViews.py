from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models import Boat


@require_http_methods(["GET"])
@csrf_exempt
def getBoatsByPort(request):
    try:
        portName = request.GET.get("portName")
        boats = Boat.objects.filter(motherPort__name=portName)
        boatsNames = [boat.name for boat in boats]
        return JsonResponse({"status": "success", "boats": boatsNames}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)


@require_http_methods(["GET"])
@csrf_exempt
def getBoatsByCompany(request):
    try:
        companyName = request.GET.get("companyName")
        boats = Boat.objects.filter(company=companyName)
        boatsNames = [boat.name for boat in boats]
        return JsonResponse({"status": "success", "boats": boatsNames}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)


@require_http_methods(["GET"])
@csrf_exempt
def getBoat(request):
    try:
        boatName = request.GET.get("boatName")
        boat = Boat.objects.get(name=boatName)
        return JsonResponse({"status": "success", "boat": boat.__dict__}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)