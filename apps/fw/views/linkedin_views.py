import requests
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.fw.models.user_model import FwUser

from decouple import config


class LinkedInView(APIView):
    def post(self, request):
        url_access_token = "https://www.linkedin.com/oauth/v2/accessToken"

        url_data = "https://api.linkedin.com/v2/me?projection=(id,firstName,lastName,positions)"

        user_id = request.data.get("id")
        code = request.data.get("code")
        client_id = config("LI_CLIENT_ID")
        secret_id = config("LI_SECRET_ID")
        redirect_uri = config("LI_REDIRECT_URI")

        headers = {"Content-Type": "x-www-form-urlencoded"}

        params = {
            "grant_type": "authorization_code",
            "code": code,
            "client_id": client_id,
            "client_secret": secret_id,
            "redirect_uri": redirect_uri,
        }

        access_token = (
            requests.post(url=url_access_token, headers=headers, params=params)
            .json()
            .get("access_token")
        )

        headers = {"Authorization": f"Bearer {access_token}"}

        data = requests.get(url_data, headers=headers).json()
        print(data)
        linkedin_id = data.get("id")

        user = FwUser.objects.filter(id=user_id).first()

        if user and linkedin_id:
            user.linkedin_id = linkedin_id
            user.save()
            return Response({"message": "Ok"})

        return Response({"message": "Fail"}, status=400)
