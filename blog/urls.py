from django.urls import path
from .views import  BlogList,blog_detail
urlpatterns =[
     path("",BlogList.as_view(),name="bloglist"),
   
     path("blog_detail/<int:pk>/",blog_detail,name="blogdetail")
    ]