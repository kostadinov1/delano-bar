from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from delano_bar.core.models import Product


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['products'] = Product.objects.all()
        return context


