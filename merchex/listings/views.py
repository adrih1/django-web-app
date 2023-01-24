

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Annonce


def hello(request):
    bands = Band.objects.all()
    annonces = Annonce.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont:<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
        <p>Dernières annonces:<p>
        <ul>
            <li>{annonces[0].title}</li>
            <li>{annonces[1].title}</li>
            <li>{annonces[2].title}</li>
        </ul>
""")

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons la merch !</p>')

def listings(request):
    return HttpResponse('<h1>Listings</h1> <p>Tous les produits !</p>')

def contact(request):
    return HttpResponse("<h1>Contact</h1> <p>N'hésitez pas à nous contacter</p>")