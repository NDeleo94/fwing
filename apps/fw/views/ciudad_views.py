from rest_framework.views import APIView

from rest_framework.response import Response

from apps.fw.utils.ciudad_utils import add_coordinates, fetch_ciudades


class CiudadView(APIView):
    def post(self, request):
        func = request.data.get("funcion")

        contador_ok = 0
        contador_fail = 0
        ciudades = fetch_ciudades()
        for ciudad in ciudades:
            if not ciudad.lat or not ciudad.long:
                try:
                    add_coordinates(ciudad=ciudad)
                    contador_ok += 1
                except Exception as e:
                    contador_fail += 1

        message = "Task done successfully"
        return Response(
            {
                "message": f"{message}",
                "ok": f"{contador_ok} cities added",
                "error": f"{contador_fail} could not be added",
            }
        )
