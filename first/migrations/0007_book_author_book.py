# Generated by Django 4.2.3 on 2023-07-18 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0006_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='first.author'),
        ),
    ]
