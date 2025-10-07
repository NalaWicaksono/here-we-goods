from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    # pages
    path("", views.product_list, name="show_main"),

    # auth pages
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),

    # products (non-AJAX fallback pages)
    path("products/new/", views.product_create, name="add_product"),
    path("products/<int:pk>/", views.product_detail, name="product_detail"),
    path("products/<int:pk>/edit/", views.product_edit, name="product_edit"),
    path("products/<int:pk>/delete/", views.product_delete, name="product_delete"),

    # data delivery tugas sebelumnya
    path("json/", views.show_json, name="show_json"),
    path("xml/", views.show_xml, name="show_xml"),
    path("json/<int:id>/", views.show_json_by_id, name="show_json_by_id"),
    path("xml/<int:id>/", views.show_xml_by_id, name="show_xml_by_id"),

    # ===== AJAX API =====
    path("api/products/", views.api_products_list_create, name="api_products_list_create"),
    path("api/products/<int:pk>/", views.api_products_retrieve_update_delete, name="api_products_rud"),
    path("api/auth/login/", views.api_login, name="api_login"),
    path("api/auth/register/", views.api_register, name="api_register"),
    path("api/auth/logout/", views.api_logout, name="api_logout"),
]
