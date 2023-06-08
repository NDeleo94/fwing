import os
from django.conf import settings

from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.response import Response


class ImageView(APIView):
    def get(self, request, image_path):
        dot_index = image_path.rindex(".") + 1
        ext = image_path[dot_index:]
        try:
            image_file = open(
                os.path.join(settings.MEDIA_ROOT, f"images/{image_path}"), "rb"
            )
            response = FileResponse(image_file)
            response["Content-Type"] = f"image/{ext}"
            response["Content-Disposition"] = "inline"
            return response
        except IOError:
            return Response({"error": "Image not found"}, status=404)
