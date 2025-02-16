from rest_framework import serializers


class FileUploadRequestType(serializers.Serializer):
    file = serializers.FileField()
    action = serializers.CharField()
