from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_items, name="show_items"),
    path("add/", views.add_item, name="add_item"),
    path("detail/<int:pk>/", views.item_detail, name="item_detail"),
    path("json/", views.show_json, name="show_json"),
    path("xml/", views.show_xml, name="show_xml"),
    path("json/<int:id>/", views.show_json_by_id, name="show_json_by_id"),
    path("xml/<int:id>/", views.show_xml_by_id, name="show_xml_by_id"),
]
