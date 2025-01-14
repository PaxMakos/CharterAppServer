from django.urls import path
from .views import boatViews, charterViews, portViews, authViews, photoViews, chatViews, messageViews


urlpatterns = [
    path('login/', authViews.loginToApp, name='login'),
    path('logout/', authViews.logoutFromApp, name='logout'),
    path('register/', authViews.register, name='register'),
    path('getUser/', authViews.getUser),
    path('changePassword/', authViews.changePassword),
    path('changeEmail/', authViews.changeEmail),
    path('boats/', boatViews.getAllBoats, name='getAllBoats'),
    path('boats/byPort/', boatViews.getBoatsByPort, name='getBoatsByPort'),
    path('boats/byCompany/', boatViews.getBoatsByCompany, name='getBoatsByCompany'),
    path('boats/details/', boatViews.getBoat, name='getBoat'),
    path('charters/ByBoat/', charterViews.getChartersByBoat, name='getChartersByBoat'),
    path('charters/ByUser/', charterViews.getChartersByUser, name='getChartersByUser'),
    path('charters/add/', charterViews.addCharter, name='addCharter'),
    path('ports/', portViews.getPorts, name='getPorts'),
    path('port/details/', portViews.getPort, name='getPort'),
    path('boatPhotos/', photoViews.getBoatPhotos, name='getBoatPhotos'),
    path('photos/<str:img_name>/', photoViews.getPhoto, name='getPhoto'),
    path('chats/', chatViews.getAllChats),
    path('chats/create/', chatViews.createChat),
    path('messages/', messageViews.getMessagesByChat),
    path('messages/create/', messageViews.createMessage),
    ]
