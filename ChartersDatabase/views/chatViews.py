from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models import Chat

@require_http_methods(["GET"])
@csrf_exempt
def getAllChats(request):
    try:
        chats = Chat.objects.all()
        chatsList = [{"id": chat.id, "title": chat.title} for chat in chats]
        return JsonResponse({"status": "success", "chats": chatsList}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)

@require_http_methods(["POST"])
@csrf_exempt
def createChat(request):
    try:
        title = request.POST.get("title")
        if not title:
            return JsonResponse({"status": "error", "created": False, "message": "Title is required"}, safe=False)
        chat = Chat.objects.create(title=title)
        return JsonResponse({"status": "success", "created": True, "chat": {"id": chat.id, "title": chat.title}}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "created": False, "message": str(e)}, safe=False)