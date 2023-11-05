from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.fw.utils.siu_utils import *
from apps.fw.utils.egresado_utils import *


class EgresadosSIU(APIView):
    def post(self, request):
        try:
            egresados = get_egresados_from_SIU()
        except Exception as e:
            return Response({"error": f"An unexpected error occurred: {str(e)}"})

        contador_nuevos_egresados = 0

        for egresado in egresados:
            if check_data_egresado(json_egresado=egresado):
                nuevo_egresado = crear_nuevo_egresado(json_egresado=egresado)

                if nuevo_egresado:
                    contador_nuevos_egresados += 1

        register_update(
            cantidad=contador_nuevos_egresados,
            origen=request.data.get("origen"),
        )

        return Response(
            {"message": f"Se agregaron {contador_nuevos_egresados}"}, status=200
        )
