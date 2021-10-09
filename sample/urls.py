from django.urls import path

from sample.views import index

urlpatterns = [
    path("", index, name="index")
]
