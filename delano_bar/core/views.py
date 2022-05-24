from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from delano_bar.core.models import Product, Event, PromoEvent


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        event = Event.objects.first()
        context['event'] = event
        context['products'] = Product.objects.all()
        return context


class EventsView(ListView):
    template_name = 'no-sidebar.html'
    queryset = Event.objects.all()


class PromoEventsView(ListView):
    template_name = 'right-sidebar.html'
    queryset = PromoEvent.objects.all()


class MenuView(ListView):
    template_name = 'menu/main-menu.html'
    queryset = Product.objects.all()
    context_object_name = 'products'


class CocktailMenuView(ListView):
    template_name = 'menu/cocktails-menu.html'
    queryset = Product.objects.all()
    context_object_name = 'cocktails'


class BeerMenuView(ListView):
    template_name = 'menu/beer-menu.html'
    queryset = Product.objects.all()
    context_object_name = 'beers'


class SoftDrinksMenuView(ListView):
    template_name = 'menu/soft-drinks-menu.html'
    queryset = Product.objects.all()
    context_object_name = 'soft_drinks'


class AlcoholMenuView(ListView):
    template_name = 'menu/alcohol-menu.html'
    queryset = Product.objects.all()
    context_object_name = 'alcohol'


class ContactsView(TemplateView):
    pass

