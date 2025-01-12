from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from ChartersDatabase.models import Chat


@require_http_methods(["GET"])
@csrf_exempt
def getUserChats(request):
    try:
        user = request.user
        chats = Chat.objects.filter(user=user)

        chatsList = []
        for chat in chats:
            chatsList.append({
                "id": chat.id,
                "boat": chat.boat.name,
                "user": chat.user.username
            })

        return (JsonResponse({"status": "success", "chats": chatsList}, safe=False))
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)


@require_http_methods(["GET"])
@csrf_exempt
def getBoatChats(request):
    try:
        user = request.user
        chats = Chat.objects.filter(boat__user=user)

        chatsList = []
        for chat in chats:
            chatsList.append({
                "id": chat.id,
                "boat": chat.boat.name,
                "user": chat.user.username
            })

        return (JsonResponse({"status": "success", "chats": chatsList}, safe=False))
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)


@require_http_methods(["GET"])
@csrf_exempt
def getChatMessages(request):
    try:
        chatId = request.GET.get("chatId")
        chat = Chat.objects.get(id=chatId)
        messages = chat.message_set.all()

        messagesList = []
        for message in messages:
            messagesList.append({
                "sender": message.sender,
                "message": message.message,
                "date": message.date
            })

        return JsonResponse({"status": "success", "messages": messagesList}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)


@require_http_methods(["POST"])
@csrf_exempt
def sendMessage(request):
    pass