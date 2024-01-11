from django.shortcuts import render
from django.views.generic import TemplateView
from site_module.models import SiteSettings, FooterLink, FooterlinkTitle
from home_module.models import Slider


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home_module/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sliders = Slider.objects.filter(is_active=True)
        context['sliders'] = sliders
        return context


def header_component(request):
    site_settings = SiteSettings.objects.filter(is_main_settings=True).first()
    context = {'settings': site_settings}
    return render(request, 'shared/header_component.html', context)


def footer_component(request):
    site_settings = SiteSettings.objects.filter(is_main_settings=True).first()
    footerbox = FooterLink.objects.all()
    footer_title = FooterlinkTitle.objects.all()
    context = {'settings': site_settings,
               'footer_title': footer_title}
    return render(request, 'shared/footer_component.html', context)


class AboutUsView(TemplateView):
    template_name = 'home_module/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_detail = SiteSettings.objects.filter(is_main_settings=True).first()
        context['site_detail'] = site_detail
        return context
