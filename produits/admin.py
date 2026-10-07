from django.contrib import admin
from .models import TypeTissu, Tissu


@admin.register(TypeTissu)
class TypeTissuAdmin(admin.ModelAdmin):
    list_display = ("nom",)


@admin.register(Tissu)
class TissuAdmin(admin.ModelAdmin):
    list_display = ("reference", "nom", "type_tissu", "couleur", "largeur_cm", "prix_metre", "metrage_stock")
    list_filter = ("type_tissu", "couleur")
    search_fields = ("nom", "reference", "couleur")