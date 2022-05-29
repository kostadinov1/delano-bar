from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.utils.timezone import now
from django.views.generic import TemplateView, ListView, DetailView

from delano_bar.core.forms import ContactForm
from delano_bar.core.models import Product, Event, PromoEvent, ProductCategory, Photos


# TODO PROMO EVENTS IN INDEX ?
# TODO PRICE FOR MILLILITERS AND FOR A BOTTLE ?
# TODO LOCAL PHOTOS FOR PRODUCTS ?
# TODO DISCUS PRODUCT CATEGORIES AND PRODUCT PHOTOS VIEWS(MENUS)?


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        event = Event.objects.filter(date__gte=now()).order_by('date').first
        photos = Photos.objects.all().order_by('created_on')[:6]
        context['photos'] = photos
        context['event'] = event
        context['products'] = Product.objects.all()
        return context



class EventsView(ListView):
    template_name = 'events.html'
    queryset = Event.objects.filter(date__gte=now()).order_by('date')
    context_object_name = 'events'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        events = Event.objects.all()
        if events:
            latest_event = events[events.count()-1]
            context['latest_event'] = latest_event

        past_events = Event.objects.filter(date__lte=now()).order_by('date')
        context['past_events'] = past_events
        return context


class EventDetailsView(DetailView):
    model = Event
    template_name = 'event-details.html'


class PhotoGalleryView(ListView):
    template_name = 'photo-galley.html'
    paginate_by = 6
    model = Photos
    ordering = '-created_on'
    context_object_name = 'images'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cover_image = Photos.objects.filter(cover_image=True).first()
        if cover_image:
            context['cover_image'] = cover_image
        latest_image = Photos.objects.all().order_by('-created_on').first

        if latest_image:
            context['latest_image'] = latest_image
        return context


class MenuView(ListView):
    template_name = 'menu/main-menu.html'
    queryset = Product.objects.all()
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MenuView, self).get_context_data()
        cocktails = Product.objects.filter(category__name='Cocktails').order_by('created_on')
        beers = Product.objects.filter(category__name='Soft-drinks').order_by('created_on')
        soft_drinks = Product.objects.filter(category__name='Beers').order_by('created_on')
        alcohols = Product.objects.filter(category__name='Alcohol').order_by('created_on')
        ice_creams = Product.objects.filter(category__name='Ice-cream').order_by('created_on')

        context['cocktails'] = cocktails
        context['beers'] = beers
        context['soft_drinks'] = soft_drinks
        context['alcohols'] = alcohols
        context['ice_creams'] = ice_creams

        return context

class CocktailMenuView(ListView):
    template_name = 'menu/cocktails-menu.html'
    queryset = Product.objects.filter(category__name='Cocktails').order_by('created_on')
    context_object_name = 'cocktails'
    paginate_by = 6


class BeerMenuView(ListView):
    template_name = 'menu/beer-menu.html'
    queryset = Product.objects.filter(category__name='Beers').order_by('created_on')
    context_object_name = 'beers'
    paginate_by = 6



class SoftDrinksMenuView(ListView):
    template_name = 'menu/soft-drinks-menu.html'
    queryset = Product.objects.filter(category__name='Soft-drinks').order_by('created_on')
    context_object_name = 'soft_drinks'
    paginate_by = 6


class AlcoholMenuView(ListView):
    template_name = 'menu/alcohol-menu.html'
    queryset = Product.objects.filter(category__name='Alcohol').order_by('created_on')
    context_object_name = 'alcohols'
    paginate_by = 6


def contacts_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            name = cleaned_data.get('name')
            email = cleaned_data.get('email')
            message = cleaned_data.get('message')
            send_mail(f'New Reservation message from {name}, f{email}', message, email, ['example@gmail.com'])
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'contacts.html', context)




