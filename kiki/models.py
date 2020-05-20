from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError


def check_nensu(value):
    if value < 1 or value > 25:
        raise ValidationError('1〜25年が範囲です')


# Create your models here.
class Kiki(models.Model):
    kiki_id = models.CharField(verbose_name="機器ID", max_length=10)
    kiki_name = models.CharField(verbose_name="機器名称", max_length=30)
    keito = models.CharField(verbose_name="系統", max_length=30)
    settibasho = models.CharField(verbose_name="設置場所", max_length=30)
    juyodo = models.CharField(verbose_name="重要度", max_length=1,
                              validators=[RegexValidator(r'^[A-D]*$', 'A～Dが範囲です')])
    nensu = models.IntegerField(verbose_name="耐用年数", default=1,
                                validators=[check_nensu])

    def __str__(self):
        return self.kiki_id

    @staticmethod
    def get_absolute_url(self):
        return reverse('search:index')
