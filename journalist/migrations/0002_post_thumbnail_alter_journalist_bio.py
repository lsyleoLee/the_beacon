# Generated by Django 4.0.3 on 2022-03-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='journalist',
            name='bio',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
