from upload.models.image_upload_model import ImageUploadModel
from upload.serializers.file_upload_serializer import FileUploadSerializer
from upload.upload_exceptions.upload_exceptions import FileNotUploaded


class UploadServices:

    @staticmethod
    def upload_docs(request_data: dict, uid: str) -> dict:
        data = {
            "request_data": request_data,
            "uid": uid,
        }
        uploaded_file: ImageUploadModel = FileUploadSerializer().upload_file(data=data)
        if uploaded_file:
            return {
                "message": "File uploaded successfully.",
                "image_url": uploaded_file.image,
            }
        else:
            pass
            raise FileNotUploaded()
