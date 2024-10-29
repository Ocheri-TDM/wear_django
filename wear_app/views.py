from django.shortcuts import render, get_object_or_404, redirect
from .models import Car_card, Category, News
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm, CustomLoginForm
from django.contrib.auth.forms import AuthenticationForm 
import logging
# multi view-------------------------------------------------------------------------------

def index(request):
    categories = Category.objects.all()
    car_card = Car_card.objects.all().order_by('-date')[:20]

    context = {
        'categories': categories,
        'car_card': car_card
    }

    return render(request,"./index.html", context)

def categories(request, slug):
    categories = Category.objects.all()
    categories_filter = get_object_or_404(Category, slug=slug)
    car_card = Car_card.objects.filter(category=categories_filter) 

    context = {
        'categories': categories,
        'categories_filter': categories_filter,
        'car_card': car_card
    }

    return render(request, "categories.html", context)

def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def categories_by_filtred(request, slug):
    categories = Category.objects.all()  
    categories_filter = get_object_or_404(Category, slug=slug)
    car_card = Car_card.objects.filter(category=categories_filter) 

    context = {
        'categories': categories,
        'categories_filter': categories_filter,
        'car_card': car_card
    }

    return render(request, "categories-by-filtred.html", context)

def categoriesALL(request):
    car_card = Car_card.objects.all().order_by('-date')

    context = {
        'car_card': car_card
    }
    return render(request,"./categoriesALL.html", context)


def car_card(request, pk):
    car_card = get_object_or_404(Car_card, pk=pk)
    context={
        'car_card': car_card
    }

    return render(request,"./car_card.html", context)
def infoNews(request, pk):
    news = get_object_or_404(News, pk=pk)
    context={
        'news': news
    }

    return render(request,"./infoNews.html", context)

#---------------------------------------------------------------------------------

# single view
def all_cars(request):
    car_card = Car_card.objects.all()

    context = {
        'car_card': car_card
    }
    return render(request,"./all-cars.html", context)

def news(request):
    news = News.objects.all()

    context = {
        'news': news
    }

    return render(request,"./news.html", context)


logger = logging.getLogger(__name__)
def user_sign(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = NewUserForm()
    
    context = {
        'form': form
    }

    return render(request,"./signUp.html", context)



def user_login(request):
    form = CustomLoginForm()

    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        CustomLoginForm()

    context = {
        'form': form
    }
    return render(request,"./login.html", context)


def logout_action(request):
    logout(request)
    return redirect('home')
#-----------------------------------------------------------------------