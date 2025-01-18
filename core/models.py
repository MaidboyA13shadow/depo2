from django.db import models

class ServiceFeature(models.Model):
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = 'Hizmet Özelliği'
        verbose_name_plural = 'Hizmet Özellikleri'

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.ImageField(upload_to='services/icons/')
    features = models.ManyToManyField(ServiceFeature)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Hizmet'
        verbose_name_plural = 'Hizmetler'
    
    def __str__(self):
        return self.title

class Technology(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='technologies/logos/')
    
    class Meta:
        verbose_name = 'Teknoloji'
        verbose_name_plural = 'Teknolojiler'
    
    def __str__(self):
        return self.name

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Projesi'),
        ('mobile', 'Mobil Uygulama'),
        ('ecommerce', 'E-Ticaret'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    technologies = models.ManyToManyField(Technology)
    link = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title

class PricingPackage(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.ManyToManyField(ServiceFeature)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
    
    def __str__(self):
        return self.question

class Contact(models.Model):
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    maps_embed_code = models.TextField(blank=True)
    
    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'İletişim Bilgisi'
        verbose_name_plural = 'İletişim Bilgileri'


class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Bülten Aboneliği'
        verbose_name_plural = 'Bülten Abonelikleri'