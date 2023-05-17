import stripe

from django.db import models
from django.conf import settings

from users.models import User

# Create your models here.
stripe.api_key = settings.STRIPE_SECRET_KEY

class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    stripe_product_id = models.CharField(max_length=128, null=True, blank=True)
    image = models.ImageField(upload_to='product_images', null=True)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"Продукт: {self.name} | Категория: {self.category.name}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.stripe_product_id:
            stripe_product_price_responce = self.create_stripe_product_price()
            self.stripe_product_id = stripe_product_price_responce['id']
        super(Product, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'

    def create_stripe_product_price(self):
        stripe_product = stripe.Product.create(name=self.name)
        stripe_product_price = stripe.Price.create(
            product=stripe_product['id'],
            unit_amount=round(self.price*100),
            currency='rub'
        )
        return stripe_product_price


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)

    def stripe_products(self):
        line_items = []
        for product in self:
            item = {
                'price': product.product.stripe_product_id,
                'quantity': product.quantity,
            }
            line_items.append(item)
        return line_items


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.email} | product {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

    def de_json(self):
        basket_item = {
            'product_name': f'{self.product.name}',
            'quantity': self.quantity,
            'price': float(self.product.price),
            'sum': float(self.sum()),
        }

        return basket_item


