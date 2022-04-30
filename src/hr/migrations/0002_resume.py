# Generated by Django 4.0.2 on 2022-04-30 20:14

import concurrency.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hr.basemodel')),
                ('state', models.CharField(choices=[('DRAFT', 'Черновое'), ('PUBLISHED', 'Опубликовано'), ('HIDDEN', 'Скрыто')], default='DRAFT', max_length=25, verbose_name='Состояние')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Содержимое')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата/Время создания')),
                ('published_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата/Время публикации')),
                ('_version', concurrency.fields.IntegerVersionField(default=0, help_text='record revision number')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.user')),
            ],
            options={
                'verbose_name': 'Резюме',
                'verbose_name_plural': 'Резюме',
            },
            bases=('hr.basemodel',),
        ),
    ]
