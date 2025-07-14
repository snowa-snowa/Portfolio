from django.views.generic import TemplateView

class page1(TemplateView):
    template_name = 'page1.html'

class page2(TemplateView):
    template_name = 'page2.html'
