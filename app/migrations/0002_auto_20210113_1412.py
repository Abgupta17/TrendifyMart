# Generated by Django 3.1.4 on 2021-01-13 08:42

from django.db import migrations, models # type: ignore


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='address',
            new_name='locality',
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(default='Sonam', max_length=200),
            preserve_default=False,
        ),
    ]
