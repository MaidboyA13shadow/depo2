from django.contrib import admin
from django.contrib.admin.apps import AdminConfig
from django.contrib.auth.models import Group, User
from .models import (
    Service, 
    ServiceFeature, 
    Technology, 
    PricingPackage, 
    FAQ,
    Project,
    Contact,
)
from .models import Newsletter

# Admin site özelleştirme
admin.site.site_header = 'Dijihype Yönetim Paneli'
admin.site.site_title = 'Dijihype Admin'
admin.site.index_title = 'Yönetim Paneli'

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 20
    ordering = ['name']
    
    fieldsets = (
        ('Teknoloji Bilgileri', {
            'fields': ('name', 'logo'),
            'classes': ('wide', 'extrapretty'),
        }),
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order', 'created_at']
    list_filter = ['category', 'technologies']
    search_fields = ['title', 'description']
    list_editable = ['order']
    filter_horizontal = ['technologies']
    list_per_page = 20
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Proje Bilgileri', {
            'fields': ('title', 'description', 'image'),
            'classes': ('wide', 'extrapretty'),
        }),
        ('Kategori ve Teknolojiler', {
            'fields': ('category', 'technologies'),
            'classes': ('wide',),
        }),
        ('Diğer Bilgiler', {
            'fields': ('link', 'order'),
            'classes': ('wide',),
        }),
    )

@admin.register(ServiceFeature)
class ServiceFeatureAdmin(admin.ModelAdmin):
    list_display = ['description']
    search_fields = ['description']
    list_per_page = 20
    
    fieldsets = (
        ('Özellik Bilgileri', {
            'fields': ('description',),
            'classes': ('wide', 'extrapretty'),
        }),
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']
    filter_horizontal = ['features']
    search_fields = ['title', 'description']
    list_per_page = 20
    
    fieldsets = (
        ('Hizmet Bilgileri', {
            'fields': ('title', 'description', 'icon'),
            'classes': ('wide', 'extrapretty'),
        }),
        ('Özellikler ve Sıralama', {
            'fields': ('features', 'order'),
            'classes': ('wide',),
        }),
    )

@admin.register(PricingPackage)
class PricingPackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'order']
    list_editable = ['price', 'order']
    filter_horizontal = ['features']
    search_fields = ['name']
    list_per_page = 20
    
    fieldsets = (
        ('Paket Bilgileri', {
            'fields': ('name', 'price'),
            'classes': ('wide', 'extrapretty'),
        }),
        ('Özellikler ve Sıralama', {
            'fields': ('features', 'order'),
            'classes': ('wide',),
        }),
    )

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'order']
    list_editable = ['order']
    search_fields = ['question', 'answer']
    list_per_page = 20
    
    fieldsets = (
        ('Soru ve Cevap', {
            'fields': ('question', 'answer'),
            'classes': ('wide', 'extrapretty'),
        }),
        ('Sıralama', {
            'fields': ('order',),
            'classes': ('wide',),
        }),
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone']
    search_fields = ['email', 'phone', 'address']
    
    fieldsets = (
        ('İletişim Bilgileri', {
            'fields': ('email', 'phone', 'address'),
            'classes': ('wide', 'extrapretty'),
        }),
        ('Harita', {
            'fields': ('maps_embed_code',),
            'classes': ('wide',),
        }),
    )


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_at']
    search_fields = ['email']
    list_per_page = 20