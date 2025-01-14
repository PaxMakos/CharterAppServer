from django.http import JsonResponse, FileResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from ..models import Boat, Photo


@require_http_methods(["GET"])
@csrf_exempt
def getBoatPhotos(request):
    try:
        boatName = request.GET.get("boatName")
        boat = Boat.objects.get(name=boatName)
        photos = Photo.objects.filter(boat=boat)
        photosUrls = [photo.photo.url.split('/')[-1] for photo in photos]
        return JsonResponse({"status": "success", "photos": photosUrls}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)

@require_http_methods(["GET"])
@csrf_exempt
def getPhoto(request, img_name):
    try:
        print(img_name)
        photo = Photo.objects.get(photo__contains=img_name)

        file_extension = photo.photo.name.split('.')[-1].lower()
        content_type = f'image/{file_extension}'

        return FileResponse(photo.photo.open(), content_type=content_type)
    except Photo.DoesNotExist:
        raise Http404("Photo not found")
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)