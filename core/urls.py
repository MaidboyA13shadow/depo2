from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('hakkimizda/', views.AboutView.as_view(), name='about'),
    path('hizmetler/', views.ServicesView.as_view(), name='services'),
    path('projeler/', views.ProjectsView.as_view(), name='projects'),
    path('iletisim/', views.ContactView.as_view(), name='contact'),
    path('newsletter-signup/', views.newsletter_signup, name='newsletter_signup'),
]