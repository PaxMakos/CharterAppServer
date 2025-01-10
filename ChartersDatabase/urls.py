from django.urls import path
from .views import boatViews, charterViews, portViews, authViews, photoViews


urlpatterns = [
    path('login/', authViews.loginToApp),
    path('logout/', authViews.logoutFromApp),
    path('register/', authViews.register),
    path('boats/', boatViews.getAllBoats),
    path('boats/byPort/', boatViews.getBoatsByPort),
    path('boats/byCompany/', boatViews.getBoatsByCompany),
    path('boats/details/', boatViews.getBoat),
    path('charters/', charterViews.getCharters),
    path('charters/add/', charterViews.addCharter),
    path('ports/', portViews.getPortsNames),
    path('port/details/', portViews.getPort),
    path('boatPhotos/', photoViews.getBoatPhotos),
    path('photos/<str:img_name>/', photoViews.getPhoto),
    ]
