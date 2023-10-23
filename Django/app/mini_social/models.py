from django.db.models import Model, CharField, DecimalField
from django.contrib.auth.models import User


class Post(Model):
    title = CharField(max_length=150)
    body  = CharField()


class CustomUser(User):
    rating = DecimalField(max_digits=2, decimal_places=1, default=0)
    avatar = CharField(max_length=60, default='')
