# Generated by Django 3.1.1 on 2020-10-25 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload_video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('grade', models.IntegerField(blank=True, null=True)),
                ('video', models.FileField(upload_to='video')),
            ],
        ),
    ]
