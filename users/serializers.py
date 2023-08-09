from rest_framework import serializers, status
from django.contrib.auth import get_user_model
from rest_framework.response import Response

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ["username",
                  "email",
                  "password"]

        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


