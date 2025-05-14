from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page),
    path('request/', views.request_view),
    path('request/app-attributes/', views.request_app_attributes),
    path('request/middleware/', views.request_middleware),
    path('request/querydict/', views.request_querydict),
    path('request/is-secure/', views.request_is_secure),
    path('home/', views.home),
    path('response/', views.basic_response),
    path('response/subclasses/', views.response_with_headers),
    path('response/json/', views.json_response),
    path('response/streaming/', views.streaming_response),
    path('response/file/', views.file_response),
    path('response/base/', views.response_base),
]