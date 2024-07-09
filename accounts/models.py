from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out


def create_default_site(sender, **kwargs):
    Site.objects.get_or_create(
        id=0,
        name='admin',
        permission_level=0,
    )


def create_default_superuser(sender, **kwargs):
    user = get_user_model()
    try:
        user.objects.get(user_id=999, username='admin')
    except user.DoesNotExist:
        user.objects.create_superuser(
            user_id=999,
            username='admin',
            site=0,
            password='password',
        )


class CustomUserManager(BaseUserManager):
    """
    カスタムユーザーマネージャークラス
    """
    use_in_migration = True

    def _create_user(self, site_id, user_id, username, password, **extra_fields):
        """
        username, password より user を作成するクラス
        :param username:
        :param email:
        :param password:
        :param extra_fields:
        :return:
        """
        def is_integer(val):
            try:
                int(val)
                return True
            except ValueError:
                return False

        if not site_id and site_id != 0:
            raise ValueError('SITE IDは必須です。')
        if not user_id:
            raise ValueError('IDは必須です。')
        elif not is_integer(user_id):
            raise ValueError('IDは数値で設定してください。')
        if not username:
            raise ValueError('ユーザー名は必須です。')
        username = self.model.normalize_username(username)
        site = Site.objects.get(id=site_id)
        user = self.model(user_id=user_id, username=username, site_id=site, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, site_id, user_id, username, password=None, **extra_fields):
        """
        user を作成するクラス
        :param user_id:
        :param username:
        :param password:
        :param extra_fields:
        :return:
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(site_id, user_id, username, password, **extra_fields)

    def create_superuser(self, site_id, user_id, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(site_id, user_id, username, password, **extra_fields)


class Site(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    permission_level = models.IntegerField(default=0)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    カスタムユーザーモデルクラス
    """
    username_validator = UnicodeUsernameValidator()

    id = models.AutoField(primary_key=True)
    site_id = models.ForeignKey(Site, on_delete=models.CASCADE)
    user_id = models.CharField(unique=True, max_length=7)
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=False,
        help_text=_('必須。150文字以内'),
        validators=[username_validator, ],
    )
    email = models.EmailField(_('email address'), max_length=150, null=True, blank=True, default='')
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    is_superuser = models.BooleanField(_('is superuser'), default=False)

    objects = CustomUserManager()

    EMAIL_FIELD = ''
    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['site_id', 'username', ]

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('site_id', 'user_id', )

