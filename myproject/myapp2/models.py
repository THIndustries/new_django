from django.db import models
from django.utils import timezone


class User(models.Model): # Наследуемся от класса Model из модуля models
    name = models.CharField(max_length=100) # Указываем значения из модуля models
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, age: {self.age}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')


class Order(models.Model): # Модель заказа
    customer = models.ForeignKey(User, on_delete=models.CASCADE) # заказчик со ссылкой
    # на пользователя
    product = models.ManyToManyField(Product) # Указываем на продукты
    date_ordered = models.DateTimeField(auto_now_add=True) # Этот параметр идеально подходит
    # для поля, которое должно отображать дату создания и никогда не изменяться
    # после первоначального сохранения, например, created_at поле
    total_price = models.DecimalField(max_digits=8, decimal_places=2)



class Author(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    biography = models.TextField()
    email = models.EmailField()
    birthday = models.DateTimeField(default=timezone.now())

    @property
    def full_name(self):
        return f'{self.name} {self.lastname}'

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_published = models.BooleanField()
    views = models.IntegerField()

    def __str__(self):
        return f"Title is {self.title}"

    def get_summary(self):
        words = self.content.split()
        return f"{' '.join(words[:7])}..."