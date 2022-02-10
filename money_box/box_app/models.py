from django.contrib.auth.models import User
from django.db.models import ForeignKey, CASCADE, DateField


class Child(User):
    parent = ForeignKey(User, on_delete=CASCADE, verbose_name='Родитель', related_name='children')
    birth_day = DateField(verbose_name='Дата рождения ребенка')
