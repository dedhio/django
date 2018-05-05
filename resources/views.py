from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "hello.html", {"frota": 300})

def custom(request):
    vehivle_1 = Vehicle("Palio", "Fiat")
    vehivle_2 = Vehicle("Onix", "GM")
    list_vehicle = [vehivle_1, vehivle_2]

    return render(request, "teste.html", {"vehicles": list_vehicle})