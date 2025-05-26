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
        verbose_name='Новая цена',
    )
    old_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Старая цена',
        blank=True,
        null=True,
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

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-price']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


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

    def __str__(self):
            return self.title
    
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

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name