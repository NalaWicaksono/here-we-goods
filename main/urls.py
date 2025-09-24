from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.show_main, name="show_main"),
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("add/", views.add_item, name="add_item"),  
    path("json/", views.show_json, name="show_json"),
    path("xml/", views.show_xml, name="show_xml"),
    path("json/<int:id>/", views.show_json_by_id, name="show_json_by_id"),
    path("xml/<int:id>/", views.show_xml_by_id, name="show_xml_by_id"),
    path("item/<int:pk>/", views.item_detail, name="item_detail"),
]
