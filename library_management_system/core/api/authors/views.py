from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework import status

from core.models import Author

class AuthorFieldError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

@api_view(http_method_names=['GET', 'POST'])
def get_or_create_author(request: Request):
    try:
        if request.method == 'GET':
            authors = Author.objects.all()

            view_form_data = []

            for author in authors:
                view_form_data.append({
                    "id": author.id,
                    "name": author.name,
                    "bio": author.bio,
                })
            return Response(view_form_data, status=status.HTTP_200_OK)
        if request.method == 'POST':
            data = request.data

            name = data.get('name')
            bio = data.get('bio')

            if name is not None:
                if isinstance(name, str):
                    if len(name.strip()) > 0:
                        author = Author()

                        author.name = name
                        author.bio = bio
                        author.save()

                        author = {
                            "id": author.id,
                            "name": author.name,
                            "bio": author.bio,
                        }
                        return Response(data=author, status=status.HTTP_201_CREATED)
                    raise AuthorFieldError("name field must have some value")
                raise AuthorFieldError("name field must be a string")
            raise AuthorFieldError("name field is required")
    except AuthorFieldError as err:
        return Response(data={"error": err.message },status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(data={"error": str(e) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def get_or_update_or_delete_author(request: Request, id):
    try:
        if request.method == 'GET':
            author = Author.objects.get(pk=id)

            author = {
                "id": author.id,
                "name": author.name,
                "bio": author.bio,
            }
            return Response(data=author, status=status.HTTP_200_OK)
        if request.method == 'PUT':
            data = request.data

            author = Author.objects.get(pk=id)

            name = data.get('name')
            bio = data.get('bio')

            if name is not None:
                if isinstance(name, str):
                    if len(name.strip()) > 0:
                        author.name = name
                        if bio is not None and isinstance(bio, str) and len(bio.strip()) > 0:
                            author.bio = bio
                        author.save()

                        author = {
                            "id": author.id,
                            "name": author.name,
                            "bio": author.bio,
                        }
                        return Response(data=author, status=status.HTTP_200_OK)
                    raise AuthorFieldError("name field must have some value")
                raise AuthorFieldError("name field must be a string")
            raise AuthorFieldError("name field is required")
        if request.method == 'DELETE':
            author = Author.objects.get(pk=id)
            author.delete()

            return Response(data={ 'message', 'Author Deleted Successfully' }, status=status.HTTP_200_OK)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except AuthorFieldError as err:
        return Response(data={"error": err.message },status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(data={"error": str(e) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)