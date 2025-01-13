from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models import Chat, Message

@require_http_methods(["GET"])
@csrf_exempt
def getAllChats(request):
    try:
        chats = Chat.objects.all()
        chatsList = []
        for chat in chats:
            chatsList.append({
                "id": chat.id,
                "title": chat.title,
            })

        return JsonResponse({"status": "success", "chats": chatsList}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)

@require_http_methods(["POST"])
@csrf_exempt
def createChat(request):
    try:
        title = request.POST.get("title")
        chat = Chat.objects.create(title=title)
        return JsonResponse({"status": "success", "chat": {"id": chat.id, "title": chat.title}}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)