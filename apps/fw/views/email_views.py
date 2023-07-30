from django.conf import settings
from django.shortcuts import render
from django.template.loader import get_template
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMultiAlternatives

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.fw.models.user_model import FwUser
from apps.fw.models.email_model import Email


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


class EmailTemplateView(APIView):
    def post(self, request):
        destinataries = request.data["usuarios"]
        email_template = Email.objects.filter(id=request.data["plantilla"]).first()

        # Replace the placeholder "@user" with the actual user's name in the email body.
        body_with_user = email_template.cuerpo.replace("@nombres", "{nombres}").replace(
            "@apellidos", "{apellidos}"
        )

        # Loop through the list of user IDs and send the email to each user.
        for user_id in destinataries:
            user = get_object_or_404(FwUser, id=user_id)
            subject = email_template.asunto
            from_email = "egresados.computacion@herrera.unt.edu.ar"  # Update with your sender email
            to_email = "n.deleo94@gmail.com"

            # Replace "{name}" with the user's name in the email body.
            personalized_body = body_with_user.format(
                nombres=user.nombres, apellidos=user.apellidos
            )

            text_content = "Hi {nombres}, Welcome to My System!".format(
                nombres=user.nombres, apellidos=user.apellidos
            )
            html_content = personalized_body

            msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        # template = get_template("correo_invitacion.html")
        # content = template.render()

        # email = EmailMultiAlternatives(
        #     "Correo de prueba",
        #     "FollowING",
        #     settings.EMAIL_HOST_USER,
        #     [destinatary],
        # )
        # email.attach_alternative(
        #     content=content,
        #     mimetype="text/html",
        # )

        # sended = email.send()
        # if sended:
        #     return Response("Email enviado")
        # return Response("Error al enviar email")

        return Response({"message": "Emails sent successfully!"})
