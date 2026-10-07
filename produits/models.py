from django.db import models


class TypeTissu(models.Model):
    nom = models.CharField(max_length=100)

    class Meta:
        verbose_name = "type de tissu"
        verbose_name_plural = "types de tissu"

    def __str__(self):
        return self.nom


class Tissu(models.Model):
    reference = models.CharField(max_length=50, blank=True)
    nom = models.CharField(max_length=200)
    type_tissu = models.ForeignKey(TypeTissu, on_delete=models.SET_NULL, null=True, blank=True)
    couleur = models.CharField(max_length=50)
    largeur_cm = models.IntegerField(default=150)
    prix_metre = models.DecimalField(max_digits=10, decimal_places=2)
    metrage_stock = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    seuil_alerte = models.DecimalField(max_digits=8, decimal_places=2, default=10)

    class Meta:
        verbose_name_plural = "tissus"

    def stock_bas(self):
        return self.metrage_stock <= self.seuil_alerte

    def couleur_css(self):
        couleurs = {
            "blanc": "#f5f5f0", "noir": "#1a1a1a", "rouge": "#b3263a",
            "bleu": "#2a4d9b", "vert": "#2e7d4f", "jaune": "#e8c21a",
            "rose": "#e68ab0", "gris": "#8a8d93", "beige": "#d8c3a0",
            "marron": "#6b4430", "orange": "#e07a1f", "violet": "#6a3d9a",
            "turquoise": "#2bb3b1",
        }
        return couleurs.get(self.couleur.strip().lower(), "#9aa3b5")

    def __str__(self):
        return f"{self.nom} - {self.couleur}"