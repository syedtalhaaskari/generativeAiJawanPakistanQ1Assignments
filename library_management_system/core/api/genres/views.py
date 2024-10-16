from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework import status
from django.core.exceptions import ValidationError, FieldError, BadRequest

from core.models import Genre

class GenreFieldError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

@api_view(http_method_names=['GET', 'POST'])
def get_or_create_genre(request: Request):
    try:
        if request.method == 'GET':
            genres = Genre.objects.all()

            view_form_data = []

            for genre in genres:
                view_form_data.append({
                    "id": genre.id,
                    "name": genre.name,
                })
            return Response(view_form_data, status=status.HTTP_200_OK)
        if request.method == 'POST':
            data = request.data

            name = data.get('name')

            if name is not None:
                if isinstance(name, str):
                    if len(name.strip()) > 0:
                        genre = Genre()

                        genre.name = name
                        genre.save()

                        genre = {
                            "id": genre.id,
                            "name": genre.name,
                        }
                        return Response(data=genre, status=status.HTTP_201_CREATED)
                    raise GenreFieldError("name field must have some value")
                raise GenreFieldError("name field must be a string")
            raise GenreFieldError("name field is required")
    except GenreFieldError as err:
        return Response(data={"error": err.message },status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(data={"error": str(e) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def get_or_update_or_delete_genre(request: Request, id):
    try:
        if request.method == 'GET':
            genre = Genre.objects.get(pk=id)

            genre = {
                "id": genre.id,
                "name": genre.name,
            }
            return Response(data=genre, status=status.HTTP_200_OK)
        if request.method == 'PUT':
            data = request.data

            genre = Genre.objects.get(pk=id)

            name = data.get('name')

            if name is not None:
                if isinstance(name, str):
                    if len(name.strip()) > 0:
                        genre.name = name
                        genre.save()

                        genre = {
                            "id": genre.id,
                            "name": genre.name,
                        }
                        return Response(data=genre, status=status.HTTP_200_OK)
                    raise GenreFieldError("name field must have some value")
                raise GenreFieldError("name field must be a string")
            raise GenreFieldError("name field is required")
        if request.method == 'DELETE':
            genre = Genre.objects.get(pk=id)
            genre.delete()

            return Response(data={ 'message', 'Genre Deleted Successfully' }, status=status.HTTP_200_OK)
    except Genre.DoesNotExist:
        return Response(data={ "error": "Genre does not exist" }, status=status.HTTP_404_NOT_FOUND)
    except GenreFieldError as err:
        return Response(data={"error": err.message },status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(data={"error": str(e) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)