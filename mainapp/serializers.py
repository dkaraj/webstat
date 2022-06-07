import json

from rest_framework import serializers
from django.utils.translation import gettext as _

from mainapp.models import  Website


class WebsiteDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Website

        fields = ("id", "name", "code", "development_mode", "support_email", "no_reply_email",
                  "developer_email", "timezone")

class WebsiteSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=255, required=False,allow_blank=True)
    code = serializers.CharField(max_length=255, required=True)
    development_mode = serializers.BooleanField(required=False)
    support_email = serializers.EmailField(required=False, allow_blank=True)
    no_reply_email = serializers.EmailField(required=False, allow_blank=True)
    developer_email = serializers.EmailField(required=False, allow_blank=True)
    timezone = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = Website

        fields = ("id", "name", "code", "development_mode", "support_email", "no_reply_email",
                  "developer_email", "timezone")

    def create(self, validated_data):
        """
        Create and return a new `Website` instance, given the validated data.
        """
        return WebsiteSerializer.objects.create(**validated_data)
