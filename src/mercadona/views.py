from .models import produit, promotion, categorie
from django.shortcuts import redirect, render
from .forms import produitForm, promotionForm, categorieForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def mercadona_list(request):
    product = produit.objects.all()
    promo = promotion.objects.all()
    cat = categorie.objects.all()
    context = {"product": product, "promo": promo, "cat": cat}
    return render(request, "mercadona/list.html", context)

@login_required
def produit_new(request):
    cat = categorie.objects.all()
    if request.method == "POST":
        form = produitForm(request.POST,request.FILES)
        if form.is_valid():
            produit = form.save(commit=False)
            produit.save()
            return redirect('produit_new')
    else:
        form = produitForm()
    context = {'form':form, "cat": cat}
    return render(request,"mercadona/produit_new.html",context)

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate (request, username=username, password=password)
        if user is None:
            context = {"erreur" : "mot de passe ou nom d'utilisateur invalide."}
            return render(request, "mercadona/login.html", context)
        login(request, user)
        return redirect("/")
    return render(request, "mercadona/login.html",{})

def logout_view(request):
    logout(request)
    return redirect("/")

def delete_product(request, product_id):
    product = produit.objects.get(pk=product_id)
    product.delete()
    return redirect("/")

@login_required
def promo_new(request):
    if request.method == "POST":
        form = promotionForm(request.POST)

        if form.is_valid():
            promotion = form.save(commit=False)
            promotion.save()
            return redirect('/')
    else:
        form = promotionForm()
    context = {'form':form}
    return render(request, "mercadona/promo_new.html", context)


