# Generated by Django 3.2.22 on 2024-02-09 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camera_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='crime_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='visitor_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('CAMERA', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Thief.camera')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Thief.login')),
            ],
        ),
        migrations.CreateModel(
            name='police_station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Thief.login')),
            ],
        ),
        migrations.CreateModel(
            name='familiar_person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('F_name', models.CharField(max_length=100)),
                ('F_place', models.CharField(max_length=100)),
                ('F_contact', models.CharField(max_length=100)),
                ('F_image', models.CharField(max_length=100)),
                ('USER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Thief.user')),
            ],
        ),
        migrations.CreateModel(
            name='familiar_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('CAMERA', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Thief.camera')),
                ('FAMILIAR_PERSON', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Thief.familiar_person')),
            ],
        ),
        migrations.CreateModel(
            name='criminals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=100)),
                ('POLICE', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Thief.police_station')),
            ],
        ),
        migrations.CreateModel(
            name='crimehistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=30)),
                ('history', models.CharField(max_length=300)),
                ('CATEGORY', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Thief.crime_category')),
                ('CRIMINAL', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Thief.criminals')),
            ],
        ),
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=500)),
                ('cdate', models.CharField(default='2024-02-09', max_length=20)),
                ('reply', models.CharField(default='pending', max_length=500)),
                ('rdate', models.CharField(default=0, max_length=20)),
                ('USER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Thief.user')),
            ],
        ),
        migrations.AddField(
            model_name='camera',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Thief.user'),
        ),
        migrations.CreateModel(
            name='alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('CAMERA', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Thief.camera')),
                ('CRIMINALS', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Thief.criminals')),
            ],
        ),
    ]
