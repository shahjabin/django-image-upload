from django.urls import path

from web.views import UploadView

urlpatterns = [
    path('', UploadView.as_view(), name="index"),
    path('upload', UploadView.as_view(), name="upload"),  
]

