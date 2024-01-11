from django.shortcuts import render, redirect
from .forms import ContactUsForm, ContactUsModelForm
from django.views.generic.edit import FormView
from django.urls import reverse
from site_module.models import SiteSettings


# def contact_us_page(request):
# -------------------------------------first option-------------------------------------------
# if request.method == "POST":
#     contact_form = ContactUsForm(request.POST)
#     if contact_form.is_valid():
#         print(contact_form.cleaned_data)
#         return redirect('home_page')
# else:
#     contact_form = ContactUsForm()
#
# return render(request, 'contact_us_module/conact_us.html', {
#     "contact_form": contact_form
# })

# -------------------------------------other option-------------------------------------------

# if request.method == 'POST':
#     contact_form = ContactUsModelForm(request.POST)
#     if contact_form.is_valid():
#         contact_form.save()
#         return redirect('home_page')
# else:
#     contact_form = ContactUsModelForm()
#
# return render(request, 'contact_us_module/conact_us.html', {
#     'contact_form': contact_form
# })


class ContactUsFormView(FormView):
    template_name = 'contact_us_module/conact_us.html'
    form_class = ContactUsModelForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_settings = SiteSettings.objects.filter(is_main_settings=True).first()
        context['site_info']= site_settings
        return context

    def get_success_url(self):
        return reverse('success-form-page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def success_page(request):
    return render(request, 'contact_us_module/success_page.html')
