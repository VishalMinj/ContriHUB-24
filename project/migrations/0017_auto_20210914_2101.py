# Generated by Django 3.2.7 on 2021-09-14 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_rename_user_pullrequest_contributor'),
    ]

    operations = [
        migrations.AddField(
            model_name='pullrequest',
            name='bonus',
            field=models.IntegerField(default=0, verbose_name='Bonus'),
        ),
        migrations.AddField(
            model_name='pullrequest',
            name='penalty',
            field=models.IntegerField(default=0, verbose_name='Penalty'),
        ),
    ]