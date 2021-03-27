from django.http import HttpResponse
from django.urls import path  
from .views import plugin_crossconnectView 

def dummmy_view(request):
    html = "<html><body>Cross Connect plugin.</body></html>"
    return  HttpResponse(html)

urlpatterns = [
    path("", dummmy_view, name="crossconnect_list"),
    path("<int:pk>/", plugin_crossconnectView.as_view(), name="plugin_crossconnect"),
]
# urlpatterns = [
#     path("<int:pk>/",plugin_crossconnectView.as_view(),name="plugin_crossconnect"),
# ]