from django.urls import path     
from . import views


urlpatterns = [
    path('', views.index),
    path("createNewBook", views.addingBooks),
    path("bookinfo/<int:idBook>", views.showbookinfo),
    path("addToAuthorlist/<int:idBook>", views.anotherone)
]