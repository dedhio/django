from datetime import date
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
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

    
class VehicleRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'vehicle_detail'

    def get_redirect_url(self, *args, **kwargs):
        vehicle = get_object_or_404(Vehicle, pk=kwargs['pk'])
        return super(VehicleRedirectView, self).get_redirect_url(*args, **kwargs)


class VehicleCreate(CreateView):
    model = Vehicle
    template_name = 'vehicle_form.html'
    fields = ['name', 'plate', 'description', 'licence_plate', 'manufacture_year', 'manufacturer']
    success_url = reverse_lazy('vehicle_list')


class VehicleUpdate(UpdateView):
    model = Vehicle
    template_name = 'vehicle_form.html'
    fields = ['name', 'plate', 'description', 'licence_plate', 'manufacture_year', 'manufacturer']
    success_url = reverse_lazy('vehicle_list')


class VehicleDelete(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicle_list')
    template_name = 'vehicle_confirm_delete.html'


class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'


class VehicleListView(ListView):
    model = Vehicle
    template_name = 'list_vehicle.html'
    queryset = Vehicle.objects.order_by('name')
    context_object_name = 'vehicle_list'
    paginate_by = 5

    def get_queryset(self):
        return Vehicle.objects.filter(is_active=True).filter(manufacture_year__gt=date(2012,1,1)).order_by('licence_plate')


class UseControlList(ListView):
    template_name = "usecontrol_list.html"

    def get_context_data(self, **kwargs):
        context = super(UseControlList, self).get_context_data(**kwargs)

        usecontrol = UseControl.objects.selected_related("vehicle").selected_related("driver").all().first()

        context['driver'] = usecontrol.driver.name
        context['vehicle'] = usecontrol.vehicle.name
        context['date_started'] = usecontrol.date_started

        return context