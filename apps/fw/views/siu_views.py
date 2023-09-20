from django.shortcuts import render

import requests, base64
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.fw.models.user_model import FwUser
from apps.fw.models.carrera_model import Carrera
from apps.fw.models.egreso_model import Egreso
from apps.fw.models.ciudad_model import Ciudad
from apps.fw.models.privacidad_model import Privacidad

from apps.fw.serializers.ciudad_serializers import CiudadUpdateSerializer
from apps.fw.serializers.egresado_serializers import EgresadoUpdateSerializer
from apps.fw.serializers.egreso_serializers import EgresoUpdateSerializer
from apps.fw.serializers.privacidad_serializers import PrivacidadSerializer

from decouple import config


class EgresadosSIU(APIView):
    def title_case(self, objeto, atributo):
        return (
            objeto.get(atributo).title()
            if objeto.get(atributo) != None
            else objeto.get(atributo)
        )

    def get_credentials(self):
        user = config("SIU_FACET_USER")
        password = config("SIU_FACET_PASSWORD")

        credentials = f"{user}:{password}"

        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        return encoded_credentials

    def get_egresados(self):
        encoded_credentials = self.get_credentials()

        response = requests.get(
            url=config("SIU_FACET_URL"),
            headers={"Authorization": f"Basic {encoded_credentials}"},
        ).json()

        egresados = response.get("data")
        result = [egresado["post"] for egresado in egresados]
        return result

    def get_or_create_ciudad(self, data):
        if not data:
            ciudad = None
        else:
            ciudad = Ciudad.objects.filter(ciudad__icontains=data).first()

            if ciudad:
                return ciudad
            else:
                data_cased = data.title()
                data_ciudad = {
                    "ciudad": data_cased,
                }
                serializer = CiudadUpdateSerializer(data=data_ciudad)
                serializer.is_valid(raise_exception=True)
                ciudad = serializer.save()
                return ciudad

    def create_egresado(self, dni, egresado):
        apellidos_nuevo_egresado = self.title_case(egresado, "apellido")
        nombres_nuevo_egresado = self.title_case(egresado, "nombres")
        email_nuevo_egresado = egresado.get("email")
        fecha_nac_nuevo_egresado = self.title_case(egresado, "fecha_nacimiento")
        nacionalidad_nuevo_egresado = self.title_case(egresado, "nacionalidad")
        # domicilio_nuevo_egresado = self.title_case(egresado, "domicilio")
        # certificado_nuevo_egresado = self.title_case(egresado, "certificado")
        sexo_nuevo_egresado = self.title_case(egresado, "sexo")

        ciudad_natal_nuevo_egresado = self.get_or_create_ciudad(
            self.title_case(egresado, "localidadnac")
        )
        ciudad_actual_nuevo_egresado = self.get_or_create_ciudad(
            self.title_case(egresado, "localidad")
        )

        data_egresado = {
            "dni": dni,
            "apellidos": apellidos_nuevo_egresado,
            "nombres": nombres_nuevo_egresado,
            "email": email_nuevo_egresado,
            "fecha_nac": fecha_nac_nuevo_egresado,
            "nacionalidad": nacionalidad_nuevo_egresado,
            "ciudad_natal": ciudad_natal_nuevo_egresado.id,
            "ciudad_actual": ciudad_actual_nuevo_egresado.id,
            # "domicilio":domicilio_nuevo_egresado,
            # "certificado":certificado_nuevo_egresado,
            "sexo": sexo_nuevo_egresado,
        }
        serializer = EgresadoUpdateSerializer(data=data_egresado)
        serializer.is_valid(raise_exception=True)
        nuevo_egresado = serializer.save()

        return nuevo_egresado

    def create_egreso(self, carrera, usuario, egresado):
        ciclo_egreso = egresado.get("fecha_egreso")
        data_egreso = {
            "carrera": carrera.id,
            "usuario": usuario.id,
            "ciclo_egreso": ciclo_egreso,
        }
        serializer = EgresoUpdateSerializer(data=data_egreso)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def create_privacidad(self, usuario):
        data_privacidad = {
            "usuario": usuario.id,
        }
        serializer = PrivacidadSerializer(data=data_privacidad)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def set_origin(self, usuario):
        usuario.origen = 2
        usuario.save()

    def crear_nuevo_egresado(self, dni, carrera, egresado):
        nuevo_egresado = self.create_egresado(dni=dni, egresado=egresado)

        self.create_egreso(carrera=carrera, usuario=nuevo_egresado, egresado=egresado)

        self.create_privacidad(usuario=nuevo_egresado)

        self.set_origin(usuario=nuevo_egresado)

    def post(self, request):
        try:
            egresados = self.get_egresados()
        except Exception as e:
            return {"error": f"An unexpected error occurred: {str(e)}"}

        contador_nuevos_egresados = 0

        for egresado in egresados:
            carrera_nuevo_egresado = egresado.get("carrera")

            carrera = Carrera.objects.filter(
                carrera__icontains=carrera_nuevo_egresado, following=True
            ).first()

            if carrera:
                dni_nuevo_egresado = int(egresado.get("nro_documento"))
                usuario = FwUser.objects.filter(dni=dni_nuevo_egresado).exists()

                if not usuario:
                    self.crear_nuevo_egresado(
                        dni=dni_nuevo_egresado,
                        carrera=carrera,
                        egresado=egresado,
                    )
                    contador_nuevos_egresados += 1

        return Response(
            {"message": f"Se agregaron {contador_nuevos_egresados}"}, status=200
        )
