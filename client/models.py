from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from config.settings import SHADE_GROUP_CHOICES, SKIN_TYPE_CHOICES, AGE_RANGE_CHOICES

from client.managers import MyAccountManager
from client.validators import validate_english


class Account(AbstractUser):
    """ My user model """
    username = None

    firstname = models.CharField('first name',
                                 max_length=100,
                                 validators=[validate_english])
    lastname = models.CharField('last name',
                                max_length=100,
                                validators=[validate_english])
    email = models.EmailField(unique=True)
    skin_type = models.CharField('skin type',
                                 max_length=25,
                                 choices=SKIN_TYPE_CHOICES,
                                 blank=True, null=True)
    shade_group = models.CharField('shade group',
                                   max_length=20,
                                   choices=SHADE_GROUP_CHOICES,
                                   blank=True, null=True)
    age_range = models.CharField('age range',
                                 max_length=10,
                                 choices=AGE_RANGE_CHOICES,
                                 blank=True, null=True)
    date_joined = models.DateField('date joined',
                                   default=timezone.now)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    def __str__(self):
        return f'{self.email}'
