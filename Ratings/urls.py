from django.urls import path
from .views import upload_rating
urlpatterns = [
    path("rating/upload",upload_rating, name="rating_upload_view"),
   
]