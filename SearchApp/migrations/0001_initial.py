# Generated by Django 4.0.1 on 2022-01-06 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pillar', models.CharField(choices=[('Pillar1', 'Pillar1'), ('Pillar2', 'Pillar2'), ('Pillar3', 'Pillar3')], default='Pillar1', max_length=200)),
                ('sourceType', models.CharField(choices=[('sourceType1', 'Sourcetype1'), ('sourceType2', 'Sourcetype2'), ('sourceType3', 'Sourcetype3')], default='sourceType1', max_length=200)),
                ('market', models.CharField(choices=[('market1', 'Market1'), ('market2', 'Market2'), ('market3', 'Market3')], default='market1', max_length=200)),
                ('brandSource', models.CharField(choices=[('brandSource1', 'Brandsource1'), ('brandSource2', 'Brandsource2'), ('brandSource3', 'Brandsource3')], default='brandSource1', max_length=200)),
                ('review', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=150)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
