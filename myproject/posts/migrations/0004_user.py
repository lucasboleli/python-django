# Generated by Django 5.1.1 on 2024-09-23 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
