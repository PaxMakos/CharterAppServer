from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models import Charter


@require_http_methods(["GET"])
@csrf_exempt
def getCharters(request):
    boatName = request.GET.get("boatName")
    charters = Charter.objects.filter(boat__name=boatName)

    chartersList = []
    for charter in charters:
        chartersList.append({
            "id": charter.id,
            "startDate": charter.startDate,
            "endDate": charter.endDate,
        })

    return JsonResponse(chartersList, safe=False)


@require_http_methods(["POST"])
@csrf_exempt
def addCharter(request):
    boatName = request.POST.get("boatName")
    startDate = request.POST.get("startDate")
    endDate = request.POST.get("endDate")
    price = request.POST.get("price")
    user = request.user

    charter = Charter.objects.create(
        boat__name=boatName,
        startDate=startDate,
        endDate=endDate,
        price=price,
        user=user
    )

    return JsonResponse(charter.__dict__, safe=False)