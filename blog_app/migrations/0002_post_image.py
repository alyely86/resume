# Generated by Django 5.1.3 on 2024-12-18 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/img/defult.jpg', upload_to='blog/'),
        ),
    ]