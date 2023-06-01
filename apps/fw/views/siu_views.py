from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json


class EgresadosSIU(APIView):
    def post(self, request):
        response = requests.get("https://guarani.unt.edu.ar/rest/ws_facet.php").json()
        egresados = response.get("data")
        result = [item["post"] for item in egresados]
        return Response(result, status=200)
