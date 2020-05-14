# Generated by Django 3.0.5 on 2020-05-14 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Readlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReadlistManga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manga.Manga')),
                ('readlist', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manga.Readlist')),
            ],
        ),
        migrations.AddField(
            model_name='readlist',
            name='manga',
            field=models.ManyToManyField(through='manga.ReadlistManga', to='manga.Manga'),
        ),
    ]