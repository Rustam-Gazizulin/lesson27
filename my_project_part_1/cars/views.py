from cars.models import Car
from django.http import JsonResponse

def list_car(request):
    cars = Car.objects.all()
    response = []
    for car in cars:
        response.append({
            'id': car.id,
            'slug': car.slug,
            'name': car.name,
            'brand': car.brand,
            'address': car.address,
            'description': car.description,
            'status': car.status,
            'created': car.created,
        })
    return JsonResponse(response, safe=False)

def get_car(request, pk):
    try:
        cars = Car.objects.get(id=pk)
    except Car.DoesNotExist:
        return JsonResponse({'error': 'not found'}, status=404)

    return JsonResponse({
        'id': cars.id,
        'slug': cars.slug,
        'name': cars.name,
        'brand': cars.brand,
        'address': cars.address,
        'description': cars.description,
        'status': cars.status,
        'created': cars.created,
    })


def search(request):
    cars = Car.objects.all()
    search_brand = request.GET.get('brand', None)
    if search_brand:
        cars = cars.filter(brand=search_brand)

    response = []
    for car in cars:
        response.append({
            'id': car.id,
            'name': car.name,
            'brand': car.brand,
            'status': car.status,
        })
    return JsonResponse(response, safe=False)

