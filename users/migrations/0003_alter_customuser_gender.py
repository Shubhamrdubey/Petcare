# Generated by Django 4.0.4 on 2022-05-19 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_gender_alter_customuser_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10, null=True),
        ),
    ]
