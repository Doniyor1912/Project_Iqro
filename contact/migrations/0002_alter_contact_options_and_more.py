# Generated by Django 5.1.3 on 2024-12-04 08:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('full_name',), 'verbose_name_plural': 'Contact'},
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.AddField(
            model_name='contact',
            name='email_address',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='contact',
            name='full_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, default=''),
        ),
    ]
