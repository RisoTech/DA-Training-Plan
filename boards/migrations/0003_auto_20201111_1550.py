# Generated by Django 3.1.3 on 2020-11-11 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0002_topic_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='posts', to='boards.topic'),
        ),
    ]
