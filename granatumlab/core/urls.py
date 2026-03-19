from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls), # автоматическая админ панель для управления БД
    path('', views.show_home, name='home'), # главная
    path('about/', views.show_about, name='about'), # о проекте
    # Группируем страницы внутри "Сгенирировать блюдо"
    path('eat/', include(([
        path('', views.show_hub, name='hub'), # чат с нейронкой, кнопки и галочки
        path('result/<slug:res_slug>/', views.show_result, name='result'), # рецепт и где купить
    ], 'eat'))),  # 'eat' — это теперь имя группы, ее фамилия или иначе namespace - пространство имен

    # Группируем страницы "Личного кабинета"
    path('profile/', include(([
        path('', views.show_fridge, name='index'), # перенаправит на холодильник
        path('fridge/', views.show_fridge, name='fridge'), # холодильник
        path('info/', views.show_info, name='info'), # параметры пользователя
        path('shops/', views.show_shops, name='shops'), # магазины пользователя
    ], 'profile'))),  # 'profile' — имя группы
]



