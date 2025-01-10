from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models import Charter, Boat
import datetime


@require_http_methods(["GET"])
@csrf_exempt
def getCharters(request):
    try:
        boatName = request.GET.get("boatName")
        charters = Charter.objects.filter(boat__name=boatName)

        chartersList = []
        for charter in charters:
            chartersList.append({
                "id": charter.id,
                "startDate": charter.startDate,
                "endDate": charter.endDate,
            })

        return JsonResponse({"status": "success", "charters": chartersList}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)


@require_http_methods(["POST"])
@csrf_exempt
def addCharter(request):
    try:
        boatName = request.POST.get("boatName")
        startDate = request.POST.get("startDate")
        endDate = request.POST.get("endDate")
        price = request.POST.get("price")
        user = request.user

        startDate = datetime.datetime.strptime(startDate, "%Y-%m-%d").date()
        endDate = datetime.datetime.strptime(endDate, "%Y-%m-%d").date()

        existingCharters = Charter.objects.filter(boat__name=boatName)
        for charter in existingCharters:
            if charter.startDate <= startDate <= charter.endDate or charter.startDate <= endDate <= charter.endDate:
                return JsonResponse({"status": "error", "message": "This boat is already chartered in this period"}, safe=False)

        Charter.objects.create(
            boat=Boat.objects.get(name=boatName),
            startDate=startDate,
            endDate=endDate,
            price=price,
            user=user
        )

        return JsonResponse({"status": "success", "message": "Charter added successfully"}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)
