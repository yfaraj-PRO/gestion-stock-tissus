from decimal import Decimal, InvalidOperation

from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .models import Tissu
from django.contrib.auth.decorators import login_required

@login_required
def liste_tissus(request):
    recherche = request.GET.get("q", "")
    tissus = Tissu.objects.all().order_by("nom")
    if recherche:
        tissus = tissus.filter(
            Q(nom__icontains=recherche)
            | Q(couleur__icontains=recherche)
            | Q(reference__icontains=recherche)
        )
    return render(
        request,
        "produits/liste.html",
        {"tissus": tissus, "recherche": recherche},
    )

@login_required
def modifier_stock(request, tissu_id):
    if request.method == "POST":
        tissu = get_object_or_404(Tissu, pk=tissu_id)
        try:
            quantite = Decimal(request.POST.get("quantite", "0"))
        except InvalidOperation:
            quantite = Decimal("0")

        if request.POST.get("action") == "retirer":
            quantite = -quantite

        nouveau_stock = tissu.metrage_stock + quantite
        tissu.metrage_stock = max(nouveau_stock, Decimal("0"))
        tissu.save()
    return redirect("liste_tissus")