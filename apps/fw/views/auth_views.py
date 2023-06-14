from django.shortcuts import render

from django.utils import timezone
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from apps.fw.models.user_model import FwUser
from apps.fw.serializers.egresado_serializers import EgresadoLoginSerializer
from google.auth import jwt


class LoginGoogleView(APIView):
    def get_google_email(self, token):
        try:
            decoded_token = jwt.decode(token, verify=False)
            google_email = decoded_token.get("email")
            return google_email
        except jwt.exceptions.DecodeError as e:
            print(f"Error decoding Google token: {e}")
            return None

    def post(self, request):
        token = request.data
        google_email = self.get_google_email(token)
        if google_email:
            user = FwUser.objects.filter(email=google_email).first()

            if user:
                user.last_login = timezone.now()
                user.save()
                # Generate or retrieve the token for the user
                token, _ = Token.objects.get_or_create(user=user)
                user_serializer = EgresadoLoginSerializer(user)
                return Response(
                    {
                        "token": token.key,
                        "user": user_serializer.data,
                    }
                )
            else:
                return Response({"error": "Invalid credentials"}, status=400)
        else:
            return Response({"error": "Missing email"}, status=400)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if username and password:
            if "@" in username:
                user_finded = FwUser.objects.filter(email=username).first()
                if user_finded:
                    username = user_finded.dni
                else:
                    return Response({"error": "Invalid credentials"}, status=400)

            user = authenticate(username=username, password=password)

            if user:
                user.last_login = timezone.now()
                user.save()
                # Generate or retrieve the token for the user
                token, _ = Token.objects.get_or_create(user=user)
                user_serializer = EgresadoLoginSerializer(user)

                return Response(
                    {
                        "token": token.key,
                        "user": user_serializer.data,
                    }
                )
            else:
                return Response({"error": "Invalid credentials"}, status=400)
        else:
            return Response({"error": "Missing username or password"}, status=400)


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Delete the token associated with the user
        Token.objects.filter(user=request.user).delete()
        return Response({"success": "Logout successful"})
