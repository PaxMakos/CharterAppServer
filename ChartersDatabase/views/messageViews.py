from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models import Chat, Message

@require_http_methods(["GET"])
@csrf_exempt
def getMessagesByChat(request):
    try:
        chat_title = request.GET.get("chat_title")
        chat = Chat.objects.filter(title=chat_title).first()
        messages = Message.objects.filter(chat=chat).order_by('sequence_number')
        messagesList = []
        for message in messages:
            messagesList.append({
                "id": message.id,
                "sequence_number": message.sequence_number,
                "content": message.content,
            })
        return JsonResponse({"status": "success", "messages": messagesList}, safe=False)
    except Chat.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Chat not found"}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)

@require_http_methods(["POST"])
@csrf_exempt
def createMessage(request):
    try:
        chat_title = request.POST.get("chat_title")
        content = request.POST.get("content")
        chat = Chat.objects.filter(title=chat_title).first()
        if chat is None:
            return JsonResponse({"status": "error", "message": "Chat not found"}, safe=False)
        message = Message.objects.create(chat=chat, content=content)
        return JsonResponse({"status": "success", "message": {
            "id": message.id,
            "sequence_number": message.sequence_number,
            "content": message.content,
        }}, safe=False)
    except Chat.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Chat not found"}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)