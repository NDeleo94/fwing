from rest_framework.views import APIView

from rest_framework.response import Response


class TestView(APIView):
    def get(self, request):
        return Response({"message": "Test Get"}, status=200)

    def post(self, request):
        return Response({"message": "Test Post"}, status=200)
