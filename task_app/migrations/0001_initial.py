# Generated by Django 4.1 on 2022-08-22 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField(blank=True, max_length=300)),
                ('register', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='register_app.register', verbose_name='Member')),
            ],
            options={
                'db_table': 'tbl_task',
            },
        ),
    ]
