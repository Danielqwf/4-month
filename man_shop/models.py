from django.db import models

class Shop(models.Model):
    COLOR = (
        ('Белый', 'Белый'),
        ('Черный', 'Черный'),
        ('Красный', 'Красный'),
        ('Серый', 'Серый')
    )

    BRAND = (
        ('Artem Shumov', 'Artem Shumov'),
        ('Altea', 'Altea'),
        ('Dal Lago', 'Dal Lago'),
        ('Nike', 'Nike'),
    )


    name = models.CharField('Название: ', max_length=100)
    color = models.CharField('Цвет: ', max_length=100, choices=COLOR)
    size = models.CharField('Размер: ', max_length=100, default='l(50)')
    prise = models.IntegerField('Цена: ')
    image = models.ImageField('Фото продукта: ', upload_to='')
    production = models.CharField('Производство: ', max_length=50)
    material = models.CharField('Материал: ', max_length=100, default='Хлопок')
    brand = models.CharField('Бренд:', max_length=100, choices=BRAND)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name
