from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models import Port


@require_http_methods(["GET"])
@csrf_exempt
def getPortsNames(request):
    ports = Port.objects.all()
    portsNames = [port.name for port in ports]
    return JsonResponse(portsNames, safe=False)


@require_http_methods(["GET"])
@csrf_exempt
def getPort(request):
    portName = request.GET.get("portName")
    port = Port.objects.get(name=portName)
    return JsonResponse(port.__dict__, safe=False)