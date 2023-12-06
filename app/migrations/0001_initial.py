# Generated by Django 4.2.7 on 2023-12-06 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept_name',
            fields=[
                ('dname', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Dept_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_head', models.CharField(max_length=20)),
                ('dept_url', models.URLField()),
                ('dname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept_name')),
            ],
        ),
        migrations.CreateModel(
            name='Dept_Faculty_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=10)),
                ('subj', models.CharField(max_length=20)),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept_info')),
            ],
        ),
    ]
