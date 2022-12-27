from django.db import models
from django.utils import timezone

from accounts.models import CustomUser


class Party(models.Model):

    user = models.ForeignKey(
        CustomUser,
        verbose_name='作成者',
        on_delete=models.CASCADE,
        default=CustomUser
    )
    title = models.CharField(
        verbose_name='飲み会名',
        max_length=100,
    )
    date = models.DateField(
        verbose_name='予約日'
    )
    time = models.TimeField(
        verbose_name='時間'
    )
    restaurant = models.CharField(
        verbose_name='店舗名',
        max_length=100,
    )
    address = models.CharField(
        verbose_name='場所',
        max_length=500,
    )
    url = models.URLField(
        verbose_name='店舗リンク'
    )
    subscriber = models.CharField(
        verbose_name='予約者名',
        max_length=100,
    )
    fee = models.PositiveIntegerField(
        verbose_name='会費'
    )
    comment = models.TextField(
        verbose_name='コメント'
    )
    create_dt = models.DateTimeField(
        verbose_name='作成日時', #自動的にしたい場合 auto_now_add=True → 採用：default=timezone.now
        default=timezone.now,
    )
    mod_dt = models.DateTimeField(
        verbose_name='編集日時', #自動的にしたい場合 auto_now=True → 採用：default=timezone.now
        default=timezone.now,    
    )

    def __str__(self):
        return self.title
