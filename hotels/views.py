from django.shortcuts import render
from django.http import HttpResponse

hotels = [
    {
        'city': 'bogota',
        'user': {
            'adminstrator': 'Diego Gonzalez'
        },
        'picture': 'https://picsum.photos/200/200/?image=903'
    },
    {
        'city': 'medellin',
        'user': {
            'adminstrator': 'Aljandro Acuna'
        },
        'picture': 'https://picsum.photos/200/200/?image=1076'
    },
    {
        'city': 'pasto',
        'user': {
            'adminstrator': 'Gonzalez Acuna'
        },
        'picture': 'https://picsum.photos/200/200/?image=1036'
    }

]

def list_hotels(request):
    return render(request, 'feed.html', {'data': hotels})



# Create your views here.
