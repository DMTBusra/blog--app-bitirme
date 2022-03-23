from django.urls import path,include
from .views import RegisterAPI,log_out
urlpatterns =[
    path("auth/",include("dj_rest_auth.urls")),
    path("register/",RegisterAPI.as_view()),
    path("logout/",log_out),

    ]