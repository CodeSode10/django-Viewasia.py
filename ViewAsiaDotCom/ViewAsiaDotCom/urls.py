from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin-asia/', admin.site.urls),

    path('', viewHome, name="viewHome"),

    path('about/', viewAbout, name="viewAbout"),

    path('contact/', viewContact, name="viewContact"),
    
    path('login/', viewLogin, name="viewLogin"),
    
    path('signup/', viewSignup, name="viewSignup"),
    
    path('subscription/', viewSubscription, name="viewSubscription"),

    path('upload/', viewUpload, name="viewUpload"),

    path('category/', searchImg, name="searchImg"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
