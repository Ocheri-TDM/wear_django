from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('categories/', views.categories, name='categories'),
    path('categories/list', views.categories_list, name='categories_list'),
    path('categories/<slug:slug>', views.categories_by_filtred, name='categories_by_filtred'),
    path('all', views.categoriesALL, name='categoriesALL'),
    path('car_card/detail/<int:pk>/', views.car_card, name='car_card'),
    path('infoNews/detail/<int:pk>/', views.infoNews, name='infoNews'),
    path('login', views.user_login, name='login'),
    path('news', views.news, name='news'),
    path('sign', views.user_sign, name='sign'),
    path('all-cars', views.all_cars, name='all-cars'),
    path('logout', views.logout_action, name ='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)