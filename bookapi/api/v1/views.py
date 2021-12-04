from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view

from django.http import HttpResponse

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from bookapi.models import Book
import json

@api_view()
def upload(request):
    if request.method == 'POST':
        json_data = json.loads(request.data)
        if json_data.is_valid():
            json_data.save()
        return Response({"status_code": 200,
                         "status": "success",
                         "data": json_data})
    if request.method == 'GET':
        shelf = Book.objects.all()
        return Response({"status_code": 200,
                         "status": "success",
                         "data": shelf})


def update(request,book_id):
    book_id = int(book_id)
    try :
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return HttpResponse({"status_code": 200,
                         "status": "success",
                         "message": "Book does not exist",
                         })

    return HttpResponse({"status_code": 200,
                    "status": "success",
                    "message": "?name={} is updated successfully".format(book_sel['name']),
                    "data": book_sel})


def delete(request,book_id):
    book_id = int(book_id)
    try :
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return HttpResponse({"status_code": 200,
                         "status": "success",
                         "message": "Book does not exist"})
    book_sel.delete()
    return HttpResponse({"status_code": 200,
                    "status": "success",
                    "message": "?name={} is deleted successfully".format(book_sel),
                    "data": book_sel})


