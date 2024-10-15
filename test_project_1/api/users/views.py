from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(http_method_names=['GET'])
def get_data(request):
    data = {
        "name": "Syed Talha Askari",
    }
    return Response(data)