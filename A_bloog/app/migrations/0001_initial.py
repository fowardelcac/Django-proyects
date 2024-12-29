# Generated by Django 5.1.4 on 2024-12-29 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=75, verbose_name='Author')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('content', models.CharField(max_length=500, verbose_name='Content')),
            ],
        ),
    ]
