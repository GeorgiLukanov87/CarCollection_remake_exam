from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def validate_car_year(value):
    if value <= 1980 or value >= 2049:
        raise ValidationError('Year must be between 1980 and 2049!')


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[
            validators.MinLengthValidator(2, message='The username must be a minimum of 2 chars!'),
        ]
    )

    email = models.EmailField()
    age = models.PositiveIntegerField(
        validators=[
            validators.MinValueValidator(18, message='The age cannot be below 18!'),
        ]
    )

    password = models.CharField(
        max_length=30,
    )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )


class Car(models.Model):
    CAR_TYPE_CHOICES = (
        ('Sports Car', '1-Sports Car'),
        ('Pickup', '2-Pickup'),
        ('Crossover', '3-Crossover'),
        ('Minibus', '4-Minibus'),
        ('Other', '5-Other'),
    )

    type = models.CharField(
        max_length=10,
        choices=CAR_TYPE_CHOICES,
    )

    model = models.CharField(
        max_length=20,
        validators=[
            validators.MinLengthValidator(2, message='It should consist of a minimum of 2 characters!')
        ],
    )

    year = models.PositiveIntegerField(
        validators=[
            validate_car_year,
        ]
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=[validators.MinValueValidator(1, message='Price cannot be below 1!')]
    )
