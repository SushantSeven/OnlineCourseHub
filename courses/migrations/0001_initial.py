# Generated by Django 4.2.3 on 2023-07-26 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=False)),
                ('thumbnail', models.ImageField(upload_to='file/thumbnail')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('resource', models.ImageField(upload_to='files/resources')),
                ('length', models.IntegerField()),
            ],
        ),
    ]
