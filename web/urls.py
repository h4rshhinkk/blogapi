from django.urls import path


from . import views

app_name = "web"

urlpatterns = [
   path('',views.index,name="index"),
   path('get-all-posts/',views.GetAllPosts,name="get-all-posts"),
   path('create-new-post/',views.CreatePost,name="create-new-post"),
   path('delete-post/',views.DeletePost,name="delete-post"),
   path('get-post/',views.GetPost),
   path('update-post/',views.UpdatePost)
]