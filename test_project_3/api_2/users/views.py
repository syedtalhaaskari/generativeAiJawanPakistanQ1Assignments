from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(http_method_names=['GET'])
def get_data(request):
    data = [
        {
            "name": "Syed Talha Askari",
        },
        {
            "name": "API 2",
        }
    ]
    return Response(data)