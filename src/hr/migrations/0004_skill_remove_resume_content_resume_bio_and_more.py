# Generated by Django 4.0.2 on 2022-06-04 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_remove_resume__version_vacancy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
            },
        ),
        migrations.RemoveField(
            model_name='resume',
            name='content',
        ),
        migrations.AddField(
            model_name='resume',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='Информация о себе'),
        ),
        migrations.AddField(
            model_name='resume',
            name='current_position',
            field=models.CharField(default='dummy', max_length=50, verbose_name='Текущаая должность'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='desired_position',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Желаемая должность'),
        ),
        migrations.AddField(
            model_name='resume',
            name='experience',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Опыт работы'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('APPLICANT', 'соискатель'), ('MANAGER', 'менеджер')], default='APPLICANT', max_length=25, verbose_name='Роль'),
        ),
        migrations.AddField(
            model_name='resume',
            name='skills',
            field=models.ManyToManyField(to='hr.Skill', verbose_name='Навыки'),
        ),
    ]