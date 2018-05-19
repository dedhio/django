from datetime import date
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from .models import Manufacturer, Vehicle, Driver, UseControl


def index(request):

    return render(request, "hello.html", {"frota": 300})


def custom(request):

    vehivle_1 = Vehicle("Palio", "Fiat")
    vehivle_2 = Vehicle("Onix", "GM")
    list_vehicle = [vehivle_1, vehivle_2]

    return render(request, "teste.html", {"vehicles": list_vehicle})


def use_control_add(request):

    manufacturer = Manufacturer()
    manufacturer.name = "Audi"
    manufacturer.save()

    # vehicle = Vehicle("Ecosport", "Ford", "" , "ETT4512", date(2013, 8, 20), Manufacturer())        
    vehicle = Vehicle()
    vehicle.name = "Ecosport"
    vehicle.plate = "Ford"
    vehicle.description = "Conservado"
    vehicle.licence_plate = "QWE9031"
    vehicle.manufacture_year = date(2013, 8, 20)
    vehicle.manufacturer = manufacturer
    vehicle.save()

    driver = Driver()
    driver.name = "Geovani"
    driver.save()

    use_control = UseControl()
    use_control.driver = driver
    use_control.vehicle = vehicle
    use_control.save()

    return HttpResponse('Modelos criados com sucesso')


def use_control_list(request):
    ''' Busca Primeiro '''
    usecontrol = UseControl.objects.all().first()
    data = {
        'vehicle': usecontrol.vehicle.name,
        'driver': usecontrol.driver.name,
        'date_started': usecontrol.date_started
    }
    return render(request, 'usecontrol_list.html', data)


class UseControlList(TemplateView):
    template_name = "usecontrol_list.html"

    def get_context_data(self, **kwargs):
        context = super(UseControlList, self).get_context_data(**kwargs)

        usecontrol = UseControl.objects.all().first()

        context['driver'] = usecontrol.driver.name
        context['vehicle'] = usecontrol.vehicle.name
        context['date_started'] = usecontrol.date_started

        return context

    
class VehicleCreate(CreateView):
    model = Vehicle
    template_name = 'vehicle_form.html'
    fields = ['name', 'plate', 'description', 'licence_plate', 'manufacture_year', 'manufacturer']
    success_url = reverse_lazy('vehicle_add')


class VehicleUpdate(UpdateView):
    model = Vehicle
    template_name = 'vehicle_form.html'
    fields = ['name', 'plate', 'description', 'licence_plate', 'manufacture_year', 'manufacturer']
    success_url = reverse_lazy('vehicle_add')


class VehicleDelete(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicle_add')
    template_name = 'vehicle_confirm_delete.html'