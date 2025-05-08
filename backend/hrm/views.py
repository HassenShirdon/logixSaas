from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hrm(request):
    return Response({"message": "Welcome to HRM Module"})