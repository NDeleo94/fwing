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

    def crearEgresado(self, dni, carrera, egresado):
        apellidos_nuevo_egresado = egresado.get("apellido").title()
        nombres_nuevo_egresado = egresado.get("nombres").title()
        email_nuevo_egresado = egresado.get("email")
        fecha_nac_nuevo_egresado = egresado.get("fecha_nacimiento")
        nacionalidad_nuevo_egresado = egresado.get("nacionalidad").title()
        ciudad_natal_nuevo_egresado = egresado.get("localidadnac").title()
        ciudad_actual_nuevo_egresado = egresado.get("localidad").title()
        domicilio_nuevo_egresado = egresado.get("domicilio").title()
        certificado_nuevo_egresado = egresado.get("certificado").title()
        sexo_nuevo_egresado = egresado.get("sexo")

        nuevo_egresado = FwUser.objects.create(
            dni=dni,
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
                    self.crearEgresado(
                        dni=dni_nuevo_egresado,
                        carrera=carrera,
                        egresado=egresado,
                    )
                    contador_nuevos_egresados += 1

        return Response(
            {"message": f"Se agregaron {contador_nuevos_egresados}"}, status=200
        )
