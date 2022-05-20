# Generated by Django 4.0.4 on 2022-05-19 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Male', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Number',
            field=models.PositiveIntegerField(null=True, unique=True),
        ),
    ]