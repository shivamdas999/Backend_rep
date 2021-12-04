from rest_framework.decorators import api_view
from rest_framework.response import Response

from bookapi.iceandfireapi import IceAndFireAPI


@api_view()
def get_books_from_api(request):

    # this retrieves book from ice and fire api

    ice_and_fire_api = IceAndFireAPI()
    books_from_api = ice_and_fire_api.get_books(request.GET)
    return Response({"status_code": 200,
                     "status": "success",
                     "data": books_from_api})