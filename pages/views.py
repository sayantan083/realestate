from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing
from realtors.models import Realtor
from django.conf import settings

from .mixins import Directions
'''
Basic view for routing 
'''
def route(request):

	context = {"google_api_key": settings.GOOGLE_API_KEY}
	return render(request, 'pages/route.html', context)


'''
Basic view for displaying a map 
'''
def map(request):

	lat_a = request.GET.get("lat_a")
	long_a = request.GET.get("long_a")
	lat_b = request.GET.get("lat_b")
	long_b = request.GET.get("long_b")
	# directions = Directions(lat_a= lat_a, long_a=long_a, lat_b = lat_b, long_b=long_b)

	context = {
		"google_api_key": settings.GOOGLE_API_KEY,
		"lat_a": lat_a,
		"long_a": long_a,
		"lat_b": lat_b,
		"long_b": long_b,
		"origin": f'{lat_a}, {long_a}',
		"destination": f'{lat_b}, {long_b}',
		# "directions": directions,

	}
	return render(request, 'pages/map.html', context)

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)