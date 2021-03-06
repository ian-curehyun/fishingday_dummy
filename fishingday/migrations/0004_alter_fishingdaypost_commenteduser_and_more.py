# Generated by Django 4.0 on 2021-12-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishingday', '0003_alter_fishingdaypost_posttext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishingdaypost',
            name='commentedUser',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fishingdaypost',
            name='fishGeo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fishingdaypost',
            name='fishName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fishingdaypost',
            name='fishSize',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fishingdaypost',
            name='fishimage',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fishingdaypost',
            name='fishingCertification',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fishingdaypost',
            name='fishingDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fishingdaypost',
            name='fishingMethod',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fishingdaypost',
            name='fishingbait',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fishingdaypost',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fishingdaypost',
            name='likedUser',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fishingdaypost',
            name='youtube',
            field=models.URLField(blank=True, null=True),
        ),
    ]
