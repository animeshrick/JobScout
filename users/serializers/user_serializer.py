from typing import Optional
from rest_framework import serializers

from users.export_types.validation_types.validation_result import ValidationResult
from users.models.user_models.user import User
from users.services.encryption_services.encryption_service import EncryptionServices
from users.services.helpers import (
    validate_email,
    validate_name,
    validate_password,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate(self, data: Optional[dict] = None) -> Optional[bool]:
        email = data.get("email")
        fname = data.get("fname")
        lname = data.get("lname")
        password = data.get("password")
        role = data.get("role")

        # Email Validation
        if email and email != "" and isinstance(email, str):
            validation_result_email: ValidationResult = validate_email(email)
            is_validated_email = validation_result_email.is_validated
            if not is_validated_email:
                raise serializers.ValidationError(detail=validation_result_email.error)
        else:
            raise serializers.ValidationError(detail="Email should not be empty.")

        # Name and Username Validation
        if (
            fname
            and lname
            and fname != ""
            and lname != ""
            and isinstance(fname, str)
            and isinstance(lname, str)
        ):
            validation_result_name: ValidationResult = validate_name(fname + lname)
            is_validated_name = validation_result_name.is_validated
            if not is_validated_name:
                raise serializers.ValidationError(detail=validation_result_name.error)
        else:
            raise serializers.ValidationError(
                detail="First Name and Last Name should not be empty."
            )

        # Password Validation
        if password and password != "" and isinstance(password, str):
            validation_result_password: ValidationResult = validate_password(password)
            is_validated_password = validation_result_password.is_validated
            if not is_validated_password:
                raise serializers.ValidationError(validation_result_password.error)
        else:
            raise serializers.ValidationError(detail="Password should not be empty.")

        # user role validations
        if role and role.lower() not in ["seeker", "recruiter"]:
            raise serializers.ValidationError(
                detail="Invalid role. Allowed roles: seeker, recruiter."
            )

        if is_validated_email and is_validated_password and is_validated_name:
            return True

    def create(self, data: dict) -> User:
        role = data.get("role")
        role = role if role else "seeker"

        if self.validate(data):
            user = User(
                email=data.get("email"),
                fname=data.get("fname"),
                lname=data.get("lname"),
                password=EncryptionServices().encrypt(data.get("password")),
                role=role,
            )
            user.save()
            return user
