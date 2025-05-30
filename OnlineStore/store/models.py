from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Категория',
    )
    description = models.TextField(
        blank=True, 
        verbose_name="Описание"
    )
    parent_category = models.ForeignKey(
        'self',
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='children', 
        verbose_name="Родительская категория"
    )  # Связь с самой собой для подкатегорий
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('-id',)

    def __str__(self):
        return self.name
    

class Brands(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Бренд',
    )

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name
    

class Models(models.Model):
    brand = models.ForeignKey(
        Brands,
        on_delete=models.PROTECT,
        related_name='models',
        verbose_name='Модель',
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Название',
    )

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return f'{self.brand} {self.name}'


class Item(models.Model):
    title = models.CharField(
        max_length=200, 
        verbose_name='Название',
    )
    description = models.TextField(
        verbose_name='Описание',
        )
    slug = models.CharField(
        unique=True,
        max_length=50,
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата добавления',
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Цена',
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='items/',
        blank=True,
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name='Доступно',
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name='Категория',
    )
    model = models.ForeignKey(
        Models,
        on_delete=models.PROTECT,
        related_name='models',
        verbose_name='Модель',
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-price']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Characteristics(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Характеристика',
    )
    type = models.CharField(
        max_length=255,
        verbose_name='Тип',
    )


class ItemCharacteristics(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        verbose_name='Товар',
    )
    characteristics = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        verbose_name='Характеристика',
    )
    value = models.CharField(
        max_length=255,
        verbose_name='Значение',
    )


class Promotion(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Акция',
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    start_date = models.DateTimeField(
        verbose_name='Дата начала',
    )
    end_date = models.DateTimeField(
        verbose_name='Дата окончания',
    )
    discount_value = models.DecimalField(
        verbose_name='Значение скидки',
    )
    conditions = models.TextField(
        verbose_name='Условия применения',
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name='Активно',
    )

    def __str__(self):
            return self.name
    
    class Meta:
        ordering = ['-start_date']
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'


class ItemPromotion(models.Model):
    item = models.ForeignKey(
        Item, 
        on_delete=models.CASCADE, 
        verbose_name = 'Товар')
    promotion = models.ForeignKey(
        Promotion, 
        on_delete=models.CASCADE, 
        verbose_name = 'Акция')
    
    class Meta:
        ordering = ['promotion']
        verbose_name = 'Акционный товар'
        verbose_name_plural = 'Акционные товары'


class Review(models.Model):
    product = models.ForeignKey(
        Item,
        related_name='reviews',
        on_delete=models.PROTECT,
        verbose_name='Товар'
    )
    user = models.ForeignKey(
        User,
        verbose_name='Имя',
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг'
    )
    review = models.TextField(
        max_length=255,
        verbose_name='Отзыв'
    )
    review_date = models.DateTimeField(
        verbose_name= 'Дата отзыва'
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name
    