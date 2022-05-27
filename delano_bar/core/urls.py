from django.urls import path

from delano_bar.core.views import HomeView, EventsView, MenuView, PhotoGalleryView, CocktailMenuView, BeerMenuView, \
    SoftDrinksMenuView, AlcoholMenuView, contacts_view, EventDetailsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('events/?order=down', EventsView.as_view(), name='events'),
    path('event-details/<int:pk>/', EventDetailsView.as_view(), name='event details'),
    path('menu/?order=down', MenuView.as_view(), name='menu'),
    path('cocktails-menu/?order=down', CocktailMenuView.as_view(), name='cocktail menu'),
    path('beer-menu/?order=down', BeerMenuView.as_view(), name='beer menu'),
    path('softdrinks-menu/?order=down', SoftDrinksMenuView.as_view(), name='soft drinks menu'),
    path('alcohol-menu/?order=down', AlcoholMenuView.as_view(), name='alcohol menu'),
    path('photo-gallery/?order=down', PhotoGalleryView.as_view(), name='photo gallery'),
    path('contact/?order=down', contacts_view, name='contacts')
]