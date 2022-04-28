# Generated by Django 4.0.3 on 2022-04-26 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalist', '0005_post_editor_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='../client/static/image'),
        ),
    ]