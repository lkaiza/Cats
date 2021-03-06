# Generated by Django 3.0.6 on 2020-05-09 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('life_style', models.CharField(max_length=150, verbose_name='Образ жизни')),
                ('care', models.CharField(max_length=150, verbose_name='Уход')),
                ('attachment', models.CharField(max_length=150, verbose_name='Привязанность')),
                ('activity', models.CharField(max_length=150, verbose_name='Активность')),
                ('sociability', models.CharField(max_length=150, verbose_name='Общительность')),
                ('noisiness', models.CharField(max_length=150, verbose_name='Разговорчивость')),
            ],
            options={
                'verbose_name': 'Characteristics',
                'verbose_name_plural': 'Characteristicss',
            },
        ),
        migrations.CreateModel(
            name='TypeOfWool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Тип шерсти')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'TypeOfWool',
                'verbose_name_plural': 'TypeOfWools',
            },
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Порода')),
                ('height', models.IntegerField(verbose_name='Рост')),
                ('weight', models.IntegerField(verbose_name='Вес')),
                ('health', models.CharField(max_length=250, verbose_name='Здоровье')),
                ('life_span', models.IntegerField(verbose_name='Продолжительность жизни')),
                ('country_of_origin', models.CharField(max_length=50, verbose_name='Страна происхождения')),
                ('about', models.CharField(max_length=550, verbose_name='О породе')),
                ('lifestyle', models.CharField(max_length=550, verbose_name='Образ жизни')),
                ('qualities', models.CharField(max_length=250, verbose_name='Качесва')),
                ('img', models.ImageField(upload_to='image/', verbose_name='Изображение')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('characteristics', models.ManyToManyField(to='cats.Characteristics', verbose_name='Характеристики')),
                ('type_of_wool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cats.TypeOfWool', verbose_name='Тип шерсти')),
            ],
            options={
                'verbose_name': 'Cat',
                'verbose_name_plural': 'Cats',
            },
        ),
    ]
