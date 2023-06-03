from django.shortcuts import render

import requests
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.fw.models.user_model import FwUser
from apps.fw.models.carrera_model import Carrera
from apps.fw.models.egreso_model import Egreso


class EgresadosSIU(APIView):
    def getEgresados(self):
        response = requests.get("https://guarani.unt.edu.ar/rest/ws_facet.php").json()
        egresados = response.get("data")
        result = [egresado["post"] for egresado in egresados]
        return result

    def getAtributosEgresado(self, egresado):
        return (
            egresado.get("apellido").title(),
            egresado.get("nombres").title(),
            egresado.get("email"),
            egresado.get("fecha_nacimiento"),
            egresado.get("nacionalidad").title(),
            egresado.get("localidadnac").title(),
            egresado.get("localidad").title(),
            egresado.get("domicilio").title(),
            egresado.get("certificado").title(),
            egresado.get("sexo"),
        )

    def post(self, request):
        egresados = self.getEgresados()
        contador_nuevos_egresados = 0
        for egresado in egresados:
            carrera_nuevo_egresado = egresado.get("carrera")

            carrera = Carrera.objects.filter(
                carrera__iexact=carrera_nuevo_egresado
            ).first()

            if carrera:
                dni_nuevo_egresado = int(egresado.get("nro_documento"))
                usuario = FwUser.objects.filter(dni=dni_nuevo_egresado).exists()

                if not usuario:
                    (
                        apellidos_nuevo_egresado,
                        nombres_nuevo_egresado,
                        email_nuevo_egresado,
                        fecha_nac_nuevo_egresado,
                        nacionalidad_nuevo_egresado,
                        ciudad_natal_nuevo_egresado,
                        ciudad_actual_nuevo_egresado,
                        domicilio_nuevo_egresado,
                        certificado_nuevo_egresado,
                        sexo_nuevo_egresado,
                    ) = self.getAtributosEgresado(egresado)

                    nuevo_egresado = FwUser.objects.create(
                        dni=dni_nuevo_egresado,
                        apellidos=apellidos_nuevo_egresado,
                        nombres=nombres_nuevo_egresado,
                        email=email_nuevo_egresado,
                        fecha_nac=fecha_nac_nuevo_egresado,
                        nacionalidad=nacionalidad_nuevo_egresado,
                        ciudad_natal=ciudad_natal_nuevo_egresado,
                        ciudad_actual=ciudad_actual_nuevo_egresado,
                        domicilio=domicilio_nuevo_egresado,
                        certificado=certificado_nuevo_egresado,
                        sexo=sexo_nuevo_egresado,
                    )

                    ciclo_egreso_nuevo_egresado = egresado.get("fecha_egreso")

                    Egreso.objects.create(
                        carrera=carrera,
                        usuario=nuevo_egresado,
                        ciclo_egreso=ciclo_egreso_nuevo_egresado,
                    )

                    contador_nuevos_egresados += 1

        return Response(
            {"message": f"Se agregaron {contador_nuevos_egresados}"}, status=200
        )
