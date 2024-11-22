from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models import Port


@require_http_methods(["GET"])
@csrf_exempt
def getPortsNames(request):
    try:
        ports = Port.objects.all()
        portsNames = [port.name for port in ports]
        return JsonResponse({"status": "success", "ports": portsNames}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)


@require_http_methods(["GET"])
@csrf_exempt
def getPort(request):
    try:
        portName = request.GET.get("portName")
        port = Port.objects.get(name=portName)
        return JsonResponse({"status": "success", "port": port.__dict__}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)