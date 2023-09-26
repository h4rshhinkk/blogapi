from django.urls import path
from . import views

app_name = "drinks"


urlpatterns = [
    path('drink_list/',views.drink_list,name="drink_list"),

    path('drink_detail/<int:id>',views.drink_detail,name="drink_detail"),
    
]