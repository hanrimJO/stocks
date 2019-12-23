from django.shortcuts import render
from django.http import JsonResponse



# Create your views here.


def stock_list(request):
    return render(request, 'stock/index.html', {})


def stock_chart(request):
    data = {
        'results': [1000, 3062, 6263, 18394, 18287, 28682, 31274, 33259, 2589, 24159, 32651, 31984, 38451]
    }

    return JsonResponse(data)
