from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import Category
from customers.models import Customer


def Home(request):
    """
    Fonction qui renvoie l'utilsiateur à la landing page
    """
    return render(request, "home.html")


def category_product_list(request):
    categories = Category.objects.prefetch_related("product_set")
    return render(request, "category_product_list.html", {"categories": categories})


def list_customers(request):
    customers = Customer.objects.all()
    return render(request, "list_customers.html", {"customers": customers})


@login_required
def dashboard_view(request):
    """
    Affiche la page du tableau de bord pour l'utilisateur connecté.

    Cette page permet à l'utilisateur d'effectuer différentes actions,
    telles que la création de clients, de produits, etc.
    """
    user = request.user
    return render(request, "dashboard.html", context={user: user})


class UserRegisterView(CreateView):
    """
    Vue pour l'enregistrement d'un nouvel utilisateur.

    Cette page permet à l'utilisateur de s'inscrire en remplissant un formulaire.
    Après une inscription réussie, l'utilisateur est redirigé vers la page de connexion.
    """

    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")


class UserLoginView(LoginView):
    template_name = "users/login.html"


class UserLogoutView(LogoutView):
    template_name = "users/logout.html"
