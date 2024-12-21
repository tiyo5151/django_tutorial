from django.urls import path
from .views import (
    IndexView,
    PageCreateView,
    PageListView,
    PageDetailView,
    PageUpdateView,
    PageDeleteView,
)

app_name = "diary"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("page/create/", PageCreateView.as_view(), name="page_create"),
    path("pages/", PageListView.as_view(), name="page_list"),
    path("page/<uuid:id>/", PageDetailView.as_view(), name="page_detail"),
    path("page/<uuid:id>/update/", PageUpdateView.as_view(), name="page_update"),
    path("page/<uuid:id>/delete/", PageDeleteView.as_view(), name="page_delete"),
]
