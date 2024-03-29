# Generated by Django 4.2.1 on 2023-05-31 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(default='', max_length=100, verbose_name='Prenom')),
                ('nom', models.CharField(default='', max_length=100, verbose_name='Nom')),
                ('email', models.CharField(default='', max_length=300, verbose_name='Email')),
                ('telephone', models.CharField(default='', max_length=50, verbose_name='Telephone')),
                ('occupation', models.CharField(default='', max_length=200, verbose_name='Occupation')),
                ('lienCv', models.CharField(default='', max_length=1000, verbose_name='Lien CV')),
            ],
        ),
    ]
