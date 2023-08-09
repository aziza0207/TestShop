from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer

User = get_user_model()


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = get_user_model().objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."})
        return Response(serializer.errors, status=400)

