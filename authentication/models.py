from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser,UserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from datetime import datetime, timedelta
import jwt
# Create your models here.

class CustomUserManager(UserManager):
    
    """Define a model manager for Custom User model"""

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        if not password:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser,PermissionsMixin):
    '''Custom User model with email based authentication'''

    name = models.CharField(
        _('name'),
        max_length=150,
    )
    
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    
    @property
    def token(self):
        '''Generates a JSON Web Token that stores user's name and email and has validity of 20 hours'''

        token = jwt.encode(
            {'name':self.name,'email':self.email,'exp':datetime.now()+timedelta(hours=20)},
            settings.SECRET_KEY,algorithm='HS256')
        return token
