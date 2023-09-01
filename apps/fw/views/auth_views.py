from django.shortcuts import render

from django.utils import timezone
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, get_authorization_header
from apps.fw.models.user_model import FwUser
from apps.fw.models.imagen_model import Imagen

from apps.fw.serializers.egresado_serializers import EgresadoLoginSerializer
from apps.fw.serializers.imagen_serializers import ImagenSerializer
from apps.fw.serializers.auth_serializers import *

from apps.fw.views.email_views import *

from google.auth import jwt


class LoginGoogleView(APIView):
    def get_google_property(self, token, property):
        try:
            decoded_token = jwt.decode(token, verify=False)
            google_email = decoded_token.get(property)
            return google_email
        except jwt.exceptions.DecodeError as e:
            print(f"Error decoding Google token: {e}")
            return None

    def set_google_profile_picture(self, usuario, token):
        imagen = Imagen.objects.filter(usuario=usuario).first()
        if imagen:
            imagen.url = self.get_google_property(token, "picture")
            imagen.file = None
            imagen.save()
        else:
            data_imagen = {
                "usuario": usuario.id,
                "file": None,
                "url": self.get_google_property(token, "picture"),
            }
            serializer = ImagenSerializer(data=data_imagen)
            serializer.is_valid(raise_exception=True)
            serializer.save()

    def post(self, request):
        token = request.data
        google_email = self.get_google_property(token, "email")
        if google_email:
            user = FwUser.objects.filter(email=google_email).first()

            if user:
                # if not user.last_login:
                #     self.set_google_profile_picture(usuario=user, token=token)
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


class NewPassword(APIView):
    def post(self, request):
        # Check data
        serializer = NewPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get data
        token = get_authorization_header(request).split()
        token = token[1].decode()

        new_password = serializer.validated_data.get("new_password")

        # Get user from token
        try:
            user = Token.objects.get(key=token).user
        except Token.DoesNotExist:
            return Response(
                {"error": "Invalid authentication token"},
                status=401,
            )

        # Change password
        user.set_password(new_password)
        user.save()
        return Response({"success": "Password changed successfully"})


class ChangePassword(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Check data
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get data
        token = get_authorization_header(request).split()
        token = token[1].decode()

        old_password = serializer.validated_data.get("old_password")
        new_password = serializer.validated_data.get("new_password")

        # Get user from token
        try:
            user = Token.objects.get(key=token).user
        except Token.DoesNotExist:
            return Response(
                {"error": "Invalid authentication token"},
                status=401,
            )

        # Change password
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response({"success": "Password changed successfully"})
        return Response({"error": "Invalid old password"}, status=400)


class ResetPassword(APIView):
    def post(self, request):
        # Check data
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get data
        email = serializer.validated_data.get("email")

        # Get user
        user = FwUser.objects.filter(email=email).first()

        if user:
            # Create token to user
            token, _ = Token.objects.get_or_create(user=user)

            # Send email
            sended = send_forget_password_email(user=user, token=token)
            if sended:
                return Response({"success": "Email sent successfully"})
            return Response("Error al enviar email")
        return Response({"error": "Invalid email"}, status=400)


class ChangeEmail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Check data
        serializer = ChangeEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get data
        token = get_authorization_header(request).split()
        token = token[1].decode()

        old_email = serializer.validated_data.get("old_email")
        new_email = serializer.validated_data.get("new_email")

        # Get user from token
        try:
            user = Token.objects.get(key=token).user
        except Token.DoesNotExist:
            return Response(
                {"error": "Invalid authentication token"},
                status=401,
            )

        # Change password
        if user.email == old_email:
            user.email = new_email
            user.save()
            return Response({"success": "Email changed successfully"})
        return Response({"error": "Invalid old email"}, status=400)
