from django.urls import path
from .views import cadastro, login, index, main, instrutores_area, course_details

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("cadastro/", cadastro, name="cadastro"),
    path("login/", login, name="login"),
    path("main/", main, name="main"),
    path("", index, name="index"),
    path("instrutores", instrutores_area, name="instrutores_area"),
    path("cursos/<int:curso_id>", course_details, name="course_details"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
