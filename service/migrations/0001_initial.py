# Generated by Django 3.1.3 on 2020-11-15 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('fonction', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('tel', models.CharField(max_length=40)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Agents',
                'verbose_name_plural': 'Agents',
            },
        ),
        migrations.CreateModel(
            name='CatProjet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/CatProjet')),
                ('description', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'CatProjet',
                'verbose_name_plural': 'CatProjets',
            },
        ),
        migrations.CreateModel(
            name='Propriete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('titre', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('commentaire', models.TextField()),
                ('image1', models.ImageField(upload_to='images/Propriete')),
                ('image2', models.ImageField(upload_to='images/Propriete')),
                ('image3', models.ImageField(upload_to='images/Propriete')),
                ('ville', models.CharField(max_length=255)),
                ('prix', models.FloatField(null=True)),
                ('quartier', models.CharField(max_length=255)),
                ('situation', models.CharField(max_length=255)),
                ('superficie', models.FloatField(null=True)),
                ('douche', models.IntegerField(null=True)),
                ('chambre', models.IntegerField(null=True)),
                ('garage', models.BooleanField(default=False)),
                ('statu', models.CharField(max_length=20)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Propriete',
                'verbose_name_plural': 'Proprietes',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('fonction', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/Services')),
                ('description', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('cat_projet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Catprojet', to='service.catprojet')),
            ],
            options={
                'verbose_name': 'Projet',
                'verbose_name_plural': 'Projets',
            },
        ),
    ]
