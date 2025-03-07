from django.shortcuts import render
from cars.models import Car

# Create your views here.

def cars_view(request):
    
    cars = Car.objects.all().order_by('-model')
    search = request.GET.get('search') #filtrando pelo parametro seach
    
    
    # se o usuario mandar realizar uma busca, ele vai filtrar os carros
    if search:
        cars = Car.objects.filter(model__icontains=search)

    
    
    return render(
        request, 
        'cars.html',
        {'cars': cars}
        
    )
