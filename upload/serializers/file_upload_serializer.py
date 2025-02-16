from typing import Optional
from rest_framework import serializers

from upload.models.image_upload_model import ImageUploadModel
from upload.upload_exceptions.upload_exceptions import WrongFileFormat
from users.services.helpers import validate_user_uid
import cloudinary.uploader
import cloudinary
import os


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUploadModel
        fields = "__all__"

    def validate(self, data: Optional[dict] = None) -> Optional[bool]:
        # validating for is valid user
        uid = data.get("uid")
        if not validate_user_uid(uid).is_validated:
            pass
            # raise JobApplicationNotCreatedError()

        request_data = data.get("request_data")

        file = request_data.get("file")
        action = request_data.get("action")

        if not file or not action:
            raise ValueError("All fields are required.")

        if action not in ["upload_profile_img", "upload_cv"]:
            raise ValueError("Invalid upload action")

        return True

    def upload_file(self, data: dict) -> ImageUploadModel | None:
        if self.validate(data):
            user_id = data.get("uid")
            request_data = data.get("request_data")
            cloudinary.config(
                cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
                api_key=os.getenv("CLOUDINARY_API_KEY"),
                api_secret=os.getenv("CLOUDINARY_API_SECRET"),
            )

            file = request_data.get("file")
            action = request_data.get("action")

            try:
                upload_result = cloudinary.uploader.upload(
                    file.file,
                    public_id=f"{action}/{user_id}_{action}",
                    overwrite=True,
                    resource_type="image" if action == "upload_profile_img" else "raw",
                )
            except Exception as e:
                raise WrongFileFormat()

            print(f'secure_url: {upload_result.get("secure_url")}')

            # optimize_url, _ = cloudinary_url(
            #     user_id,
            #     fetch_format="auto",
            #     quality="auto",
            # )
            # optimize_url, _ = cloudinary_url(user_id, fetch_format="auto", quality="auto",
            # resource_type=resource_type)
            # print(f"optimize_url: {optimize_url}")

            # auto_crop_url, _ = cloudinary_url(user_id, width=500, height=500, crop="auto", gravity="auto",
            # resource_type=resource_type) print(f"auto_crop_url: {auto_crop_url}")

            if upload_result:
                file_type = ImageUploadModel(
                    image=upload_result.get("secure_url"),
                    public_id=user_id,
                    action=action,
                    uploaded_at=upload_result.get("created_at"),
                )
                return file_type
            else:
                return None
