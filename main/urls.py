from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.product_list, name="show_main"),

    # auth
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),

    # products (toko)
    path("products/new/", views.product_create, name="add_product"),
    path("products/<int:pk>/", views.product_detail, name="product_detail"),
    path("products/<int:pk>/edit/", views.product_edit, name="product_edit"),
    path("products/<int:pk>/delete/", views.product_delete, name="product_delete"),

    # data delivery untuk Item (tetap ada sesuai tutorial sebelumnya)
    path("json/", views.show_json, name="show_json"),
    path("xml/", views.show_xml, name="show_xml"),
    path("json/<int:id>/", views.show_json_by_id, name="show_json_by_id"),
    path("xml/<int:id>/", views.show_xml_by_id, name="show_xml_by_id"),
]
