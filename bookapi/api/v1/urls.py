from django.conf.urls import include, url


from bookapi.api.v1.views import  update, upload, delete



urlpatterns = [

    url(r'',upload),
    url(r'<int:book_id/update', update),
    url(r'<int:book_id/delete', delete),

]