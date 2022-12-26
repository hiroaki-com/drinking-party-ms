from django.db import models

from accounts.models import CustomUser


class Party(models.Model):


    party_name = models.CharField(
        verbose_name='飲み会名'
    )

    date = models.DateField(
        verbose_name='予約日'
    )

    time = models.TimeField(
        verbose_name='時間'
    )

    restaurant = models.CharField(
        verbose_name='店舗名'
    )

    address = models.Charfield(
        verbose_name='場所'
    )

    url = models.URLField(
        verbose_name='店舗リンク'
    )

    subscriber = models.CharField(
        verbose_name='予約者名'
    )

    fee = models.PositiveIntegerField(
        verbose_name='会費'
    )

    comment = models.TextField(
        verbose_name='コメント'
    )

    create_dt = models.DateTimeField(
        verbose_name='作成日時'
    )

    mod_dt = models.DateTimeField(
        verbose_name='編集日時'
    )


    def__str__(self):

　　　　    return self.party_name
