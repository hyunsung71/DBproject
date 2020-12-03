# Generated by Django 3.1.3 on 2020-12-03 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Additional Service',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='BookedDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('day', models.DateField(null=True)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('checkin', models.DateField()),
                ('checkout', models.DateField()),
                ('card', models.CharField(blank=True, choices=[('삼성카드', '삼성카드'), ('국민카드', '국민카드'), ('롯데카드', '롯데카드')], max_length=20)),
                ('cardNum', models.IntegerField(blank=True, null=True)),
                ('cardExpYear', models.CharField(default='****', max_length=4)),
                ('cardExpMonth', models.CharField(default='**', max_length=2)),
                ('additionalService', models.ManyToManyField(blank=True, to='reservations.AdditionalService')),
                ('bedtype', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='rooms.bedtype')),
                ('roomtype', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='rooms.roomtype')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
