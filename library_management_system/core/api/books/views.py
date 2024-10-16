from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework import status

from core.models import Book, Author, Genre

class BookFieldError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

@api_view(http_method_names=['GET', 'POST'])
def get_or_create_book(request: Request):
    try:
        if request.method == 'GET':
            books = Book.objects.all()
            query_params = request.query_params

            author_id = query_params.get('author_id')
            genre_id = query_params.get('genre_id')
            title = query_params.get('title')
            published_date = query_params.get('published_date')
            if author_id is not None:
                books = books.filter(author__id=int(author_id))
            if genre_id is not None:
                books = books.filter(genre__id=int(genre_id))
            if title is not None:
                books = books.filter(title=title)
            if published_date is not None:
                books = books.filter(published_date=published_date)

            view_form_data = []

            for book in books:
                author_data = []
                for author in book.author.all():
                    author_data.append({
                        "id": author.id,
                        "name": author.name,
                        "bio": author.bio,
                    })

                genre_data = []
                for genre in book.genre.all():
                    genre_data.append({
                        "id": genre.id,
                        "name": genre.name,
                    })

                view_form_data.append({
                    "id": book.id,
                    "title": book.title,
                    "authors": author_data,
                    "genres": genre_data,
                    "published_date": book.published_date,
                })
            return Response(data=view_form_data, status=status.HTTP_200_OK)
        if request.method == 'POST':
            data = request.data

            title = data.get('title')
            authors = data.get('authors')
            genres = data.get('genres')
            published_date = data.get('published_date')

            if title is not None and authors is not None and genres is not None:
                book = Book()

                book.title = title
                book.published_date = published_date
                book.save()

                author_obj = Author.objects.filter(id__in=authors)
                book.author.add(*author_obj)
                genre_obj = Genre.objects.filter(id__in=genres)
                book.genre.add(*genre_obj)

                return Response(data={"Success": "Book Added Successfully"}, status=status.HTTP_201_CREATED)
            raise BookFieldError("title, author and genre are required fields")
    except Author.DoesNotExist as e:
        return Response(data=str(e), status=status.HTTP_404_NOT_FOUND)
    except Genre.DoesNotExist as e:
        return Response(data=str(e), status=status.HTTP_404_NOT_FOUND)
    except Book.DoesNotExist as e:
        return Response(data=str(e), status=status.HTTP_404_NOT_FOUND)
    except BookFieldError as err:
        return Response(data={"error": err.message },status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(data={"error": str(e) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def get_or_update_or_delete_book(request: Request, id):
    try:
        if request.method == 'GET':
            book = Book.objects.get(pk=id)

            author_data = []
            for author in book.author.all():
                author_data.append({
                    "id": author.id,
                    "name": author.name,
                    "bio": author.bio,
                })

            genre_data = []
            for genre in book.genre.all():
                genre_data.append({
                    "id": genre.id,
                    "name": genre.name,
                })
            book = {
                "id": book.id,
                "title": book.title,
                "authors": author_data,
                "genres": genre_data,
                "published_date": book.published_date,
            }
            return Response(data=book, status=status.HTTP_200_OK)
        if request.method == 'PUT':
            book = Book.objects.get(pk=id)

            data = request.data

            title = data.get('title')
            authors = data.get('authors')
            genres = data.get('genres')
            published_date = data.get('published_date')

            book.title = title if title is not None else book.title
            book.published_date = published_date if published_date is not None else book.published_date

            book.save()

            if authors is not None:
                book.author.clear()
                author_obj = Author.objects.filter(id__in=authors)
                book.author.add(*author_obj)

            if genres is not None:
                book.genre.clear()
                genre_obj = Genre.objects.filter(id__in=genres)
                book.genre.add(*genre_obj)

            return Response(data={ 'message': 'Book Updated Successfully' }, status=status.HTTP_200_OK)
        if request.method == 'DELETE':
            book = Book.objects.get(pk=id)

            book.delete()

            return Response(data={ 'message': 'Book Deleted Successfully' }, status=status.HTTP_200_OK)
    except Author.DoesNotExist:
        return Response(data={"error": "Author does not exist"}, status=status.HTTP_404_NOT_FOUND)
    except Book.DoesNotExist:
        return Response(data={"error": "Book does not exist"}, status=status.HTTP_404_NOT_FOUND)
    except BookFieldError as err:
        return Response(data={"error": err.message },status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(data={"error": str(e) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)