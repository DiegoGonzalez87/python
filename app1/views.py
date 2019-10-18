from django.http import HttpResponse
import json

def test1(request):
    return HttpResponse('Pagina 2')

def test3(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)

    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'request successfully'
    }

    return HttpResponse(
        json.dumps(data, indent=4),
        content_type = 'application/json'
    )