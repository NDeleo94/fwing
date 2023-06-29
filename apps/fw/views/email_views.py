from django.conf import settings
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

from rest_framework.views import APIView
from rest_framework.response import Response


class EmailView(APIView):
    def post(self, request):
        destinatary = request.data["email"]
        template = get_template("correo_invitacion.html")
        content = template.render()

        email = EmailMultiAlternatives(
            "Correo de prueba",
            "FollowING",
            settings.EMAIL_HOST_USER,
            [destinatary],
        )
        email.attach_alternative(
            content=content,
            mimetype="text/html",
        )

        sended = email.send()
        if sended:
            return Response("Email enviado")
        return Response("Error al enviar email")
