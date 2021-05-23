"""
Definition of urls for sto.
"""



from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from datetime import datetime
import app.forms
import app.views
from django.shortcuts import render, redirect
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic import RedirectView

app_name = 'app'

urlpatterns = [
     path('', app.views.home, name='home'),
    path('contact/', app.views.contact, name='contact'),
    path('about/', app.views.about, name='about'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', app.views.registration, name='registration'),
    #path('blog/', views.blog, name='blog'),
    #path('blogpost/<parametr>/', views.blogpost, name='blogpost'),
    #path('newpost/', views.newpost, name='newpost'),
    path('blog/', include('blog.urls', namespace='blog')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('product/', include('product.urls', namespace='product')),
    path('order/', include('order.urls', namespace='orders')),
    # path('CartDetail/', views.CartDetail, name='CartDetail'),
    #path('remove/(<product_id>)/', views.CartRemove, name='CartRemove'),
    #path('add/(<product_id>)/', views.CartAdd, name='CartAdd'),
    #path('ProductList/', views.ProductList, name='ProductList'),
    #path('<category_slug>/', views.ProductList, name='ProductListByCategory'),
    #path('<slug>/', views.ProductDetail, name='ProductDetail'),
    #path('create/', views.OrderCreate, name='OrderCreate'),
    #path('admin/order/<order_id>/', views.AdminOrderDetail, name='AdminOrderDetail'),
    path('userorders/', app.views.userorders, name='userorders'),
    path('allorders/', app.views.allorders, name='allorders'),
    path('services/', app.views.services, name='services'),
    path('diagnost/', app.views.diagnost, name='diagnost'),
    path('to/', app.views.to, name='to'),
    path('dvs/', app.views.dvs, name='dvs'),
    path('kompl/', app.views.kompl, name='kompl'),
    path('torm/', app.views.torm, name='torm'),
    path('ryl/', app.views.ryl, name='ryl'),
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()