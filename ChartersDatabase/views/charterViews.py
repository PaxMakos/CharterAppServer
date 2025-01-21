from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models import Charter, Boat
import datetime


@require_http_methods(["GET"])
@csrf_exempt
def getChartersByBoat(request):
    try:
        boatName = request.GET.get("boatName")
        charters = Charter.objects.filter(boat__name=boatName)

        chartersList = []
        for charter in charters:
            chartersList.append({
                "startDate": charter.startDate,
                "endDate": charter.endDate,
            })

        return JsonResponse({"status": "success", "charters": chartersList}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)


@require_http_methods(["GET"])
@csrf_exempt
def getChartersByUser(request):
    try:
        userName = request.GET.get("userName")
        user = User.objects.get(username=userName)
        charters = Charter.objects.filter(user=user)

        chartersList = []
        for charter in charters:
            chartersList.append({
                "boat": charter.boat.name,
                "startDate": charter.startDate,
                "endDate": charter.endDate,
                "price": charter.price,
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
        user = request.user

        if user.is_anonymous:
            user = User.objects.get(username=request.POST.get("userName"))

        if boatName is None or startDate is None or endDate is None:
            return JsonResponse({"status": "error", "message": "Missing parameters"}, safe=False)

        pricePerDay = Boat.objects.get(name=boatName).pricePerDay
        price = pricePerDay * (datetime.datetime.strptime(endDate, "%Y-%m-%d").date() - datetime.datetime.strptime(startDate, "%Y-%m-%d").date()).days

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

        return JsonResponse({"status": "error", "message": f"{type(e).__name__}: {str(e)}"}, safe=False)
