from django.db import models
from pytils.translit import slugify
from datetime import datetime

class Category(models.Model):
    name = models.CharField("Название категории", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)
    image = models.ImageField("Фотография", upload_to='category_images/', blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Car_card(models.Model):
    title = models.CharField("Название Машины", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Выбирите категорию", null=True)
    image = models.ImageField("Фотография", upload_to='car_images/', blank=True, null=True)
    company = models.CharField("AO", max_length=255)
    cost = models.CharField("Цена от:", max_length=255)
    discription = models.TextField("Описание:")
    transmision = models.CharField("Трансмиссия:", max_length=50)
    engineType = models.CharField("Тип двигателя:", max_length=20)
    engineCapacity = models.CharField("Объем Двигателя:", max_length=20)
    power = models.CharField("Мощность:", max_length=20)
    actuator = models.CharField("Привод:", max_length=20)
    address = models.CharField("Адрес:", max_length=100)
    number = models.CharField("Телефон:", max_length=20)
    email = models.CharField("E-mail:", max_length=200)
    date = models.DateTimeField("Дата публикации", default=datetime.now)

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"

    def __str__(self):
        return self.title
    
class News(models.Model):
    title = models.CharField("Заголовок", max_length=140)
    image = models.ImageField("Фотография", upload_to='news_images/', blank=True, null=True)
    discription = models.TextField("Описание:")
    date = models.DateTimeField("Дата публикации", default=datetime.now)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title