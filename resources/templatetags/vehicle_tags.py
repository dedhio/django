from django import template
from resources.models import Vehicle

register = template.Library()

@register.simple_tag
def get_vehicle(number_items):
    list_vehicle = list()

    list_vehicle.append(Vehicle("Uno", "Fiat"))
    list_vehicle.append(Vehicle("Celta", "GM"))
    list_vehicle.append(Vehicle("Palio", "Fiat"))
    list_vehicle.append(Vehicle("Cruze", "GM"))
    list_vehicle.append(Vehicle("Golf", "VW"))
    list_vehicle.append(Vehicle("Ecosport", "Ford"))
    
    return list_vehicle[:number_items]