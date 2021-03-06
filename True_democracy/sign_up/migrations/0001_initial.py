# Generated by Django 2.1.1 on 2020-02-18 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aadhar_id', models.CharField(max_length=12, unique=True, verbose_name='Id')),
                ('PhNo1', models.CharField(max_length=10, verbose_name='PhNo1')),
                ('PhNo2', models.CharField(max_length=10, verbose_name='PhNo2')),
                ('date', models.DateField(verbose_name='DOB')),
                ('Name', models.CharField(max_length=150, verbose_name='Name')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
