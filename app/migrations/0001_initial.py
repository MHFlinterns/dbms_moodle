# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-02 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.BigIntegerField(unique=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('dob', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('content', models.CharField(max_length=3000, null=True)),
                ('quiz', models.CharField(max_length=3000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('syllabus', models.CharField(max_length=1000)),
                ('credits', models.IntegerField()),
                ('fees', models.IntegerField()),
                ('durationWeeks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.BigIntegerField(unique=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('dob', models.DateField()),
                ('institute', models.CharField(max_length=200)),
                ('department', models.CharField(choices=[('AE', 'Aerospace Engineering'), ('AG', 'Agricultural & Food Engineering'), ('AR', 'Architecture & Regional Planning'), ('BT', 'Biotechnology'), ('CH', 'Chemical Engineering'), ('CY', 'Chemistry'), ('CE', 'Civil Engineering'), ('CS', 'Computer Science & Engineering'), ('EE', 'Electrical Engineering'), ('EC', 'Electronics & Electrical Communication Engineering'), ('GG', 'Geology & Geophysics'), ('HS', 'Humanities & Social Sciences'), ('IE', 'Industrial & Systems Engineering'), ('MA', 'Mathematics'), ('ME', 'Mechanical Engineering'), ('MT', 'Metallurgical & Materials Engineering'), ('MI', 'Mining Engineering'), ('NA', 'Ocean Engineering & Naval Architecture'), ('PH', 'Physics')], max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notif_from_role', models.CharField(choices=[('S', 'Student'), ('F', 'Faculty'), ('A', 'Admin')], max_length=10)),
                ('notif_from_id', models.IntegerField()),
                ('notif_to_role', models.CharField(choices=[('S', 'Student'), ('F', 'Faculty'), ('A', 'Admin')], max_length=10)),
                ('notif_to_id', models.IntegerField()),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PendingFaculty',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.BigIntegerField(unique=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('dob', models.DateField()),
                ('institute', models.CharField(max_length=200)),
                ('department', models.CharField(choices=[('AE', 'Aerospace Engineering'), ('AG', 'Agricultural & Food Engineering'), ('AR', 'Architecture & Regional Planning'), ('BT', 'Biotechnology'), ('CH', 'Chemical Engineering'), ('CY', 'Chemistry'), ('CE', 'Civil Engineering'), ('CS', 'Computer Science & Engineering'), ('EE', 'Electrical Engineering'), ('EC', 'Electronics & Electrical Communication Engineering'), ('GG', 'Geology & Geophysics'), ('HS', 'Humanities & Social Sciences'), ('IE', 'Industrial & Systems Engineering'), ('MA', 'Mathematics'), ('ME', 'Mechanical Engineering'), ('MT', 'Metallurgical & Materials Engineering'), ('MI', 'Mining Engineering'), ('NA', 'Ocean Engineering & Naval Architecture'), ('PH', 'Physics')], max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.BigIntegerField(unique=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('dob', models.DateField()),
                ('parent_email_id', models.EmailField(max_length=254)),
                ('institute', models.CharField(max_length=200)),
                ('year', models.IntegerField(choices=[(1, 'Freshman'), (2, 'Sophomore'), (3, 'Junior'), (4, 'Senior'), (5, 'Graduate')])),
                ('department', models.CharField(choices=[('AE', 'Aerospace Engineering'), ('AG', 'Agricultural & Food Engineering'), ('AR', 'Architecture & Regional Planning'), ('BT', 'Biotechnology'), ('CH', 'Chemical Engineering'), ('CY', 'Chemistry'), ('CE', 'Civil Engineering'), ('CS', 'Computer Science & Engineering'), ('EE', 'Electrical Engineering'), ('EC', 'Electronics & Electrical Communication Engineering'), ('GG', 'Geology & Geophysics'), ('HS', 'Humanities & Social Sciences'), ('IE', 'Industrial & Systems Engineering'), ('MA', 'Mathematics'), ('ME', 'Mechanical Engineering'), ('MT', 'Metallurgical & Materials Engineering'), ('MI', 'Mining Engineering'), ('NA', 'Ocean Engineering & Naval Architecture'), ('PH', 'Physics')], max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='course',
            name='faculty',
            field=models.ManyToManyField(to='app.Faculty'),
        ),
        migrations.AddField(
            model_name='course',
            name='pre_requisites',
            field=models.ManyToManyField(blank=True, null=True, related_name='_course_pre_requisites_+', to='app.Course'),
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(blank=True, null=True, to='app.Student'),
        ),
        migrations.AddField(
            model_name='calendar',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Course'),
        ),
        migrations.AlterUniqueTogether(
            name='calendar',
            unique_together=set([('course', 'date')]),
        ),
    ]
