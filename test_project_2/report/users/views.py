from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(http_method_names=['GET'])
def get_data(request):
    data = [
        {
            "name": "Syed Talha Askari",
        }
    ]
    return Response(data)