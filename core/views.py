from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from .models import Service, Technology, Project, PricingPackage, FAQ
class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.first()
        return context

class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.first()
        return context

class ServicesView(TemplateView):
    template_name = 'core/services.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['technologies'] = Technology.objects.all()
        context['packages'] = PricingPackage.objects.all()
        context['faqs'] = FAQ.objects.all()
        return context

class ProjectsView(TemplateView):
    template_name = 'core/projects.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context

class ContactView(TemplateView):
    template_name = 'core/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.first()
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # E-posta gönderme işlemi
        email_message = f"""
        Yeni İletişim Formu Mesajı:
        
        İsim: {name}
        E-posta: {email}
        Telefon: {phone}
        Konu: {subject}
        
        Mesaj:
        {message}
        """

        try:
            send_mail(
                subject=f'Yeni İletişim Formu Mesajı: {subject}',
                message=email_message,
                from_email=email,
                recipient_list=['info@dijihype.com'],  # Şirket e-posta adresiniz
                fail_silently=False,
            )
            messages.success(request, 'Mesajınız başarıyla gönderildi. En kısa sürede size dönüş yapacağız.')
        except:
            messages.error(request, 'Mesajınız gönderilirken bir hata oluştu. Lütfen daha sonra tekrar deneyin.')

        return redirect('core:contact')

def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            Newsletter.objects.create(email=email)
            messages.success(request, 'Bültenimize başarıyla abone oldunuz!')
        except:
            messages.error(request, 'Bu e-posta adresi zaten kayıtlı veya geçersiz.')
        return redirect('core:contact')