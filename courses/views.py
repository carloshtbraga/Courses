from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from .models import Instrutor, Curso, Categoria
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout


def index(request):
    return render(request, "index.html")


def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("password")
        is_instructor = request.POST.get("is_instructor")
        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse("Usuário já existe")
        else:
            user = User.objects.create_user(
                username=username, email=email, password=senha
            )
            user.save()
            if is_instructor == "1":
                grupo_instrutores = Group.objects.get(name="Instrutores")
                user.groups.add(grupo_instrutores)
                foto = request.FILES.get("imagem")
                biography = request.POST.get("biography")
                instrutor = Instrutor(user=user, biografia=biography, foto=foto)
                instrutor.save()
            return redirect("login")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        senha = request.POST.get("password")
        user = authenticate(username=username, password=senha)
        if user:
            django_login(request, user)
            return redirect("main")
        else:
            return HttpResponse("Usuário ou senha inválidos")


def logout(request):
    django_logout(request)
    return redirect("index")


def main(request):
    is_logged = request.user.is_authenticated
    if is_logged:
        categorias = Categoria.objects.all()
        cursos = Curso.objects.all()
        is_instrutor = request.user.groups.filter(name="Instrutores").exists()
        context = {
            "cursos": cursos,
            "is_instrutor": is_instrutor,
            "categorias": categorias,
        }
        return render(request, "main.html", context)

    else:
        return HttpResponse("Você não está logado")


def instrutores_area(request):
    is_instrutor = request.user.groups.filter(name="Instrutores").exists()
    if is_instrutor:
        if request.method == "GET":
            categorias = Categoria.objects.all()
            context = {"categorias": categorias}
            return render(request, "instrutores_area.html", context)
        elif request.method == "POST":
            # Obtenha os dados do formulário
            titulo = request.POST.get("titulo")
            descricao = request.POST.get("descricao")
            preco = request.POST.get("preco")
            categorias = request.POST.getlist("categorias")

            # Acesse a imagem enviada pelo usuário
            imagem = request.FILES.get("imagem")

            # Crie o curso e associe-o ao instrutor
            curso = Curso.objects.create(
                título=titulo,
                descrição=descricao,
                preço=preco,
                instrutor=request.user.instrutor,
                image=imagem,  # Associe a imagem ao curso
            )

            # Associe as categorias selecionadas ao curso
            curso.categorias.set(categorias)

            return redirect("main")
    else:
        return HttpResponse("Você não é um instrutor")


def course_details(request, curso_id):
    is_logged = request.user.is_authenticated
    if is_logged:
        curso = get_object_or_404(Curso, pk=curso_id)
        return render(request, "course_details.html", {"curso": curso})
    else:
        return HttpResponse("Você não está logado")


def search_courses(request):
    categorias = Categoria.objects.all()
    title = request.GET.get("title", "")
    category_id = request.GET.get("category", "")

    courses = Curso.objects.filter(título__icontains=title)

    if category_id:
        courses = courses.filter(categorias__id=category_id)

    return render(request, "main.html", {"cursos": courses, "categorias": categorias})
