from django.urls import path

from upload.views.upload_file import UploadFileView

urlpatterns = [path("upload-file", UploadFileView.as_view(), name="Upload-File")]
