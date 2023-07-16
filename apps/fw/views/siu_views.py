from django.shortcuts import render

import requests
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.fw.models.user_model import FwUser
from apps.fw.models.carrera_model import Carrera
from apps.fw.models.egreso_model import Egreso
from apps.fw.models.ciudad_model import Ciudad
from apps.fw.models.privacidad_model import Privacidad

from apps.fw.serializers.ciudad_serializers import CiudadUpdateSerializer


class EgresadosSIU(APIView):
    def title_case(self, objeto, atributo):
        return (
            objeto.get(atributo).title()
            if objeto.get(atributo) != None
            else objeto.get(atributo)
        )

    def get_egresados(self):
        response = requests.get("https://guarani.unt.edu.ar/rest/ws_facet.php").json()
        egresados = response.get("data")
        result = [egresado["post"] for egresado in egresados]
        return result

    def get_or_create_ciudad(self, data):
        if not data:
            ciudad = None
        elif type(data) is str:
            data_cased = data.title()
            data_ciudad = {
                "ciudad": data_cased,
            }
            serializer = CiudadUpdateSerializer(data=data_ciudad)
            serializer.is_valid(raise_exception=True)
            ciudad = serializer.save()
        else:
            ciudad = Ciudad.objects.get(id=data)

        return ciudad

    def crear_egresado(self, dni, carrera, egresado):
        apellidos_nuevo_egresado = self.title_case(egresado, "apellido")
        nombres_nuevo_egresado = self.title_case(egresado, "nombres")
        email_nuevo_egresado = self.title_case(egresado, "email")
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

        nuevo_egresado = FwUser.objects.create(
            dni=dni,
            apellidos=apellidos_nuevo_egresado,
            nombres=nombres_nuevo_egresado,
            email=email_nuevo_egresado,
            fecha_nac=fecha_nac_nuevo_egresado,
            nacionalidad=nacionalidad_nuevo_egresado,
            ciudad_natal=ciudad_natal_nuevo_egresado,
            ciudad_actual=ciudad_actual_nuevo_egresado,
            # domicilio=domicilio_nuevo_egresado,
            # certificado=certificado_nuevo_egresado,
            sexo=sexo_nuevo_egresado,
        )

        ciclo_egreso_nuevo_egresado = egresado.get("fecha_egreso")

        Egreso.objects.create(
            carrera=carrera,
            usuario=nuevo_egresado,
            ciclo_egreso=ciclo_egreso_nuevo_egresado,
        )

        Privacidad.objects.create(
            usuario=nuevo_egresado,
        )

    def post(self, request):
        egresados = self.get_egresados()
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
                    self.crear_egresado(
                        dni=dni_nuevo_egresado,
                        carrera=carrera,
                        egresado=egresado,
                    )
                    contador_nuevos_egresados += 1

        return Response(
            {"message": f"Se agregaron {contador_nuevos_egresados}"}, status=200
        )
