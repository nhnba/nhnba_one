# Generated by Django 2.2.16 on 2020-10-13 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='vip_expire',
            field=models.DateTimeField(default='3000-12-31', verbose_name='VIP的过期时间'),
        ),
        migrations.AddField(
            model_name='user',
            name='vip_id',
            field=models.IntegerField(default=1, verbose_name='用户购买的VIP的ID'),
        ),
    ]