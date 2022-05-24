from django.urls import path

from delano_bar.core.views import HomeView, EventsView, MenuView, PromoEventsView, CocktailMenuView, BeerMenuView, \
    SoftDrinksMenuView, AlcoholMenuView, ContactsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('events', EventsView.as_view(), name='events'),
    path('menu', MenuView.as_view(), name='menu'),
    path('cocktails-menu', CocktailMenuView.as_view(), name='cocktail menu'),
    path('beer-menu', BeerMenuView.as_view(), name='beer menu'),
    path('softdrinks-menu', SoftDrinksMenuView.as_view(), name='soft drinks menu'),
    path('alcohol-menu', AlcoholMenuView.as_view(), name='alcohol menu'),
    path('promo-events', PromoEventsView.as_view(), name='promo events'),
    path('contact', ContactsView.as_view(), name='contacts')
]