from django.urls import path
from .views import (
    cadastro,
    login,
    index,
    main,
    instrutores_area,
    course_details,
    logout,
    search_courses,
    carrinho,
    add_to_cart,
    remove_from_cart,
    checkout,
    checkout_confirmacao,
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("cadastro/", cadastro, name="cadastro"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("main/", main, name="main"),
    path("", index, name="index"),
    path("instrutores", instrutores_area, name="instrutores_area"),
    path("cursos/<int:curso_id>", course_details, name="course_details"),
    path("search_courses/", search_courses, name="search_courses"),
    path("carrinho/", carrinho, name="carrinho"),
    path("add_to_cart/<int:curso_id>", add_to_cart, name="add_to_cart"),
    path("remove_from_cart/<int:curso_id>", remove_from_cart, name="remove_from_cart"),
    path("checkout/", checkout, name="checkout"),
    path('checkout_confirmacao/', checkout_confirmacao, name='checkout_confirmacao'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
