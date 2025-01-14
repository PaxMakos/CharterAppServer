from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models import Chat, Message

@require_http_methods(["GET"])
@csrf_exempt
def getMessagesByChat(request):
    try:
        chat_id = request.GET.get("chat_id")
        messages = Message.objects.filter(chat_id=chat_id)
        messagesList = []
        for message in messages:
            messagesList.append({
                "id": message.id,
                "content": message.content,
                "timestamp": message.timestamp,
                "sender": message.sender,
            })

        return JsonResponse({"status": "success", "messages": messagesList}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)

@require_http_methods(["POST"])
@csrf_exempt
def createMessage(request):
    try:
        chat_id = request.POST.get("chat_id")
        content = request.POST.get("content")
        sender = request.POST.get("sender")
        chat = Chat.objects.get(id=chat_id)
        message = Message.objects.create(chat=chat, content=content, sender=sender)
        return JsonResponse({"status": "success", "message": {
            "id": message.id,
            "content": message.content,
            "timestamp": message.timestamp,
            "sender": message.sender,
        }}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)