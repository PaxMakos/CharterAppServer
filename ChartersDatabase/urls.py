from django.urls import path
from .views import boatViews, charterViews, portViews, authViews, photoViews, chatViews

urlpatterns = [
    path('login/', authViews.loginToApp),
    path('logout/', authViews.logoutFromApp),
    path('register/', authViews.register),
    path('getUser/', authViews.getUser),
    path('changePassword/', authViews.changePassword),
    path('changeEmail/', authViews.changeEmail),
    path('boats/', boatViews.getAllBoats),
    path('boats/byPort/', boatViews.getBoatsByPort),
    path('boats/byCompany/', boatViews.getBoatsByCompany),
    path('boats/details/', boatViews.getBoat),
    path('charters/ByBoat/', charterViews.getChartersByBoat),
    path('charters/ByUser/', charterViews.getChartersByUser),
    path('charters/add/', charterViews.addCharter),
    path('ports/', portViews.getPorts),
    path('port/details/', portViews.getPort),
    path('boatPhotos/', photoViews.getBoatPhotos),
    path('photos/<str:img_name>/', photoViews.getPhoto),
    path('chat/getUserChats/', chatViews.getUserChats),
    path('chat/getBoatChats/', chatViews.getBoatChats),
    path('chat/getChatMessages/', chatViews.getChatMessages),
    path('chat/sendMessage/', chatViews.sendMessage)
    ]
