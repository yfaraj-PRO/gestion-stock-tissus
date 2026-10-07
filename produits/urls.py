from django.urls import path

from . import views

urlpatterns = [
    path("", views.liste_tissus, name="liste_tissus"),
    path("stock/<int:tissu_id>/", views.modifier_stock, name="modifier_stock"),
]