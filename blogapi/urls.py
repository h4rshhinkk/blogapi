from django.contrib import admin
from django.urls import path,include
from drinks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("web.urls", namespace="web")),
    path("drinks/",include("drinks.urls", namespace="drinks")),

]
