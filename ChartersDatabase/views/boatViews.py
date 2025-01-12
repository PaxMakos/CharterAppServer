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
        toReturn = {
            "name": boat.name,
            "boatModel": boat.boatModel,
            "productionYear": boat.productionYear,
            "length": boat.length,
            "width": boat.width,
            "draft": boat.draft,
            "company": boat.company,
            "contactEmail": boat.contactEmail,
            "contactPhone": boat.contactPhone,
            "motherPort": boat.motherPort.name,
            "beds": boat.beds,
            "pricePerDay": boat.pricePerDay,
            "description": boat.description
        }

        return JsonResponse({"status": "success", "boat": toReturn}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)


@require_http_methods(["GET"])
@csrf_exempt
def getAllBoats(request):
    try:
        boats = Boat.objects.all()
        boatsData = [
            {
                "name": boat.name,
                "boatModel": boat.boatModel,
                "productionYear": boat.productionYear,
                "length": boat.length,
                "width": boat.width,
                "draft": boat.draft,
                "company": boat.company,
                "motherPort": boat.motherPort.name if boat.motherPort else None,
                "beds": boat.beds,
                "pricePerDay": boat.pricePerDay,
                "description": boat.description,
            }
            for boat in boats
        ]
        return JsonResponse({"status": "success", "boats": boatsData}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)

@require_http_methods(["GET"])
@csrf_exempt
def getAllBoatsNames(request):
    try:
        boats = Boat.objects.all()
        boatsNames = [boat.name for boat in boats]
        return JsonResponse({"status": "success", "boats": boatsNames}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)