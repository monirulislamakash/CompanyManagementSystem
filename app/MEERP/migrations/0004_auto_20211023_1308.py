# Generated by Django 3.2.6 on 2021-10-23 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MEERP', '0003_auto_20211020_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstudent',
            name='GENDER',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='Male', max_length=50),
        ),
        migrations.AlterField(
            model_name='userteacher',
            name='DNID',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Acounts', 'Acounts')], default='Teacher', max_length=50),
        ),
        migrations.AlterField(
            model_name='userteacher',
            name='GENDER',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='Male', max_length=50),
        ),
    ]
