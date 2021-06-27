from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices

from .models import Listing, Lead
from realtors.models import Realtor

def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }

  return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)

  context = {
    'listing': listing
  }

  return render(request, 'listings/listing.html', context)
def create(request):
  '''
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  description = models.TextField(blank=True)
  price = models.DecimalField(max_digits=4, decimal_places=1)
  bedrooms = models.IntegerField()
  bathrooms = models.IntegerField(default=0)
  garage = models.IntegerField(default=0)
  sqft = models.IntegerField()
  lot_size = models.IntegerField(default=0)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  '''
  '''
  'title': [''], 'address': [''], 'city': [''], 'zipcode': [''], 'description': [''], 'bathrooms': [''], 'garage': [''], 'sqft': [''], 'lotsize': [''], 'photos': ['home.jpeg']}
  '''
  print(request.user)

  if not request.user.is_authenticated:
    return render(request, 'listings/create.html', context)
  if request.method == 'POST':
    print(request.POST)
    print(request.POST)
    print(request.FILES['photos'])
    realtor = Realtor.objects.all()
    listing_obj = Listing(title=request.POST['title'], address=request.POST['address'], city=request.POST['city'], state=request.POST['state'], price=int(request.POST['price']), zipcode=int(request.POST['zipcode']), description=request.POST['description'], bedrooms=int(request.POST['bedrooms']), bathrooms=int(request.POST['bathrooms']), garage=int(request.POST['garage']), sqft=int(request.POST['sqft']), photo_main=request.FILES['photos'],  )
    listing_obj.save()
    return redirect('listings')
  context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
  return render(request, 'listings/create.html', context)
    
    

  

  #listing_obj.save()



def search(request):
  queryset_list = Listing.objects.order_by('-list_date')

  keywords, city, state, price, bedrooms = "", "all", "all", 1000, 2
  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)

  # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
    'state_choices': state_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'listings': queryset_list,
    'values': request.GET
  }
  if request.user.is_authenticated:
      user_id = request.user.id
      lead = Lead(user_id = user_id, state=state, bedrooms = bedrooms, price=price, city=city, keywords=keywords)
      lead.save()

  return render(request, 'listings/search.html', context)