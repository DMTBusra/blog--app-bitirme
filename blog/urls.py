from django.urls import path
from .views import  BlogList,Edit
urlpatterns =[
     path("",BlogList.as_view(),name="bloglist"),
   
     path("blog_detail/<int:pk>/",Edit.as_view(),name="blogdetail")
    ]