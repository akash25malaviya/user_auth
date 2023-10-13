from .serializers import *
from rest_framework import status, generics, response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate


# Create your views here.
class RegisterAPI(generics.GenericAPIView):
    """
    User Register
    """

    def post(self, request):
        serializer = RegisterSerializer(
            data=self.request.data, context={"request": request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(
                {
                    "status": True,
                    "message": "Registered successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )


class LoginAPI(generics.GenericAPIView):
    """
    User Register
    """

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            response_data = {
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "tokens": user.tokens,
            }
            return response.Response(
                {
                    "status": True,
                    "message": "Login successfully",
                    "data": response_data,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return response.Response(
                {
                    "status": True,
                    "message": "Somthig wont's wrong",
                    "data": {},
                },
                status=status.HTTP_201_CREATED,
            )

class GetUserDataAPI(generics.GenericAPIView):
    """
    User Register
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        if user:
            response_data = {
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
            }
            return response.Response(
                {
                    "status": True,
                    "message": "successfully",
                    "data": response_data,
                },
                status=status.HTTP_201_CREATED,
            )
