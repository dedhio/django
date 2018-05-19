from django import template
from resources.models import Vehicle
from datetime import date

register = template.Library()

@register.simple_tag
def get_vehicle(number_items):
    list_vehicle = list()

    list_vehicle.append(Vehicle("Uno", "Fiat", "Carro usado" , "ETT4512", date(2013, 8, 20), True))
    list_vehicle.append(Vehicle("Celta", "GM", "Carro de Leilao" , "EJV4665", date(2013, 8, 20), True))
    list_vehicle.append(Vehicle("Palio", "Fiat", "Cor vermelha" , "ARE8879", date(2013, 8, 20), True))
    list_vehicle.append(Vehicle("Cruze", "GM", "" , "ETT4512", date(2013, 8, 20), True))
    list_vehicle.append(Vehicle("Golf", "VW", "" , "ETT4512", date(2013, 8, 20), True))
    list_vehicle.append(Vehicle("Ecosport", "Ford", "" , "ETT4512", date(2013, 8, 20), True))
    
    return list_vehicle[:number_items]