# Generated by Django 4.0.3 on 2022-03-21 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journalist', '0003_alter_journalist_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journalist.journalist'),
        ),
    ]
