# Generated by Django 3.1.3 on 2020-12-04 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0010_tweet_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='reply',
            field=models.BooleanField(default=False, verbose_name='Is a reply?'),
        ),
    ]
