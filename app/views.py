from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from order.models import OrderItem, Order
from django.contrib.auth.models import User
from django.db import models
from .forms import AnketaForm
from blog.models import Blog
from product.models import Product
from cart.cart import Cart

def home(request):
    """Renders the home page."""
    cart = Cart(request)
    products = Product.objects.order_by('-created')[:3]
    last = Blog.objects.order_by('-posted')[:3]
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'СТО',
            'cart': cart,
            'last': last,
            'products': products,
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    cart = Cart(request)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'cart': cart,
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    cart = Cart(request)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
        	'cart': cart,
            'title':'Автосервис Локнянский район',
            'message':'Вас приветствует компания «СТО»!',
            'year':datetime.now().year,
        }
    )
def links(request):
    """Renders the contact page."""
    cart = Cart(request)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
        	'cart': cart,
            'title':'Полезные ресурсы',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def registration(request):
    """Renders the registration page."""
    cart = Cart(request)
    if request.method == "POST": # после отправки формы
        regform = UserCreationForm(request.POST)
        if regform.is_valid(): #валидация полей формы
            reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы
            reg_f.is_staff = False # запрещен вход в административный раздел
            reg_f.is_active = True # активный пользователь
            reg_f.is_superuser = False # не является суперпользователем
            reg_f.date_joined = datetime.now() # дата регистрации
            reg_f.last_login = datetime.now() # дата последней авторизации

            reg_f.save() # сохраняем изменения после добавления данных

            return redirect('login') # переадресация на главную страницу после регистрации
    else:
        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html',
        {
        'regform': regform, # передача формы в шаблон веб-страницы
        'cart': cart,
        'year':datetime.now().year,
        }

)

def anketa(request):
    cart = Cart(request)
    assert isinstance(request, HttpRequest)
    data = None
    dov = {'1': 'Очень доволен/льна', '2':'Доволен/льна', '3':'Скорее доволен/льна', '4':'Скорее недоволен/льна', '5':'Недоволен/льна', '6':'Очень недоволен/льна'}
    rek = {'1':'Несомненно да', '2':'Вероятно да', '3':'Я не знаю', '4':'Вероятно нет', '5':'Несомненно нет'}
    avto = {'1': 'Да' , '2': 'Нет,но планирую приобретение', '3': 'Нет'}
    if request.method == 'POST':
        form = AnketaForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['dov'] = dov[ form.cleaned_data['dov'] ]
            data['rek'] = rek[ form.cleaned_data['rek'] ]
            data['avto'] = avto[ form.cleaned_data['avto'] ]
            if(form.cleaned_data['notice'] == True):
                data['notice'] = 'Да'
            else:
                data['notice'] = 'Нет'
            data['email'] = form.cleaned_data['email']
            data['message'] = form.cleaned_data['message']
            form = None
    else:
         form = AnketaForm()
    return render(
        request,
        'app/anketa.html',
        {
            'form':form,
            'data':data,
            'cart': cart,
            }
        )

def videopost(request):
    """Renders the about page."""
    cart = Cart(request)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'Видео',
            'cart': cart,
            'message':'Приятного просмотра!',
            'year':datetime.now().year,
              }
    )

def services(request):
    """Renders the services page."""
    cart = Cart(request)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/services.html',
        {
            'title':'Услуги',
            'cart': cart,
            'message':'Наши услуги',
            'year':datetime.now().year,
        }
    )
def to(request):
    """Renders the to page."""
    cart = Cart(request)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/to.html',
        {
            'title':'ТО автомобиля',
            'cart': cart,
            'message':'Техническое обслуживание автомобиля (ТО авто) – совокупность действий, предпринимаемых в целях создания безопасных условий использования транспортного средства. ',
            'year':datetime.now().year,
        }
    )
def kompl(request):
    """Renders the diagnost page."""
    cart = Cart(request)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/kompl.html',
        {
            'title':'Комплексная диагностика автомобиля',
            'cart': cart,
            'message':'Комплексная диагностика автомобиля — единственный способ своевременно «пролечить» транспортное средство и предупредить серьезные проблемы в работе всех узлов. Вынужденный ремонт всегда обходится дороже регулярной профилактики.',
            'year':datetime.now().year,
        }
    )
def dvs(request):
    """Renders the dvs page."""
    cart = Cart(request)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/dvs.html',
        {
            'title':'Капитальный ремонт ДВС',
            'cart': cart,
            'message':'Что такое капитальный ремонт двигателя автомобиля?',
            'year':datetime.now().year,
        }
    )
def diagnost(request):
    """Renders the kompl page."""
    cart = Cart(request)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/kompl.html',
        {
            'title':'Компьютерная диагностика автомобиля',
            'cart': cart,
            'message':'Высокотехнологичные электронные системы современного автомобиля гарантируют стабильную работу и безопасную эксплуатацию транспортного средства. Появление ошибок в работе таких систем влечет за собой серьезные поломки дорогостоящих элементов и, как следствие, высокие затраты.',
            'year':datetime.now().year,
        }
    )
def torm(request):
    """Renders the torm page."""
    cart = Cart(request)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/torm.html',
        {
            'title':'Тормозная система',
            'cart': cart,
            'message':'Важность своевременного обслуживания тормозной системы.',
            'year':datetime.now().year,
        }
    )
def ryl(request):
    """Renders the ryl page."""
    cart = Cart(request)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/ryl.html',
        {
            'title':'Рулевое управление',
            'cart': cart,
            'message':'Как важна исправность рулевого управления.',
            'year':datetime.now().year,
        }
    )
    
def allorders(request):
    cart = Cart(request)
    orders = OrderItem.objects.all()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/allorders.html',
        {
            'title':'Все заказы',
            'cart': cart,
            'orders': orders,
            'year':datetime.now().year,
        }
    )

@login_required(login_url='/login/')
def userorders(request):
    cart = Cart(request)
    orders = Order.objects.filter(user = request.user)
    items = OrderItem.objects.filter(username = request.user)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/userorders.html',
        {
            'title':'Мои заказы',
            'cart': cart,
            'items': items,
            'orders': orders,
            'year':datetime.now().year,
        }
    )