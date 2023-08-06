from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template, render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.fw.models.user_model import FwUser
from apps.fw.models.email_model import Email

from decouple import config


def send_invitation_email(user, token):
    frontend_url = config("FRONTEND_URL")

    # Replace the placeholders in the email template with actual values
    email_subject = "Bienvenido a FollowING"
    email_template = "correo_invitacion.html"
    context = {
        "nombres": user.nombres,
        "frontend_url": f"{frontend_url}/login",
        "reset_url": f"{frontend_url}/reset-password/{token}",
    }
    email_body_html = render_to_string(email_template, context)
    email_body_text = strip_tags(email_body_html)

    # Send the email with both HTML and plain text versions
    msg = EmailMultiAlternatives(
        subject=email_subject,
        body=email_body_text,
        from_email=config("EMAIL_HOST_USER"),
        to=[user.email],
    )
    msg.attach_alternative(
        content=email_body_html,
        mimetype="text/html",
    )
    sended = msg.send()

    return sended


def send_forget_password_email(user, token):
    frontend_url = config("FRONTEND_URL")

    # Replace the placeholders in the email template with actual values
    email_subject = "Nueva contraseña FollowING"
    email_template = "correo_forget_password.html"
    context = {
        "nombres": user.nombres,
        "reset_url": f"{frontend_url}/reset-password/{token}",
    }
    email_body_html = render_to_string(email_template, context)
    email_body_text = strip_tags(email_body_html)

    # Send the email with both HTML and plain text versions
    msg = EmailMultiAlternatives(
        subject=email_subject,
        body=email_body_text,
        from_email=config("EMAIL_HOST_USER"),
        to=[user.email],
    )
    msg.attach_alternative(
        content=email_body_html,
        mimetype="text/html",
    )
    sended = msg.send()

    return sended


class EmailView(APIView):
    def post(self, request):
        destinatary = request.data["email"]
        template = get_template("correo_invitacion.html")
        content = template.render()

        email = EmailMultiAlternatives(
            "Bienvenido a FollowING",
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


class EmailTemplateView(APIView):
    def post(self, request):
        destinataries = request.data["usuarios"]

        email_template = Email.objects.filter(
            id=request.data["plantilla"],
        ).first()

        if not email_template:
            return Response({"message": "Template not found"})

        body_with_user = email_template.cuerpo.replace("@nombres", "{nombres}").replace(
            "@apellidos", "{apellidos}"
        )

        counter = 0
        for user_id in destinataries:
            user = get_object_or_404(FwUser, id=user_id)
            subject = email_template.asunto
            from_email = settings.EMAIL_HOST_USER
            to_email = "n.deleo94@gmail.com"  # user.email

            body = body_with_user.format(
                nombres=user.nombres,
                apellidos=user.apellidos,
            )

            text_content = "Hi {nombres}, Welcome to Following!".format(
                nombres=user.nombres,
                apellidos=user.apellidos,
            )

            html_content = body

            msg = EmailMultiAlternatives(
                subject,
                text_content,
                from_email,
                [to_email],
            )
            msg.attach_alternative(
                html_content,
                "text/html",
            )
            msg.send()
            counter += 1

        return Response({"message": f"{counter} Emails sent successfully!"})
