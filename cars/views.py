from django.http import HttpResponse
from django.shortcuts import render
from .models import CarModel


def cars_list_view(request):
    cars = CarModel.objects.all()
    q = request.GET.get('q')
    if q:
        cars = cars.filter(title__icontains=q)

    context = {'cars': cars}
    return render(request, 'cars.html', context)


def car_detail_view(request, pk):
    car = CarModel.objects.filter(id=pk).first()
    if car:
        context = {'car': car}
        return render(request, 'cars-detail.html', context)
    else:
        return HttpResponse('Car not found')


def download_car_view(request, pk):
    car = CarModel.objects.filter(id=pk).first()

    if car:
        file_path = str(car.ecar)
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            return response
    else:
        return HttpResponse("Car not found")
