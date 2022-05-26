from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.utils.timezone import now
from django.views.generic import TemplateView, ListView

from delano_bar.core.forms import ContactForm
from delano_bar.core.models import Product, Event, PromoEvent, ProductCategory, PhotoGallery


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        event = Event.objects.filter(date__gte=now()).order_by('date')[0]
        context['event'] = event
        context['products'] = Product.objects.all()
        return context


class EventsView(ListView):
    template_name = 'events.html'
    queryset = Event.objects.filter(date__gte=now()).order_by('date')
    context_object_name = 'events'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        events = Event.objects.all()
        latest_event = events[events.count()-1]
        context['latest_event'] = latest_event
        return context


class PhotoGalleryView(ListView):
    template_name = 'photo-galley.html'
    paginate_by = 6
    model = PhotoGallery
    ordering = '-created_on'
    context_object_name = 'images'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cover_image = PhotoGallery.objects.filter(cover_image=True).first()
        if cover_image:
            context['cover_image'] = cover_image
        latest_image = PhotoGallery.objects.all().order_by('-created_on').first

        if latest_image:
            context['latest_image'] = latest_image
        return context


class MenuView(ListView):
    template_name = 'menu/main-menu.html'
    queryset = Product.objects.all()
    context_object_name = 'products'


class CocktailMenuView(ListView):
    template_name = 'menu/cocktails-menu.html'
    queryset = Product.objects.filter(category__name='Cocktails')
    context_object_name = 'cocktails'


class BeerMenuView(ListView):
    template_name = 'menu/beer-menu.html'
    queryset = Product.objects.filter(category__name='Beers')
    context_object_name = 'beers'


class SoftDrinksMenuView(ListView):
    template_name = 'menu/soft-drinks-menu.html'
    queryset = Product.objects.filter(category__name='Soft-drinks')
    context_object_name = 'soft_drinks'


class AlcoholMenuView(ListView):
    template_name = 'menu/alcohol-menu.html'
    queryset = Product.objects.filter(category__name='Alcohol')
    context_object_name = 'alcohol'


def contacts_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            name = cleaned_data.get('name')
            email = cleaned_data.get('email')
            message = cleaned_data.get('message')
            send_mail(f'New BlogPost message from {name}', message=message, from_email=email, recipient_list=['somemail@mail.com'])
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'contacts.html', context)




