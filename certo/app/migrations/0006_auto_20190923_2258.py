# Generated by Django 2.2.4 on 2019-09-23 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_produto_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='marca',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.Marca'),
        ),
    ]
