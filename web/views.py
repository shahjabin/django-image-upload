from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from web.forms import UploadForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Photo

def handleAjaxUpload(request):
    try:
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({
                "code": 201,
                "message": "Image uploaded successfully"
            })
        else:
            return JsonResponse({
                "status": 400,
                "message": form.errors["image"]
            })
    except Exception as e:
        return JsonResponse({
            "code": 500,
            "message": e
        })        


class UploadView(generic.View):
    def get(self, *args, **kwargs):
        form = UploadForm()
        imageSrc = "/media/default.png"
        photo = Photo.objects.last()
        if photo:
            imageSrc = photo.image.url
        return render(self.request, "web/index.html",  {
            "form": form,
            "imageSrc": imageSrc
        })

    def post(self, *args, **kwargs):
        if self.request.is_ajax():
            return handleAjaxUpload(self.request)

        form = UploadForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            form.save()
            messages.success(self.request, "Image Uploaded")
        else:
            messages.error(self.request, "Failed uploading image")
        
        return redirect(reverse_lazy("index"))
